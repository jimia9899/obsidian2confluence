# sync/file_scanner.py

import os

def scan_markdown_files(vault_path, include_dirs):
    result = []
    vault_path = os.path.abspath(vault_path)
    include_paths = [os.path.join(vault_path, d) for d in include_dirs] if include_dirs else [vault_path]

    for base in include_paths:
        for root, _, files in os.walk(base):
            for file in files:
                if file.endswith(".md"):
                    full_path = os.path.join(root, file)
                    result.append(full_path)

    return result
