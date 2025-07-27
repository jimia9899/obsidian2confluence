# sync/sync_runner.py

import os
from sync.file_scanner import scan_markdown_files
from sync.frontmatter import extract_tags_and_content
from sync.hash_util import hash_file
from sync.state_tracker import load_state, save_state
from confluence.api import get_confluence_client, create_or_update_page

import yaml

CONFIG_PATH = "config.yaml"
STATE_PATH = "sync_state.json"

import yaml

def load_config():
    config_file = os.environ.get("CONFIG_FILE", "config/default.yml")
    with open(config_file, "r") as f:
        config = yaml.safe_load(f)
        return config

def run_sync():
    config = load_config()
    vault_path = config["obsidian_path"]
    tag_filter = config["filter"].get("tag")
    include_dirs = config["filter"].get("include_dirs", [])
    conf_cfg = config["confluence"]

    state = load_state(STATE_PATH)
    confluence = get_confluence_client(conf_cfg)

    print(f"🔍 扫描目录: {vault_path}")
    files = scan_markdown_files(vault_path, include_dirs)

    for file_path in files:
        try:
            tags, content_md = extract_tags_and_content(file_path)
        except Exception as e:
            print(f"⚠️ 读取失败: {file_path} -> {e}")
            continue

        if tag_filter and tag_filter not in tags:
            print(f"🚫 跳过: {file_path}（不含 tag {tag_filter}）")
            continue

        file_hash = hash_file(file_path)
        entry = state.get(file_path)

        if entry and entry.get("hash") == file_hash:
            print(f"⏩ 已同步: {file_path}")
            continue

        title = os.path.splitext(os.path.basename(file_path))[0]
        page_id = entry.get("page_id") if entry else None

        new_page_id = create_or_update_page(
            confluence=confluence,
            title=title,
            content_md=content_md,
            config=conf_cfg,
            page_id=page_id
        )

        state[file_path] = {
            "hash": file_hash,
            "page_id": new_page_id
        }

        print(f"✅ 已同步: {title}")

    save_state(STATE_PATH, state)
    print("🎉 所有任务完成。")
