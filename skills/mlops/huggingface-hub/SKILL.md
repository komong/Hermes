---
name: huggingface-hub
description: "HuggingFace hf CLI: search/download/upload models, datasets."
version: 1.0.0
author: Hugging Face
license: MIT
tags: [huggingface, hf, models, datasets, hub, mlops]
---

# Hugging Face CLI (`hf`) Reference Guide

The `hf` command is the modern command-line interface for interacting with the Hugging Face Hub, providing tools to manage repositories, models, datasets, and Spaces.

## Installation (this machine)

**Do NOT use `curl | bash` to install `hf` CLI** — huggingface.co is blocked from this machine (curl/wget time out). Use pip instead:

```bash
pip install huggingface-hub
# Verify:
python3 -c "from huggingface_hub import hf_hub_download; print('OK')"
```

The `hf` CLI itself may also be blocked. For downloads, use the Python library or hf-mirror.com workaround below.

## Quick Start
* **Help (via pip package):** `python3 -c "from huggingface_hub import hf_hub_download; help(hf_hub_download)"`
* **Authentication:** Set `HF_TOKEN` env var, or pass `--token` flag to Python calls.

---

## Core Commands

## Core Operations (this machine: use Python library + hf-mirror)

### Download models

The `hf` CLI is unreliable from this machine. Use the Python library instead:

```python
from huggingface_hub import hf_hub_download, snapshot_download

# Single file
path = hf_hub_download(repo_id="BAAI/bge-m3", filename="config.json")

# Full model (all files, cached)
path = snapshot_download(repo_id="BAAI/bge-m3")
```

> **On this machine, huggingface.co is blocked.** Set mirror endpoint first:
> ```bash
> export HF_ENDPOINT=https://hf-mirror.com
> ```
> Or in Python:
> ```python
> import os
> os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
> ```

### Search models

```python
import urllib.request, json
url = "https://hf-mirror.com/api/models?search=bge&limit=10"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read())
for m in data:
    print(m["id"], m.get("downloads", 0))
```

### hf-mirror.com API endpoints

| Purpose | URL |
|---------|-----|
| Search models | `https://hf-mirror.com/api/models?search=QUERY&limit=10` |
| List by author | `https://hf-mirror.com/api/models?author=ORG&limit=50&sort=downloads` |
| Model info | `https://hf-mirror.com/api/models/ORG/model-name` |
| File list | `https://hf-mirror.com/api/models/ORG/model-name/tree/main` |
| File download | `https://hf-mirror.com/download/ORG/model-name/snapshots/main/FILENAME` |

### Upload

Use Python library or `hf upload` CLI if network allows. Check connectivity first:
```python
import socket
try:
    socket.create_connection(("huggingface.co", 443), timeout=5)
    print("huggingface.co reachable")
except:
    print("blocked — use hf-mirror for downloads")
```

For uploads, `HF_ENDPOINT` has no effect — must reach huggingface.co directly.

### Authentication (`hf auth`)
*   `login` / `logout`: Manage sessions using tokens from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
*   `list` / `switch`: Manage and toggle between multiple stored access tokens.
*   `whoami`: Identify the currently logged-in account.

### Repository Management (`hf repos`)
*   `create` / `delete`: Create or permanently remove repositories.
*   `duplicate`: Clone a model, dataset, or Space to a new ID.
*   `move`: Transfer a repository between namespaces.
*   `branch` / `tag`: Manage Git-like references.
*   `delete-files`: Remove specific files using patterns.

---

## Specialized Hub Interactions

### Datasets & Models
*   **Datasets:** `hf datasets list`, `info`, and `parquet` (list parquet URLs).
*   **SQL Queries:** `hf datasets sql SQL` — Execute raw SQL via DuckDB against dataset parquet URLs.
*   **Models:** `hf models list` and `info`.
*   **Papers:** `hf papers list` — View daily papers.

### Discussions & Pull Requests (`hf discussions`)
*   Manage the lifecycle of Hub contributions: `list`, `create`, `info`, `comment`, `close`, `reopen`, and `rename`.
*   `diff`: View changes in a PR.
*   `merge`: Finalize pull requests.

### Infrastructure & Compute
*   **Endpoints:** Deploy and manage Inference Endpoints (`deploy`, `pause`, `resume`, `scale-to-zero`, `catalog`).
*   **Jobs:** Run compute tasks on HF infrastructure. Includes `hf jobs uv` for running Python scripts with inline dependencies and `stats` for resource monitoring.
*   **Spaces:** Manage interactive apps. Includes `dev-mode` and `hot-reload` for Python files without full restarts.

### Storage & Automation
*   **Buckets:** Full S3-like bucket management (`create`, `cp`, `mv`, `rm`, `sync`).
*   **Cache:** Manage local storage with `list`, `prune` (remove detached revisions), and `verify` (checksum checks).
*   **Webhooks:** Automate workflows by managing Hub webhooks (`create`, `watch`, `enable`/`disable`).
*   **Collections:** Organize Hub items into collections (`add-item`, `update`, `list`).

---

### Large file downloads (multi-GB models)

For models >1GB (e.g. pytorch_model.bin), Python library downloads via `snapshot_download` **will time out** on this machine — huggingface_hub itself makes network calls that block. Use `curl` via terminal instead, with the terminal tool's native `background: true` mode:

```bash
# Use terminal's background mode (NOT shell & operator — that gets blocked)
curl -L -C - -o "/path/to/model.bin" "https://hf-mirror.com/ORG/model/resolve/main/model.bin"
# Set background: true, notify_on_complete: true, timeout: 600

# Monitor with polling (use execute_code, NOT terminal, to avoid blocking):
python3 -c "
import os
size = os.path.getsize('/path/to/model.bin')
print(f'{size/1024**3:.2f} GB downloaded')
"
```

**Monitoring pattern**: `ls -lh /path/to/model.bin` every 60-90s via terminal. When curl reaches 100% it exits.

**Pitfall**: terminal tool with `&` background operator gets rejected. Always use terminal tool's native `background: true` parameter.

## Advanced Usage & Tips

### Global Flags
*   `--format json`: Produces machine-readable output for automation.
*   `-q` / `--quiet`: Limits output to IDs only.

### Extensions & Skills
* **Extensions:** Extend CLI functionality via GitHub repositories using `hf extensions install REPO_ID`.
* **Skills:** Manage AI assistant skills with `hf skills add`.

## Support Files
- `references/bge-models.md` — BGE embedding model catalog, usage examples, note on "bge3" naming confusion
- `references/bge-m3-download.md` — Full session log of BAAI/bge-m3 download (2.14GB, 7min via hf-mirror)
- `scripts/hf_download.py` — Resumable download script using hf-mirror.com
