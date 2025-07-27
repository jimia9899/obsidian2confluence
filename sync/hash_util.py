# sync/hash_util.py

import hashlib

def hash_file(path):
    """返回文件内容的 MD5 hash 字串"""
    with open(path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()
