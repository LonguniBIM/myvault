# Graph Report - D:\wiki\AI Research  (2026-04-30)

## Corpus Check
- 1 files · ~23,563 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 114 nodes · 149 edges · 19 communities detected
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.79)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 14|Community 14]]
- [[_COMMUNITY_Community 15|Community 15]]
- [[_COMMUNITY_Community 16|Community 16]]
- [[_COMMUNITY_Community 17|Community 17]]
- [[_COMMUNITY_Community 18|Community 18]]

## God Nodes (most connected - your core abstractions)
1. `main()` - 15 edges
2. `Comparison document: Agent Skills for LLM Coding Agents` - 9 edges
3. `Andrej Karpathy Skills (CLAUDE.md guidelines)` - 9 edges
4. `LLM Wiki (nashsu/llm_wiki desktop app)` - 9 edges
5. `Obsidian Skills (kepano/obsidian-skills)` - 9 edges
6. `Karpathy LLM Wiki Pattern methodology` - 8 edges
7. `GitHub Repo Knowledge Base (project purpose)` - 7 edges
8. `graphify â€” GraphRAG knowledge graph skill (safishamsi/graphify)` - 7 edges
9. `LLM Agent Skills concept (portable skill files)` - 7 edges
10. `LLM Coding Guidelines concept` - 7 edges

## Surprising Connections (you probably didn't know these)
- `Two-step ingest: raw capture to wiki processing` --semantically_similar_to--> `Seven-step ingest workflow (read, discuss, pages, links, index, log)`  [INFERRED] [semantically similar]
  purpose.md → Sample.md
- `Two-step ingest: raw capture to wiki processing` --semantically_similar_to--> `Six-step workflow: capture through query`  [INFERRED] [semantically similar]
  purpose.md → wiki/overview.md
- `Queries answered by traversing KB index to entity/comparison pages` --conceptually_related_to--> `Six-step workflow: capture through query`  [INFERRED]
  purpose.md → wiki/overview.md
- `Based on Andrej Karpathy LLM Wiki pattern` --references--> `Karpathy LLM Wiki Pattern methodology`  [EXTRACTED]
  Sample.md → wiki/concepts/karpathy-llm-wiki-pattern.md
- `Contradiction handling workflow (note, query, link, synthesis)` --conceptually_related_to--> `LLM-Powered Knowledge Base concept`  [INFERRED]
  schema.md → wiki/concepts/llm-knowledge-base.md

## Hyperedges (group relationships)
- **Three repos compared for agent skill configuration** — index_entity_andrej_karpathy_skills, index_entity_obsidian_skills, index_entity_graphify [EXTRACTED 1.00]
- **Implementations subsection ties pattern to llm-wiki and andrej-karpathy-skills** — karpathy_llm_wiki_pattern_concept, index_entity_llm_wiki, index_entity_andrej_karpathy_skills [EXTRACTED 1.00]
- **Knowledge-base concept category with llm-wiki and graphify exemplars** — llm_knowledge_base_concept, index_entity_llm_wiki, index_entity_graphify [EXTRACTED 1.00]
- **Karpathy-inspired four coding principles** — andrej_karpathy_skills_principle_think_before_coding, andrej_karpathy_skills_principle_simplicity_first, andrej_karpathy_skills_principle_surgical_changes, andrej_karpathy_skills_principle_goal_driven_execution, andrej_karpathy_skills_karpathy_skills_repo [EXTRACTED 1.00]
- **Five Obsidian-format agent skills bundle** — obsidian_skills_skill_obsidian_markdown, obsidian_skills_skill_obsidian_bases, obsidian_skills_skill_json_canvas, obsidian_skills_skill_obsidian_cli, obsidian_skills_skill_defuddle, obsidian_skills_obsidian_skills_collection [EXTRACTED 1.00]
- **Agent augmentation: behavioral guidelines vs wiki app vs structural graph skill** — andrej_karpathy_skills_karpathy_skills_repo, llm_wiki_llm_wiki_app, graphify_graphify_tool, obsidian_skills_obsidian_skills_collection [INFERRED 0.78]

## Communities

### Community 0 - "Community 0"
Cohesion: 0.16
Nodes (16): Comparison: llm-knowledge-base-tools, graphify â€” GraphRAG knowledge graph skill (safishamsi/graphify), llm-wiki â€” desktop wiki app (nashsu/llm_wiki), Karpathy LLM Wiki Pattern methodology, Principle: Human curates, LLM maintains, Implementations table (llm-wiki vs andrej-karpathy-skills), Three layers: Raw Sources, Wiki, Schema, LLM-Powered Knowledge Base concept (+8 more)

### Community 1 - "Community 1"
Cohesion: 0.21
Nodes (14): Comparison document: Agent Skills for LLM Coding Agents, Feature matrix (behavioral, domain, structural dimensions), Comparison: agent-skills-for-llm-coding, andrej-karpathy-skills â€” Karpathy-style CLAUDE.md guidelines (forrestchang), obsidian-skills â€” Obsidian format agent skills (kepano), Compatible agents and skill formats (Claude Code, Cursor, Codex, etc.), LLM Agent Skills concept (portable skill files), Three types: Behavioral, Domain knowledge, Structural context (+6 more)

### Community 2 - "Community 2"
Cohesion: 0.24
Nodes (11): Overview metrics (repos ingested, entities, comparisons, decisions), Six-step workflow: capture through query, GitHub Repo Knowledge Base (project purpose), Hypothesis: structured KB yields queryable decision-support with pre-analyzed comparisons, Approach inspired by Karpathy LLM Wiki pattern for repo analysis, LLM Wiki Clipper web extension (capture), Queries answered by traversing KB index to entity/comparison pages, Paradox of choice across overlapping GitHub tools (+3 more)

