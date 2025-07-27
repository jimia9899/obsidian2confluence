# sync/state_tracker.py

import json
import os

def load_state(path):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ 无法读取状态文件 {path}: {e}")
        return {}

def save_state(path, state):
    try:
        with open(path, "w") as f:
            json.dump(state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"❌ 无法保存状态文件 {path}: {e}")
