#!/usr/bin/env python3
"""
Download a HuggingFace model using hf-mirror.com (this machine).

Usage:
    python3 hf_download.py BAAI/bge-m3
    python3 hf_download.py BAAI/bge-m3 --files "config.json|pytorch_model.bin"

NOTE: For files >500MB, use terminal's native `background: true` mode instead
      (terminal `&` operator is blocked). This script is for small/medium files.
"""
import os
import sys
import urllib.request
import json

# Default model
repo_id = sys.argv[1] if len(sys.argv) > 1 else "BAAI/bge-m3"

# Parse --files flag
filter_files = None
if "--files" in sys.argv:
    idx = sys.argv.index("--files")
    filter_files = sys.argv[idx + 1].split("|")
    sys.argv.pop(idx)
    sys.argv.pop(idx)

HF_MIRROR = "https://hf-mirror.com"

def get_model_files(repo_id):
    """Get file list from hf-mirror API."""
    url = f"{HF_MIRROR}/api/models/{repo_id}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())

def download_file(url, dest):
    """Download with curl (supports resume)."""
    import subprocess
    result = subprocess.run(
        ["curl", "-L", "-C", "-", "-o", dest, url],
        capture_output=True, text=True, timeout=300
    )
    return result.returncode == 0

model_info = get_model_files(repo_id)
siblings = model_info.get("siblings", [])
print(f"Model: {repo_id}")
print(f"Files: {len(siblings)}")
print(f"Total size: {model_info.get('lastModified', 'unknown')}")

cache_dir = os.path.expanduser(f"~/.cache/huggingface/hub/models--{repo_id.replace('/', '--')}/snapshots/main/")
os.makedirs(cache_dir, exist_ok=True)

for f in siblings:
    fname = f.get("rfilename", "")
    if filter_files and not any(ff in fname for ff in filter_files):
        continue
    
    size = f.get("size", 0)
    size_str = f"{size/1024**2:.1f}MB" if size > 1024**2 else f"{size/1024:.1f}KB"
    print(f"  Downloading {fname} ({size_str})...")
    
    url = f"{HF_MIRROR}/{repo_id}/resolve/main/{fname}"
    dest = os.path.join(cache_dir, fname)
    
    if size > 500 * 1024 * 1024:
        print(f"    [SKIP — too large for script, use terminal background mode]")
        print(f"    curl -L -C - -o '{dest}' '{url}'")
        continue
    
    ok = download_file(url, dest)
    if ok:
        print(f"    [OK]")
    else:
        print(f"    [FAILED]")
