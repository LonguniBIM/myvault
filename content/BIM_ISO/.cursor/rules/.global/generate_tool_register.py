# coding: utf-8
"""
title: Tool Register Generator

tooltip:
  en_us: |
    Version = 1.0.0
    __________________________________________________________________
    Description:
    Scans all Python files in the workspace's source directory and 
    generates a comprehensive Tool Register Excel report with detailed 
    metadata about each script including purpose, dependencies, inputs, 
    outputs, and usage instructions. Works from any location within 
    the workspace by automatically detecting the workspace root.
    
    Prioritizes metadata extraction from bundle.yaml (if exists in same 
    directory as the script) over script docstrings, following pyRevit 
    bundle structure conventions.
    
    __________________________________________________________________
    Features:
    • Recursively scans all .py files in source folder
    • Prioritizes metadata from bundle.yaml over script docstrings
    • Extracts script metadata (name, purpose, description, I/O)
    • Parses docstrings and markdown comments automatically
    • Detects load_external_libs() calls for DCMvn modules
    • Generates structured Excel report with professional formatting
    • Auto-fits columns and applies table styling
    • Creates summary sheet with statistics by category/stage/language
    • Detects programming language (Python 3 vs IronPython 2.7)
    • Categorizes scripts by type and development stage
    
    __________________________________________________________________
    Input Files:
    • All Python (.py) files in the source directory
    • Excludes: __pycache__, .specstory, DCMvn, ExcelUtil folders
    • Excludes: __init__.py, generate_tool_register.py
    
    __________________________________________________________________
    Input Requirement:
    • Python scripts must have proper docstrings or markdown comments
    • Scripts should follow standard documentation format
    • Valid Python syntax for AST parsing
    
    __________________________________________________________________
    Output Files:
    • Tool Register - Generated [timestamp].xlsx
      - Sheet 1: Tool Register (detailed table with all scripts)
      - Sheet 2: Summary (statistics and counts)
    
    __________________________________________________________________
    How-to:
    • Step 1: Run the script from anywhere in the workspace
    • Step 2: Execute: python .cursor/rules/services/generate_tool_register.py
    • Step 3: Script will scan the 'source' folder in workspace root
    • Step 4: Open the generated Excel file in workspace root
    
    __________________________________________________________________
    Tool Options:
    • EXCLUDED_DIRS: Customize directories to exclude from scanning
    • EXCLUDED_FILES: Customize specific files to exclude
    • Column order and formatting can be modified in generate_report()
    
    __________________________________________________________________
    Changelogs:
    • [21.11.2024] - Added bundle.yaml support (priority over script docstrings)
    • [21.11.2024] - Added load_external_libs() detection for DCMvn modules
    • [19.11.2024] - Fixed relative path to scan workspace source directory
    • [19.11.2024] - Added automatic workspace root detection
    • [19.11.2024] - Initial version with full metadata extraction
    • [19.11.2024] - Added summary sheet with statistics
    • [19.11.2024] - Implemented AST parsing and docstring extraction
    • [19.11.2024] - Added programming language detection
    • [19.11.2024] - Added development stage categorization
    
    __________________________________________________________________

author: "Long Dang"
engine:
  clean: true
"""

import ast
import logging
import pandas as pd
import re
import warnings
import yaml
from pathlib import Path
from typing import Dict, List, Any, Optional
import xlwings as xw
from datetime import datetime

# Configure logging
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)

# Suppress warnings
warnings.filterwarnings('ignore')

# Global constants
# Get workspace root (go up from .cursor/rules/services/ to workspace root)
SCRIPT_DIR = Path(__file__).parent  # .cursor/rules/services/
WORKSPACE_ROOT = SCRIPT_DIR.parent.parent.parent  # Go up 3 levels to workspace root
SOURCE_DIR = WORKSPACE_ROOT / 'pyDCMvn.tab/MunichRE.panel'  # Target the source directory

EXCLUDED_DIRS = ['__pycache__', '.specstory', 'DCMvn', 'ExcelUtil', 'IFCTypeEnum_v25.4.3', '.cursor', 'template']
EXCLUDED_FILES = ['__init__.py', 'generate_tool_register.py']

