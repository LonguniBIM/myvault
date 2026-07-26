# Test Scenarios: /graphify-to-wiki

## Test 1 — Dry Run (No Writes)

**Input:** `/graphify-to-wiki --dry-run`  
**Expected:**
- Reads `graphify-out/graph.json` (114 nodes, 149 edges)
- Filters to `file_type: "document"` nodes only
- Identifies which nodes already exist in `wiki/` (by source_file match)
- Reports: "Would create X new pages, update Y existing pages"
- Does NOT write any files

**Validation:** No new files in `wiki/`, no changes to `wiki/index.md`

---

## Test 2 — Entity Deduplication

**Input:** `/graphify-to-wiki --entities-only`  
**Expected:**
- Node `"Obsidian Skills (kepano/obsidian-skills)"` has `source_file: "wiki/entities/obsidian-skills.md"`
- Since `wiki/entities/obsidian-skills.md` already exists → UPDATE only (add new `related:` connections)
- Does NOT create a duplicate `wiki/entities/obsidian-skills-2.md`

**Validation:** `wiki/entities/obsidian-skills.md` has updated `related:` field, no new file created

---

## Test 3 — New Entity Creation

**Input:** A node like `"Karpathy-inspired four coding principles"` from hyperedge that doesn't match any existing wiki page slug  
**Expected:**
- Creates `wiki/concepts/karpathy-coding-principles.md`
- Frontmatter includes: type, title, tags, related, created, updated, graphify_node_id
- Body uses `> [!info]` callout for metadata
- Cross-references use `[[wikilinks]]`
- Added to `wiki/index.md` under Concepts section

**Validation:** File exists with valid YAML frontmatter and wikilinks

---

## Test 4 — Surprising Connections → Synthesis

**Input:** `/graphify-to-wiki --insights-only`  
**Expected for:** "Two-step ingest: raw capture to wiki processing" ↔ "Seven-step ingest workflow"
- Creates `wiki/synthesis/two-step-vs-seven-step-ingest.md`
- Type: synthesis
- Callout: `> [!tip] Surprising Connection`
- Links both source nodes via `[[wikilinks]]`
- Confidence and source file noted

**Validation:** Synthesis page exists with correct callout type and both links

---

## Test 5 — Code Nodes Filtered Out

**Input:** `/graphify-to-wiki`  
**Expected:**
- Node `"main()"` (file_type: "code", 15 edges, highest-connected) is SKIPPED
- Node `"slugify()"` (file_type: "code") is SKIPPED
- Node `"file_sha256()"` (file_type: "code") is SKIPPED
- All `file_type: "rationale"` nodes are SKIPPED
- Only `file_type: "document"` nodes are processed

**Validation:** No wiki pages created for code functions or docstring rationales

---

## Test 6 — Index and Log Update

**Input:** `/graphify-to-wiki` (creates 3 new pages)  
**Expected:**
- `wiki/index.md` has 3 new `- [[slug]] — description` entries under correct sections
- `wiki/log.md` has new entry with today's date and `[graphify-to-wiki]` tag
- Entries are properly formatted with wikilinks

**Validation:** Both files contain new entries matching created pages

---

## Test 7 — Obsidian Format Compliance

**Input:** Any generated page  
**Expected:**
- YAML frontmatter delimited by `---`
- All internal links use `[[wikilink]]` syntax (not `[text](url)`)
- Callouts use `> [!type]` syntax
- Tags are in frontmatter `tags: []` array (not inline `#tag`)
- No bare URLs for internal content

**Validation:** Page renders correctly in Obsidian Reading View

---

## Test 8 — Knowledge Gaps → Queries

**Input:** `/graphify-to-wiki --gaps`  
**Expected:**
- GRAPH_REPORT mentions "63 isolated nodes" as knowledge gaps
- Creates query pages for meaningful gaps (not code function gaps)
- Format: `wiki/queries/gap-<descriptive-slug>.md`
- Type: query
- Lists the isolated nodes and suggests investigation

**Validation:** Query pages exist with proper type and links

---

## Test 9 — Idempotency

**Input:** Run `/graphify-to-wiki` twice with same graph.json  
**Expected:**
- First run: creates pages, updates index/log
- Second run: "No new pages to create. All graph nodes already synced."
- Does NOT duplicate entries in index.md
- Does NOT create duplicate log entries

**Validation:** File counts and index.md line count unchanged after second run

---

## Test 10 — Feedback Loop

**Input:** Full workflow cycle  
**Steps:**
1. `/graphify .` → builds graph
2. `/graphify-to-wiki` → syncs to wiki (creates new pages)
3. `/graphify . --update` → re-indexes wiki including new pages
4. Graph should now show MORE connections (new pages link back to old ones)

**Validation:** `graph.json` node count increases after step 3, edge count grows