### Community 3 - "Community 3"
Cohesion: 0.25
Nodes (8): Andrej Karpathy Skills (CLAUDE.md guidelines), Goal-Driven Execution, Simplicity First, Surgical Changes, Think Before Coding, Bias toward caution over speed on non-trivial work, LLMs excel at looping until specific goals â€” use success criteria not imperative steps, Source summary: forrestchang/andrej-karpathy-skills

### Community 4 - "Community 4"
Cohesion: 0.29
Nodes (7): main(), Add new source entry to wiki/index.md., Append entry to wiki/log.md., Save manifest to disk., save_manifest(), update_wiki_index(), update_wiki_log()

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (7): GRAPH_REPORT.md, graphify (AI coding assistant skill & knowledge graph tool), GraphRAG (graph topology retrieval), Leiden community detection (graphify), 4-Signal Knowledge Graph, Louvain community detection (LLM Wiki), Source summary: safishamsi/graphify

### Community 6 - "Community 6"
Cohesion: 0.29
Nodes (7): Karpathy LLM Wiki pattern, LLM Wiki (nashsu/llm_wiki desktop app), purpose.md captures why the wiki exists; LLM reads it on ingest/query (distinct from schema.md), Two sequential LLM calls (analysis then generation) for better wiki quality than single-pass, Two-Step Chain-of-Thought Ingest, defuddle skill, Source summary: nashsu/llm_wiki

### Community 7 - "Community 7"
Cohesion: 0.29
Nodes (7): Agent Skills specification, Obsidian Skills (kepano/obsidian-skills), json-canvas skill, obsidian-bases skill, obsidian-cli skill, obsidian-markdown skill, Source summary: kepano/obsidian-skills

### Community 8 - "Community 8"
Cohesion: 0.33
Nodes (6): create_wiki_source_page(), Save transcript as markdown in raw/transcripts/., Create a wiki source page for the transcribed media., Convert text to kebab-case slug safe for filenames., save_transcript(), slugify()

### Community 9 - "Community 9"
Cohesion: 0.33
Nodes (5): load_manifest(), Extract transcripts from video/audio files in raw/ and ingest into the wiki.  Pi, Transcribe a video/audio file using faster-whisper. Returns transcript text., Load processed files manifest (tracks what's already transcribed)., transcribe_file()

### Community 10 - "Community 10"
Cohesion: 0.33
Nodes (6): Based on Andrej Karpathy LLM Wiki pattern, Wiki lint/audit checklist (contradictions, orphans, outdated claims), Sample LLM Wiki (trip to Japan template by Claude), Question answering protocol (index first, synthesize, cite), Raw sources immutable; wiki Claude-maintained, Standard wiki page format (Summary, Sources, Related)

### Community 11 - "Community 11"
Cohesion: 0.5
Nodes (4): file_sha256(), get_new_files(), Compute SHA256 hash of a file for change detection., Filter to only files not yet processed (or changed since last run).

### Community 12 - "Community 12"
Cohesion: 0.5
Nodes (4): Comparison frontmatter (use_case, repos, best_fit, best_fit_reason), GitHub entity frontmatter fields (repo_url, language, stars, use_case), Wiki schema page types (entity, concept, source, query, comparison, etc.), Required YAML frontmatter on all pages

### Community 13 - "Community 13"
Cohesion: 1.0
Nodes (2): derive_title_from_filename(), Extract a human-readable title from the filename.

### Community 14 - "Community 14"
Cohesion: 1.0
Nodes (2): download_youtube_audio(), Download audio from YouTube URL using yt-dlp. Returns path to audio file.

### Community 15 - "Community 15"
Cohesion: 1.0
Nodes (2): Recursively find all video/audio files under base_dir., scan_media_files()

### Community 16 - "Community 16"
Cohesion: 1.0
Nodes (2): format_duration(), Format seconds into XmYs format.

### Community 17 - "Community 17"
Cohesion: 1.0
Nodes (2): Rationale: methodology pages document why not only how, Methodology pages explain why (rationale) not only how

### Community 18 - "Community 18"
Cohesion: 1.0
Nodes (1): Saved Query (empty stub)

## Knowledge Gaps
- **63 isolated node(s):** `Extract transcripts from video/audio files in raw/ and ingest into the wiki.  Pi`, `Convert text to kebab-case slug safe for filenames.`, `Compute SHA256 hash of a file for change detection.`, `Load processed files manifest (tracks what's already transcribed).`, `Save manifest to disk.` (+58 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Community 13`** (2 nodes): `derive_title_from_filename()`, `Extract a human-readable title from the filename.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 14`** (2 nodes): `download_youtube_audio()`, `Download audio from YouTube URL using yt-dlp. Returns path to audio file.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 15`** (2 nodes): `Recursively find all video/audio files under base_dir.`, `scan_media_files()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 16`** (2 nodes): `format_duration()`, `Format seconds into XmYs format.`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 17`** (2 nodes): `Rationale: methodology pages document why not only how`, `Methodology pages explain why (rationale) not only how`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 18`** (1 nodes): `Saved Query (empty stub)`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Karpathy LLM Wiki Pattern methodology` connect `Community 0` to `Community 1`, `Community 2`, `Community 10`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Why does `Comparison document: Agent Skills for LLM Coding Agents` connect `Community 1` to `Community 0`, `Community 2`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `Six-step workflow: capture through query` connect `Community 2` to `Community 0`, `Community 1`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **What connects `Extract transcripts from video/audio files in raw/ and ingest into the wiki.  Pi`, `Convert text to kebab-case slug safe for filenames.`, `Compute SHA256 hash of a file for change detection.` to the rest of the system?**
  _63 weakly-connected nodes found - possible documentation gaps or missing edges._