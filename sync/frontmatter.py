# sync/frontmatter.py

import yaml

def extract_tags_and_content(path):
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        return [], ""

    if lines[0].strip() != "---":
        return [], "".join(lines)

    i = 1
    while i < len(lines) and lines[i].strip() != "---":
        i += 1

    if i >= len(lines):
        return [], "".join(lines)

    frontmatter = yaml.safe_load("".join(lines[1:i]))
    tags = frontmatter.get("tags", [])
    content = "".join(lines[i+1:])
    return tags, content