class ScriptAnalyzer:
    """Analyzes Python scripts to extract metadata."""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = ""
        self.lines = []
        self.ast_tree = None
        self.bundle_yaml = None  # Store bundle.yaml data if found
    
    @staticmethod
    def join_multiline_to_sentence(text: str) -> str:
        """
        Join multiple lines into a single sentence.
        Detects line breaks and combines them intelligently.
        Preserves original capitalization and formatting.
        """
        if not text or text == 'N/A':
            return text
        
        # Split by newlines
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return text
        
        # Join lines into a single sentence, preserving original capitalization
        result = []
        for i, line in enumerate(lines):
            if i == 0:
                result.append(line)
            else:
                # If previous line ends with punctuation, keep next line as is
                if result[-1][-1] in '.!?':
                    result.append(line)
                else:
                    # Otherwise, just add the line as is (preserve original capitalization)
                    result.append(line)
        
        return ' '.join(result)
        
    def read_file(self) -> bool:
        """Read file content."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
            return True
        except Exception as e:
            logger.warning(f"Error reading {self.file_path}: {e}")
            return False
    
    def read_bundle_yaml(self) -> Optional[Dict]:
        """
        Read bundle.yaml file from the same directory as the Python script.
        Returns the parsed YAML data or None if not found.
        """
        bundle_path = self.file_path.parent / 'bundle.yaml'
        
        if not bundle_path.exists():
            return None
        
        try:
            with open(bundle_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                logger.debug(f"Found bundle.yaml for {self.file_path.name}")
                return data
        except Exception as e:
            logger.warning(f"Error reading bundle.yaml for {self.file_path.name}: {e}")
            return None
    
    def _get_tooltip_text(self) -> Optional[str]:
        """Extract tooltip text from bundle.yaml."""
        if not self.bundle_yaml:
            return None
        
        tooltip = self.bundle_yaml.get('tooltip')
        if not tooltip:
            return None
        
        # Handle both string and dict formats
        if isinstance(tooltip, str):
            return tooltip.strip()
        elif isinstance(tooltip, dict):
            # Try en_us first, then any other key
            return tooltip.get('en_us', '').strip() or next(iter(tooltip.values()), '').strip()
        
        return None
    
    def extract_author(self) -> str:
        """Extract author from bundle.yaml or default."""
        # Priority 1: Check bundle.yaml
        if self.bundle_yaml:
            author = self.bundle_yaml.get('author')
            if author:
                return author.strip().strip('"\'')
        
        # Priority 2: Default author
        return 'lk.dang'
    
    def parse_ast(self) -> bool:
        """Parse AST tree."""
        try:
            self.ast_tree = ast.parse(self.content)
            return True
        except SyntaxError:
            return False
    
    def extract_docstring(self) -> str:
        """Extract module-level docstring."""
        if self.ast_tree:
            docstring = ast.get_docstring(self.ast_tree)
            if docstring:
                return docstring.strip()
        
        # Fallback: extract from first triple-quoted string
        pattern = r'"""(.*?)"""'
        match = re.search(pattern, self.content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        pattern = r"'''(.*?)'''"
        match = re.search(pattern, self.content, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        return ""
    
    def parse_structured_sections(self) -> Dict[str, str]:
        """Parse structured docstring sections separated by underscores."""
        docstring = self.extract_docstring()
        if not docstring:
            return {}
        
        sections = {}
        current_section = None
        current_content = []
        
        lines = docstring.split('\n')
        
        for line in lines:
            line_stripped = line.strip()
            
            # Check if this is a section header (ends with : and next line has ___)
            if line_stripped.endswith(':') and not line_stripped.startswith('•') and not line_stripped.startswith('-'):
                # Save previous section
                if current_section:
                    sections[current_section] = '\n'.join(current_content).strip()
                    current_content = []
                
                # Start new section
                potential_section = line_stripped[:-1].strip()
                if potential_section in ['Description', 'Features', 'Input Files', 'Input Requirement', 
                                        'Output Files', 'How-to', 'Tool Options', 'Changelogs']:
                    current_section = potential_section
            elif line_stripped.startswith('_____'):
                # Separator line - skip
                continue
            elif current_section:
                # Add to current section content
                if line_stripped:  # Only add non-empty lines
                    current_content.append(line_stripped)
        
        # Save last section
        if current_section:
            sections[current_section] = '\n'.join(current_content).strip()
        
        return sections
    
    def extract_markdown_purpose(self) -> str:
        """Extract purpose from markdown cells (Jupyter-style comments)."""
        markdown_content = []
        in_markdown = False
        
        for line in self.lines[:100]:  # Check first 100 lines
            if line.strip().startswith('# %% [markdown]'):
                in_markdown = True
                continue
            elif line.strip().startswith('# %%'):
                in_markdown = False
            elif in_markdown and line.startswith('#'):
                markdown_content.append(line[1:].strip())
        
        return '\n'.join(markdown_content) if markdown_content else ""
    
    def extract_purpose(self) -> str:
        """Extract script purpose/description."""
        # Priority 1: Check bundle.yaml first
        if self.bundle_yaml:
            tooltip = self._get_tooltip_text()
            if tooltip:
                # Extract purpose from Description section
                lines = tooltip.split('\n')
                purpose_lines = []
                in_description = False
                
                for line in lines:
                    line_stripped = line.strip()
                    
                    # Detect Description section
                    if 'description:' in line_stripped.lower():
                        in_description = True
                        continue
                    
                    # Stop at other sections or separators
                    if in_description and any(marker in line_stripped for marker in ['Features:', 'How-to:', 'Input Files:', 'Output Files:', '__________']):
                        break
                    
                    # Collect description lines
                    if in_description and line_stripped:
                        purpose_lines.append(line_stripped)
                
                if purpose_lines:
                    desc = ' '.join(purpose_lines)
                    # Limit to reasonable length
                    if len(desc) > 200:
                        sentences = desc.split('.')
                        return '. '.join(sentences[:2]).strip() + '.'
                    return desc
        
        # Priority 2: Try structured sections from docstring (new format)
        sections = self.parse_structured_sections()
        if 'Description' in sections:
            desc = sections['Description']
            # Join multiple lines into single sentence
            desc = self.join_multiline_to_sentence(desc)
            # Limit to reasonable length (first 200 chars or 2 sentences)
            if len(desc) > 200:
                sentences = desc.split('.')
                return '. '.join(sentences[:2]).strip() + '.'
            return desc
        
        # Try markdown (old format)
        markdown = self.extract_markdown_purpose()
        if markdown:
            lines = markdown.split('\n')
            purpose_lines = []
            in_purpose = False
            
            for line in lines:
                if 'purpose' in line.lower() or 'description' in line.lower():
                    in_purpose = True
                    continue
                elif line.strip().startswith('---') or line.strip().startswith('###'):
                    if in_purpose:
                        break
                elif in_purpose and line.strip():
                    purpose_lines.append(line.strip())
            
            if purpose_lines:
                return ' '.join(purpose_lines[:3])
        
        # Try docstring (fallback)
        docstring = self.extract_docstring()
        if docstring:
            lines = [line.strip() for line in docstring.split('\n') if line.strip()]
            
            # Find Purpose section
            for i, line in enumerate(lines):
                if 'purpose' in line.lower():
                    purpose_lines = []
                    for j in range(i+1, min(i+5, len(lines))):
                        if lines[j] and not lines[j].startswith('-'):
                            purpose_lines.append(lines[j])
                    if purpose_lines:
                        return ' '.join(purpose_lines)
            
            # Fallback: first few lines
            return ' '.join(lines[:2])
        
        return "No description available"
    
    def extract_features(self) -> List[str]:
        """Extract key features from docstring or markdown."""
        # Priority 1: Check bundle.yaml first
        if self.bundle_yaml:
            tooltip = self._get_tooltip_text()
            if tooltip:
                features = []
                lines = tooltip.split('\n')
                in_features = False
                current_feature = []
                
                for line in lines:
                    line_stripped = line.strip()
                    
                    # Detect Features section
                    if 'Features:' in line_stripped or 'features:' in line_stripped:
                        in_features = True
                        continue
                    
                    # Stop at other sections
                    if in_features and any(marker in line_stripped for marker in ['How-to:', 'Last update:', 'Input', 'Output', '__________']):
                        break
                    
                    if in_features:
                        if (line_stripped.startswith('-') or line_stripped.startswith('•')) and current_feature:
                            # Save previous feature
                            feature_text = self.join_multiline_to_sentence('\n'.join(current_feature))
                            features.append('• ' + feature_text.lstrip('•-').strip())
                            current_feature = [line_stripped.lstrip('•-').strip()]
                        elif line_stripped.startswith('-') or line_stripped.startswith('•'):
                            current_feature = [line_stripped.lstrip('•-').strip()]
                        elif line_stripped and current_feature:
                            current_feature.append(line_stripped)
                
                # Add last feature
                if current_feature:
                    feature_text = self.join_multiline_to_sentence('\n'.join(current_feature))
                    features.append('• ' + feature_text.lstrip('•-').strip())
                
                if features:
                    return features
        
        # Priority 2: Try structured sections from docstring (new format)
        sections = self.parse_structured_sections()
        if 'Features' in sections:
            features_text = sections['Features']
            features = []
            current_feature = []
            
            for line in features_text.split('\n'):
                line = line.strip()
                if (line.startswith('•') or line.startswith('-')) and current_feature:
                    # Save previous feature as single sentence
                    feature_text = self.join_multiline_to_sentence('\n'.join(current_feature))
                    features.append('• ' + feature_text.lstrip('•-').strip())
                    current_feature = [line.lstrip('•-').strip()]
                elif line.startswith('•') or line.startswith('-'):
                    # Start new feature
                    current_feature = [line.lstrip('•-').strip()]
                elif line and current_feature:
                    # Continue current feature
                    current_feature.append(line)
                elif line and not current_feature:
                    # Standalone line
                    features.append('• ' + line)
            
            # Add last feature
            if current_feature:
                feature_text = self.join_multiline_to_sentence('\n'.join(current_feature))
                features.append('• ' + feature_text.lstrip('•-').strip())
            
            return features  # Return all features
        
        # Try old format
        features = []
        content = self.extract_docstring() or self.extract_markdown_purpose()
        
        if not content:
            return features
        
        lines = content.split('\n')
        in_features = False
        
        for line in lines:
            line = line.strip()
            if 'feature' in line.lower() or 'key feature' in line.lower():
                in_features = True
                continue
            elif in_features:
                if line.startswith('-') or line.startswith('•'):
                    features.append('• ' + line.lstrip('-•').strip())
                elif line.startswith('###') or line.startswith('---'):
                    break
        
        return features[:5]
    
    def extract_usage(self) -> str:
        """Extract usage instructions."""
        # Priority 1: Check bundle.yaml first
        if self.bundle_yaml:
            tooltip = self._get_tooltip_text()
            if tooltip:
                steps = []
                lines = tooltip.split('\n')
                in_howto = False
                
                for line in lines:
                    line_stripped = line.strip()
                    
                    # Detect How-to section (case insensitive)
                    if 'how-to:' in line_stripped.lower() or 'usage:' in line_stripped.lower():
                        in_howto = True
                        continue
                    
                    # Stop at other sections
                    if in_howto and any(marker in line_stripped for marker in ['Last update:', 'Features:', '__________']):
                        break
                    
                    if in_howto and (line_stripped.startswith('-') or line_stripped.startswith('•') or 
                                    line_stripped.lower().startswith('step')):
                        steps.append('• ' + line_stripped.lstrip('•-').strip())
                    elif in_howto and line_stripped:
                        steps.append('• ' + line_stripped)
                
                if steps:
                    return '\n'.join(steps)
        
        # Priority 2: Try structured sections from docstring (new format)
        sections = self.parse_structured_sections()
        if 'How-to' in sections:
            howto_text = sections['How-to']
            # Extract steps and join multi-line steps into single sentences
            steps = []
            # current_step = []
            
            for line in howto_text.split('\n'):
                line = line.strip()
                if line.startswith('•') or line.startswith('-') or line.lower().startswith('step'):
                    steps.append('• ' + line.lstrip('•-').strip())
                elif line:
            #     if (line.startswith('•') or line.startswith('-') or line.lower().startswith('step')) and current_step:
            #         # Save previous step as single sentence
            #         step_text = self.join_multiline_to_sentence('\n'.join(current_step))
            #         steps.append('• ' + step_text.lstrip('•-').strip().lstrip('Step').lstrip(':').lstrip('0123456789').lstrip('.').lstrip(':').strip())
            #         current_step = [line.lstrip('•-').strip()]
            #     elif line.startswith('•') or line.startswith('-') or line.lower().startswith('step'):
            #         # Start new step
            #         current_step = [line.lstrip('•-').strip()]
            #     elif line and current_step:
            #         # Continue current step
            #         current_step.append(line)
            #     elif line and not current_step:
            #         # Standalone line
                    steps.append('• ' + line)
            
            # # Add last step
            # if current_step:
            #     step_text = self.join_multiline_to_sentence('\n'.join(current_step))
            #     steps.append('• ' + step_text.lstrip('•-').strip().lstrip('Step').lstrip(':').lstrip('0123456789').lstrip('.').lstrip(':').strip())
            
            if steps:
                return '\n'.join(steps)  # All steps with newlines
            return '• ' + howto_text  # Return full text with bullet
        
        # Try old format
        content = self.extract_docstring() or self.extract_markdown_purpose()
        
        if not content:
            return "N/A"
        
        lines = content.split('\n')
        in_usage = False
        usage_lines = []
        
        for line in lines:
            line = line.strip()
            if 'usage' in line.lower() or 'how to use' in line.lower():
                in_usage = True
                continue
            elif in_usage:
                if line.startswith('###') or line.startswith('---') or 'output' in line.lower():
                    break
                elif line:
                    usage_lines.append('• ' + line)
        
        return '\n'.join(usage_lines[:3]) if usage_lines else "N/A"
    
    def detect_programming_language(self) -> str:
        """Detect programming language from script header."""
        # Check first 10 lines for Python version indicators
        for line in self.lines[:10]:
            line = line.strip()
            
            # Check for Python 3 indicator
            if line.startswith('#!') and 'python3' in line.lower():
                return 'Python 3'
            
            # Check for pyRevit/IronPython indicators
            if 'ironpython' in line.lower():
                return 'IronPython 2.7'
            
            # Check for coding declaration (typically IronPython 2.7)
            if line.startswith('#') and 'coding:' in line.lower():
                return 'IronPython 2.7'
        
        # Check imports for Revit/pyRevit (indicates IronPython)
        content_lower = self.content[:1000].lower()
        if 'from dcmvn' in content_lower or 'import clr' in content_lower or 'autodesk.revit' in content_lower:
            return 'IronPython 2.7'
        
        # Default to Python 3 for modern scripts
        return 'Python 3'
    
    def extract_input_requirements(self) -> str:
        """Extract input requirements from docstring."""
        # Priority 1: Check bundle.yaml first
        if self.bundle_yaml:
            tooltip = self._get_tooltip_text()
            if tooltip:
                req_lines = []
                lines = tooltip.split('\n')
                in_requirements = False
                
                for line in lines:
                    line_stripped = line.strip()
                    
                    # Detect Input Requirement section
                    if 'input requirement' in line_stripped.lower():
                        in_requirements = True
                        continue
                    
                    # Stop at other sections
                    if in_requirements and any(marker in line_stripped for marker in ['Output', 'Features:', 'How-to:', 'Last update:', '__________']):
                        break
                    
                    if in_requirements and (line_stripped.startswith('-') or line_stripped.startswith('•')):
                        req_lines.append('• ' + line_stripped.lstrip('•-').strip())
                    elif in_requirements and line_stripped:
                        req_lines.append('• ' + line_stripped)
                
                if req_lines:
                    return '\n'.join(req_lines)
        
        # Priority 2: Try structured sections from docstring (new format)
        sections = self.parse_structured_sections()
        if 'Input Requirement' in sections:
            req_text = sections['Input Requirement']
            # Extract bullet points and join multi-line requirements
            req_lines = []
            current_req = []
            
            for line in req_text.split('\n'):
                line = line.strip()
                if (line.startswith('•') or line.startswith('-')) and current_req:
                    # Save previous requirement as single sentence
                    req_sentence = self.join_multiline_to_sentence('\n'.join(current_req))
                    req_lines.append('• ' + req_sentence.lstrip('•-').strip())
                    current_req = [line.lstrip('•-').strip()]
                elif line.startswith('•') or line.startswith('-'):
                    # Start new requirement
                    current_req = [line.lstrip('•-').strip()]
                elif line and current_req:
                    # Continue current requirement
                    current_req.append(line)
                elif line and not current_req:
                    # Standalone line
                    req_lines.append('• ' + line)
            
            # Add last requirement
            if current_req:
                req_sentence = self.join_multiline_to_sentence('\n'.join(current_req))
                req_lines.append('• ' + req_sentence.lstrip('•-').strip())
            
            if req_lines:
                return '\n'.join(req_lines)  # All requirements with newlines
            return '• ' + req_text  # Return full text with bullet
        
        # Try old format
        content = self.extract_docstring() or self.extract_markdown_purpose()
        
        if not content:
            return "N/A"
        
        lines = content.split('\n')
        in_requirements = False
        req_lines = []
        
        for line in lines:
            line = line.strip()
            
            # Look for requirement/prerequisite sections
            if any(keyword in line.lower() for keyword in ['requirement', 'prerequisite', 'prepare', 'before']):
                in_requirements = True
                continue
            elif in_requirements:
                if line.startswith('###') or line.startswith('---') or line.startswith('##'):
                    break
                elif line and (line.startswith('-') or line.startswith('•')):
                    req_lines.append('• ' + line.lstrip('-•').strip())
        
        if req_lines:
            return '\n'.join(req_lines)  # All requirements with newlines
        
        # Fallback
        file_refs = self.extract_file_references()
        if file_refs['inputs']:
            return 'See Input Files'
        
        return "N/A"
    
    def detect_development_stage(self) -> str:
        """Detect development stage based on script content and metadata."""
        content_lower = self.content.lower()
        
        # Check for development indicators
        if 'todo' in content_lower or 'fixme' in content_lower or 'wip' in content_lower:
            return 'Development'
        
        # Check for test/demo scripts
        if 'test' in self.file_path.name.lower() or 'demo' in self.file_path.name.lower():
            return 'Testing'
        
        # Check for version in docstring
        docstring = self.extract_docstring()
        if docstring and any(keyword in docstring.lower() for keyword in ['beta', 'alpha', 'draft']):
            return 'Development'
        
        # Check for extensive documentation (indicates production)
        if len(docstring) > 500 or len(self.extract_markdown_purpose()) > 500:
            return 'Production'
        
        # Default to Production for main tools
        if self.file_path.name.startswith(('0', '1')) and self.file_path.name[1].isdigit():
            return 'Production'
        
        return 'Stable'
    
    def extract_imports(self) -> List[str]:
        """Extract all imports from the script, including load_external_libs calls."""
        imports = []
        
        if self.ast_tree:
            for node in ast.walk(self.ast_tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        # Get the full import name
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        # Get the module name for 'from X import Y'
                        imports.append(node.module)
        
        # Extract load_external_libs calls for DCMvn modules
        dcmvn_modules = self.extract_load_external_libs_calls()
        imports.extend(dcmvn_modules)
        
        # Remove duplicates and sort
        unique_imports = sorted(list(set(imports)))
        
        return unique_imports
    
    def extract_load_external_libs_calls(self) -> List[str]:
        """
        Extract DCMvn module paths from load_external_libs() function calls.
        
        Detects patterns like:
        - load_external_libs("DCMvn.purepy.io.selectinput")
        - saveoutput_module = load_external_libs("DCMvn.purepy.io.saveoutput")
        
        Returns:
            List of DCMvn module paths
        """
        dcmvn_modules = []
        
        if not self.ast_tree:
            return dcmvn_modules
        
        for node in ast.walk(self.ast_tree):
            # Look for function calls
            if isinstance(node, ast.Call):
                # Check if function name is 'load_external_libs'
                func_name = None
                if isinstance(node.func, ast.Name):
                    func_name = node.func.id
                elif isinstance(node.func, ast.Attribute):
                    func_name = node.func.attr
                
                if func_name == 'load_external_libs':
                    # Extract the first argument (module path string)
                    if node.args and len(node.args) > 0:
                        arg = node.args[0]
                        if isinstance(arg, ast.Str):  # Python 2.7 / IronPython
                            dcmvn_modules.append(arg.s)
                        elif isinstance(arg, ast.Constant):  # Python 3.8+
                            if isinstance(arg.value, str):
                                dcmvn_modules.append(arg.value)
        
        return dcmvn_modules
    
    def extract_file_references(self) -> Dict[str, List[str]]:
        """Extract input/output file references from docstring."""
        inputs = []
        outputs = []
        
        # Priority 1: Check bundle.yaml first
        if self.bundle_yaml:
            tooltip = self._get_tooltip_text()
            if tooltip:
                lines = tooltip.split('\n')
                in_input = False
                in_output = False
                
                for line in lines:
                    line_stripped = line.strip()
                    
                    # Detect sections
                    if 'input files:' in line_stripped.lower():
                        in_input = True
                        in_output = False
                        continue
                    elif 'output files:' in line_stripped.lower():
                        in_output = True
                        in_input = False
                        continue
                    elif any(marker in line_stripped for marker in ['Features:', 'How-to:', 'Last update:', '__________']):
                        in_input = False
                        in_output = False
                    
                    # Extract items
                    if in_input and (line_stripped.startswith('-') or line_stripped.startswith('•')):
                        inputs.append('• ' + line_stripped.lstrip('•-').strip())
                    elif in_input and line_stripped:
                        inputs.append('• ' + line_stripped)
                    elif in_output and (line_stripped.startswith('-') or line_stripped.startswith('•')):
                        outputs.append('• ' + line_stripped.lstrip('•-').strip())
                    elif in_output and line_stripped:
                        outputs.append('• ' + line_stripped)
                
                # Return if found anything in bundle.yaml
                if inputs or outputs:
                    return {'inputs': inputs, 'outputs': outputs}
        
        # Priority 2: Try structured sections from docstring (new format)
        sections = self.parse_structured_sections()
        
        if 'Input Files' in sections:
            input_text = sections['Input Files']
            current_input = []
            
            for line in input_text.split('\n'):
                line = line.strip()
                if (line.startswith('•') or line.startswith('-')) and current_input:
                    # Save previous input as single sentence
                    input_sentence = self.join_multiline_to_sentence('\n'.join(current_input))
                    inputs.append('• ' + input_sentence.lstrip('•-').strip())
                    current_input = [line.lstrip('•-').strip()]
                elif line.startswith('•') or line.startswith('-'):
                    # Start new input
                    current_input = [line.lstrip('•-').strip()]
                elif line and current_input:
                    # Continue current input
                    current_input.append(line)
                elif line and not current_input:
                    # Standalone line
                    inputs.append('• ' + line)
            
            # Add last input
            if current_input:
                input_sentence = self.join_multiline_to_sentence('\n'.join(current_input))
                inputs.append('• ' + input_sentence.lstrip('•-').strip())
        
        if 'Output Files' in sections:
            output_text = sections['Output Files']
            current_output = []
            
            for line in output_text.split('\n'):
                line = line.strip()
                if (line.startswith('•') or line.startswith('-')) and current_output:
                    # Save previous output as single sentence
                    output_sentence = self.join_multiline_to_sentence('\n'.join(current_output))
                    outputs.append('• ' + output_sentence.lstrip('•-').strip())
                    current_output = [line.lstrip('•-').strip()]
                elif line.startswith('•') or line.startswith('-'):
                    # Start new output
                    current_output = [line.lstrip('•-').strip()]
                elif line and current_output:
                    # Continue current output
                    current_output.append(line)
                elif line and not current_output:
                    # Standalone line
                    outputs.append('• ' + line)
            
            # Add last output
            if current_output:
                output_sentence = self.join_multiline_to_sentence('\n'.join(current_output))
                outputs.append('• ' + output_sentence.lstrip('•-').strip())
        
        # If we got results from structured sections, return them
        if inputs or outputs:
            return {'inputs': inputs, 'outputs': outputs}  # Return all items
        
        # Try old format
        content = self.extract_docstring() or self.extract_markdown_purpose()
        
        if content:
            lines = content.split('\n')
            in_input = False
            in_output = False
            
            for line in lines:
                line = line.strip()
                
                if 'input' in line.lower() and ('file' in line.lower() or 'data' in line.lower()):
                    in_input = True
                    in_output = False
                    continue
                elif 'output' in line.lower():
                    in_output = True
                    in_input = False
                    continue
                elif line.startswith('###') or line.startswith('---'):
                    in_input = False
                    in_output = False
                
                if in_input and (line.startswith('-') or line.startswith('•')):
                    inputs.append('• ' + line.lstrip('-•').strip())
                elif in_output and (line.startswith('-') or line.startswith('•')):
                    outputs.append('• ' + line.lstrip('-•').strip())
        
        return {'inputs': inputs, 'outputs': outputs}  # Return all items
    
    def get_file_info(self) -> Dict[str, Any]:
        """Get file metadata."""
        stats = self.file_path.stat()
        return {
            'size_kb': round(stats.st_size / 1024, 2),
            'modified': datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d'),
            'lines': len(self.lines)
        }
    
    def analyze(self) -> Dict[str, Any]:
        """Perform complete analysis."""
        if not self.read_file():
            return None
        
        # Try to load bundle.yaml first (priority source)
        self.bundle_yaml = self.read_bundle_yaml()
        
        self.parse_ast()
        
        relative_path = self.file_path.relative_to(SOURCE_DIR)
        file_refs = self.extract_file_references()
        features = self.extract_features()
        
        # Format dependencies with bullet points
        imports = self.extract_imports()
        dependencies = '\n'.join(['• ' + imp for imp in imports]) if imports else 'N/A'
        
        return {
            'Script Name': relative_path.name,
            'Purpose': self.extract_purpose(),
            'Features': '\n'.join(features) if features else 'N/A',
            'Dependencies': dependencies,
            'Programming Language': self.detect_programming_language(),
            'Full Path': str(self.file_path),
            'Input Files': '\n'.join(file_refs['inputs']) if file_refs['inputs'] else 'N/A',
            'Input Requirement': self.extract_input_requirements(),
            'Output Files': '\n'.join(file_refs['outputs']) if file_refs['outputs'] else 'N/A',
            'Usage': self.extract_usage() or 'N/A',
            'Status': 'Done',
            'Applied Project': 'Multi-Projects',
            'Category': self._categorize_script(relative_path),
            'Development Stage': self.detect_development_stage(),
            'Author': self.extract_author()
        }
    
    def _categorize_script(self, path: Path) -> str:
        """Categorize script by location and name."""
        path_str = str(path).lower()
        
        if 'bcfextract' in path_str:
            return 'BCF Processing'
        elif 'lib' in path_str:
            return 'Utility Library'
        elif 'xlwings_util' in path_str:
            return 'Excel Utility'
        elif 'validation' in path.name.lower():
            return 'Validation'
        elif 'merge' in path.name.lower():
            return 'Data Merge'
        elif 'convert' in path.name.lower():
            return 'Conversion'
        elif path.name.startswith('0') or path.name.startswith('1'):
            return 'Main Tool'
        else:
            return 'Other'


def scan_python_files(base_dir: Path) -> List[Path]:
    """Recursively scan for Python files."""
    python_files = []
    
    for path in base_dir.rglob('*.py'):
        # Check if in excluded directory
        if any(excluded in path.parts for excluded in EXCLUDED_DIRS):
            continue
        
        # Check if excluded file
        if path.name in EXCLUDED_FILES:
            continue
        
        python_files.append(path)
    
    return sorted(python_files)


def generate_report(data: List[Dict[str, Any]], output_path: Path):
    """Generate Excel report with formatting."""
    logger.info("Creating Excel report...")
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    # Reorder columns according to user requirements (with Features added)
    column_order = [
        'Script Name', 'Purpose', 'Features', 'Dependencies', 'Programming Language',
        'Full Path', 'Input Files', 'Input Requirement', 'Output Files',
        'Usage', 'Status', 'Applied Project', 'Category',
        'Development Stage', 'Author'
    ]
    df = df[column_order]
    
    # Sort by Category then Script Name
    df = df.sort_values(['Category', 'Script Name']).reset_index(drop=True)
    
    # Add index column (No.) starting from 1
    df.insert(0, 'No.', range(1, len(df) + 1))
    
    # Remove any 'Column1' if exists (legacy column)
    if 'Column1' in df.columns:
        df = df.drop('Column1', axis=1)
    
    # Save to Excel with xlwings for formatting
    try:
        logger.info(f"Saving to {output_path}...")
        
        # Create Excel file with xlwings
        app = xw.App(visible=False)
        wb = app.books.add()
        ws = wb.sheets[0]
        ws.name = 'Tool Register'
        
        # Write data (without index to avoid Column1)
        ws.range('A1').options(index=False).value = df
        
        # Get actual number of columns after writing
        num_cols = len(df.columns)
        last_col = chr(64 + num_cols)  # Convert to letter (A=65)
        
        # Format header
        header_range = ws.range(f'A1:{last_col}1')
        header_range.api.Font.Bold = True
        header_range.api.Font.Size = 11
        header_range.api.Interior.Color = 0x44546A  # Dark blue
        header_range.api.Font.Color = 0xFFFFFF  # White
        header_range.api.VerticalAlignment = -4108  # xlCenter
        header_range.api.HorizontalAlignment = -4108  # xlCenter
        
        # Apply borders to all data
        data_range = ws.range(f'A1:{last_col}{len(df)+1}')
        data_range.api.Borders.LineStyle = 1
        data_range.api.Borders.Weight = 2
        
        # Wrap text for description columns
        for col in ['C', 'D', 'H', 'I', 'J', 'K']:  # Purpose, Features, Input Files, Input Req, Output Files, Usage
            ws.range(f'{col}2:{col}{len(df)+1}').api.WrapText = True
        
        # Set column widths (16 columns)
        ws.range('A:A').column_width = 8   # No.
        ws.range('B:B').column_width = 35  # Script Name
        ws.range('C:C').column_width = 45  # Purpose
        ws.range('D:D').column_width = 45  # Features
        ws.range('E:E').column_width = 25  # Dependencies
        ws.range('F:F').column_width = 15  # Programming Language
        ws.range('G:G').column_width = 60  # Full Path
        ws.range('H:H').column_width = 35  # Input Files
        ws.range('I:I').column_width = 35  # Input Requirement
        ws.range('J:J').column_width = 35  # Output Files
        ws.range('K:K').column_width = 40  # Usage
        ws.range('L:L').column_width = 10  # Status
        ws.range('M:M').column_width = 20  # Applied Project
        ws.range('N:N').column_width = 15  # Category
        ws.range('O:O').column_width = 15  # Development Stage
        ws.range('P:P').column_width = 12  # Author
        
        # Auto-fit columns after setting widths (for fine-tuning)
        ws.autofit('c')
        
        # Freeze header row
        ws.range('A2').api.Select()
        app.api.ActiveWindow.FreezePanes = True
        
        # Create table with correct range
        table_range = ws.range(f'A1:{last_col}{len(df)+1}')
        table = ws.api.ListObjects.Add(1, table_range.api, None, 1)
        table.Name = 'ToolRegisterTable'
        table.TableStyle = 'TableStyleMedium2'
        
        # Add summary sheet
        summary_ws = wb.sheets.add('Summary', after=ws)
        
        # Write summary data row by row
        row = 1
        summary_ws.range(f'A{row}').value = 'Tool Register Summary'
        summary_ws.range(f'A{row}').api.Font.Bold = True
        summary_ws.range(f'A{row}').api.Font.Size = 14
        
        row += 2
        summary_ws.range(f'A{row}').value = 'Total Scripts'
        summary_ws.range(f'B{row}').value = len(df)
        
        row += 2
        summary_ws.range(f'A{row}').value = 'By Category:'
        summary_ws.range(f'A{row}').api.Font.Bold = True
        
        category_counts = df['Category'].value_counts().to_dict()
        for cat, count in sorted(category_counts.items()):
            row += 1
            summary_ws.range(f'A{row}').value = f'  {cat}'
            summary_ws.range(f'B{row}').value = count
        
        row += 2
        summary_ws.range(f'A{row}').value = 'By Development Stage:'
        summary_ws.range(f'A{row}').api.Font.Bold = True
        
        stage_counts = df['Development Stage'].value_counts().to_dict()
        for stage, count in sorted(stage_counts.items()):
            row += 1
            summary_ws.range(f'A{row}').value = f'  {stage}'
            summary_ws.range(f'B{row}').value = count
        
        row += 2
        summary_ws.range(f'A{row}').value = 'By Programming Language:'
        summary_ws.range(f'A{row}').api.Font.Bold = True
        
        lang_counts = df['Programming Language'].value_counts().to_dict()
        for lang, count in sorted(lang_counts.items()):
            row += 1
            summary_ws.range(f'A{row}').value = f'  {lang}'
            summary_ws.range(f'B{row}').value = count
        
        row += 2
        summary_ws.range(f'A{row}').value = 'Generated'
        summary_ws.range(f'B{row}').value = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        summary_ws.autofit('c')
        
        # Save and close
        wb.save(str(output_path))
        wb.close()
        app.quit()
        
        logger.info(f"✓ Report generated successfully: {output_path}")
        
    except Exception as e:
        logger.error(f"Error generating report: {e}")
        # Fallback to simple pandas export
        df.to_excel(output_path, index=False, sheet_name='Tool Register')
        logger.info(f"✓ Basic report saved: {output_path}")


def main():
    """Main execution function."""
    start_time = datetime.now()
    
    logger.info("="*60)
    logger.info("Tool Register Generator")
    logger.info("="*60)
    logger.info(f"Workspace Root: {WORKSPACE_ROOT}")
    logger.info(f"Source Directory: {SOURCE_DIR}")
    
    # Check if source directory exists
    if not SOURCE_DIR.exists():
        logger.error(f"Source directory not found: {SOURCE_DIR}")
        logger.error("Please ensure the 'source' folder exists in the workspace root.")
        return
    
    # Scan for Python files
    logger.info(f"Scanning {SOURCE_DIR} for Python files...")
    python_files = scan_python_files(SOURCE_DIR)
    logger.info(f"Found {len(python_files)} Python files to analyze")
    
    # Analyze each file
    results = []
    for i, file_path in enumerate(python_files, 1):
        logger.info(f"[{i}/{len(python_files)}] Analyzing {file_path.name}...")
        
        analyzer = ScriptAnalyzer(file_path)
        result = analyzer.analyze()
        
        if result:
            results.append(result)
        else:
            logger.warning(f"  ⚠ Failed to analyze {file_path.name}")
    
    logger.info(f"Successfully analyzed {len(results)}/{len(python_files)} files")
    
    # Generate report
    if results:
        # Save output to workspace root
        output_path = WORKSPACE_ROOT / f"Tool Register - Generated {datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
        generate_report(results, output_path)
        
        # Calculate runtime
        elapsed = (datetime.now() - start_time).total_seconds()
        minutes = int(elapsed // 60)
        seconds = int(elapsed % 60)
        
        logger.info("="*60)
        logger.info(f"✓ Completed in {minutes}m{seconds}s")
        logger.info(f"✓ Total scripts analyzed: {len(results)}")
        logger.info(f"✓ Report saved to: {output_path.name}")
        logger.info("="*60)
    else:
        logger.error("No results to generate report!")


if __name__ == '__main__':
    main()

