# /graphify-to-wiki

Sync graphify knowledge graph output into LLM Wiki using Obsidian-flavored markdown.

## Execution

1. **Read inputs:**
   - `graphify-out/graph.json` — full graph data
   - `graphify-out/GRAPH_REPORT.md` — curated highlights
   - `wiki/index.md` — existing pages list
   - `schema.md` — page type rules

2. **Parse & classify nodes:**
   - Nodes with ≥3 edges, confidence EXTRACTED/INFERRED
   - Skip code functions (main, slugify, etc.)
   - Classify: named tool/repo → entity | abstract idea → concept | cross-community bridge → synthesis

3. **Deduplicate:**
   - Normalize node labels to kebab-case slugs
   - Match against existing wiki/ pages
   - Existing → update `related:` frontmatter only
   - New → create full page

4. **Generate pages using Obsidian format:**
   - YAML frontmatter per schema.md
   - `[[wikilinks]]` for all cross-references
   - `> [!info]` callouts for metadata
   - Tags in frontmatter array

5. **Update wiki/index.md and wiki/log.md**

6. **Report:** List created/updated pages, dangling links, knowledge gaps

## Obsidian Skills Reference

Use formatting from: `.claude/skills/obsidian-skills/skills/obsidian-markdown/SKILL.md`

- Wikilinks: `[[page-slug]]` or `[[page-slug|Display Name]]`
- Callouts: `> [!info]`, `> [!tip]`, `> [!warning]`, `> [!abstract]`
- Frontmatter: Full YAML with type, title, tags, related, created, updated
- Block IDs: `^block-id` for linkable paragraphs

## Flags

- `--dry-run` — Preview without writing
- `--entities-only` — Only god nodes → entities
- `--insights-only` — Only surprising connections → synthesis
- `--gaps` — Only knowledge gaps → query pages
- `--update` — Only update existing pages with new connections
- `--include-ambiguous` — Include AMBIGUOUS confidence nodes

## After Running

```bash
/graphify . --update   # Re-index wiki to incorporate new pages (feedback loop)
```
