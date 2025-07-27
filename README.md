# 🧠 Obsidian to Confluence Sync (`obs2confluence`)

**Sync your Obsidian Markdown notes to Confluence Cloud automatically.**  
Supports tag-based filtering, directory scoping, page ID caching, and full automation via Python.

---
## 🚀 Features

- ✅ Sync Obsidian `.md` files to Confluence Cloud
- ✅ Tag-based filtering (`tags: [confluence-sync]`)
- ✅ Directory scope control (`Projects/`, `Weekly/`, etc.)
- ✅ Confluence page updates via `page_id` caching
- ✅ Markdown to Confluence-compatible HTML conversion
- ✅ Configurable via `config.yaml`
- ✅ Dry-run support and CLI integration
- ✅ Auto hash-check to avoid redundant uploads
---
## 🗂️ Project Structure

```pgsql
obs2confluence/
├── main.py                # Entry point
├── config.yaml            # User-defined configuration
├── sync_state.json        # Sync metadata: hash + page_id
├── Makefile               # Automation commands (make sync / clean / install)
├── sync/
│   ├── sync_runner.py     # Main sync logic
│   ├── file_scanner.py    # Markdown file collector
│   ├── frontmatter.py     # YAML tag extractor
│   ├── hash_util.py       # File hashing
│   └── state_tracker.py   # Load/save sync state
├── confluence/
│   └── api.py             # Confluence API wrapper
```
---
## ⚙️ Requirements

- Python 3.7+
    
- Dependencies:
    ```
    pip install -r requirements.txt
    ```

---
## 🛠️ Usage

### Step 1: Prepare `config.yaml`

```yaml
obsidian_path: /path/to/your/vault

filter:
  tag: confluence-sync
  include_dirs:
    - "Projects"
    - "Weekly"

confluence:
  url: https://yourdomain.atlassian.net/wiki
  username: your@email.com
  api_token: your_confluence_api_token
  space_key: DOCS
  parent_page_id: 12345678

```
### Step 2: Add `confluence-sync` tag in your Obsidian notes
```markdown
--- tags: [confluence-sync] --- # My Synced Note
```
### Step 3: Run sync

```bash
python main.py
```
Or with `make`:
```bash
make sync
```

---
## ✅ Example Output
```yaml
🔍 Scanning vault: /Users/me/ObsidianVault
📄 Processing: Projects/Meeting Notes.md
✅ Synced: Meeting Notes
🎉 All tasks complete.
```

---

## 📦 Optional Commands
```bash
make install   # install dependencies
make clean     # remove __pycache__ and state
make lint      # run flake8
make zip       # package code into obs2conf.zip

```

---
## 📌 Notes

- This project only supports **Obsidian → Confluence** (one-way sync) for now
    
- Only notes with YAML frontmatter tag `confluence-sync` are uploaded
    
- All pages are created under the specified parent page in Confluence
    
- Sync state is stored in `sync_state.json` (MD5 + page_id)
    
---
## 📘 Future Plans

- 🔄 Bidirectional sync (Confluence → Obsidian)
    
- 🖼 Image / attachment upload
    
- 🔗 Obsidian `[[wikilink]]` support
    
- 🧩 Convert into native Obsidian plugin (TypeScript shell + CLI backend)
    

---

## 📝 License

MIT License