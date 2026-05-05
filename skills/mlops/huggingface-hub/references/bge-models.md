# BGE Embedding Models Reference

BGE = BAAI General Embedding. The go-to open-source embedding model family.

## Key Models

| Model ID | Language | Size | Dims | Notes |
|----------|----------|------|------|-------|
| `BAAI/bge-m3` | Multilingual (100+) | ~2GB | 1024 | Latest gen, best overall |
| `BAAI/bge-large-en-v1.5` | English | ~1.3GB | 1024 | Top English-only |
| `BAAI/bge-base-en-v1.5` | English | ~0.7GB | 768 | Balanced |
| `BAAI/bge-small-en-v1.5` | English | ~0.5GB | 384 | Fast/lightweight |
| `BAAI/bge-large-zh-v1.5` | Chinese | ~1.3GB | 1024 | Best Chinese |
| `BAAI/bge-small-zh-v1.5` | Chinese | ~0.5GB | 512 | Fast Chinese |
| `BAAI/bge-base-zh-v1.5` | Chinese | ~0.7GB | 768 | Balanced Chinese |
| `BAAI/bge-reranker-v2-m3` | Multilingual | ~2.7GB | — | Cross-encoder reranker |
| `BAAI/llm-embedder` | General | — | — | For LLM-as-judge scenarios |

## Download (this machine)

```python
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download

# Full model to cache
path = snapshot_download(repo_id="BAAI/bge-m3")
print(path)  # e.g. ~/.cache/huggingface/hub/models--BAAI--bge-m3/

# Single file
from huggingface_hub import hf_hub_download
cfg = hf_hub_download(repo_id="BAAI/bge-m3", filename="config.json")
```

## Usage (sentence-transformers)

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("BAAI/bge-m3")
embeddings = model.encode(["Hello world", "你好世界"])
# embeddings[i] is a 1024-dim vector
```

## Reranking

```python
from sentence_transformers import CrossEncoder

reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")
scores = reranker.predict([("query", "candidate1"), ("query", "candidate2")])
```

## Note on "bge3"

There is no HuggingFace model named "bge3". The latest version is **BGE-M3** (bge-m3). The user likely means either:
- `BAAI/bge-m3` (multilingual, latest)
- `BAAI/bge-large-zh-v1.5` (best Chinese)
