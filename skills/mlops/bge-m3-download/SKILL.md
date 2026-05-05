---
name: bge-m3-download
description: "下载 BAAI/bge-m3 嵌入模型：hf-mirror 镜像 + snapshot_download ignore_patterns 绕过 403 + HF_HUB_OFFLINE 强制缓存"
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [huggingface, embedding, bge-m3, hf-mirror, mlops]
related_skills: [huggingface-hub]
---

# BGE-M3 模型下载技能

在中国大陆网络环境下，下载 HuggingFace 上的 BAAI/bge-m3 嵌入模型（~2.1GB）需要绕过三个坑：
1. HuggingFace 直连超时
2. hf-mirror 对 `.DS_Store` 和 `imgs/*` 返回 403
3. `FlagEmbedding` 库内部会重新调 `snapshot_download`，再次触发 403

## 适用场景

| 场景 | 触发关键词 |
|------|-----------|
| 下载 bge-m3 模型 | "下载 bge-m3"、"bge m3 模型"、"BAAI/bge-m3" |
| embedding 模型下载失败 | "HF 403"、"hf-mirror 错误"、"embedding 模型下不下来" |
| AI-knowledge 项目部署 | "AI-knowledge"、"Qdrant"、"embedding" |

## 快速开始

### 方式一：Python 脚本（推荐）

```python
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download
# ignore_patterns 绕过 hf-mirror 403 错误
snapshot_download(
    "BAAI/bge-m3",
    ignore_patterns=["*.DS_Store", "imgs/*"]
)
```

### 方式二：curl 分文件下载（大文件用后台模式）

```bash
# 设置镜像
export HF_ENDPOINT=https://hf-mirror.com

# 小文件批量下载
for f in config.json tokenizer.json tokenizer_config.json special_tokens_map.json sentencepiece.bpe.model sparse_linear.pt colbert_linear.pt modules.json; do
  curl -L -o "/tmp/$f" "https://hf-mirror.com/BAAI/bge-m3/resolve/main/$f" --max-time 120
done

# 大文件用 terminal native background mode（不要用 shell &，会报语法错误）
curl -L -C - -o "/tmp/pytorch_model.bin" "https://hf-mirror.com/BAAI/bge-m3/resolve/main/pytorch_model.bin"
# 在 terminal 调用时使用 background=true 参数
```

### 方式三：huggingface_hub CLI

```bash
export HF_ENDPOINT=https://hf-mirror.com
pip install huggingface-hub
python -c "
from huggingface_hub import snapshot_download
snapshot_download('BAAI/bge-m3', ignore_patterns=['*.DS_Store', 'imgs/*'])
"
```

## 已在项目中引用

项目路径：`./projects/Qoder/Sandbox/AI-knowlege/src/embedder.py`

```python
from FlagEmbedding import BGEM3FlagModel

MODEL_NAME = "BAAI/bge-m3"
EMBED_DIM = 1024
```

## 三个坑及解决方案

### 坑 1：HuggingFace 直连超时

**现象**：`ConnectTimeout: HTTPSConnectionPool(host='huggingface.co', ...)`

**原因**：大陆网络无法直连 huggingface.co

**解决**：设置 `HF_ENDPOINT=https://hf-mirror.com`

### 坑 2：hf-mirror 返回 403 Forbidden

**现象**：`HTTPError 403 Forbidden` 对 `.DS_Store` 或 `imgs/*` 文件

**原因**：hf-mirror 对这些隐藏文件/目录做了访问限制

**解决**：`snapshot_download(..., ignore_patterns=['*.DS_Store', 'imgs/*'])`

⚠️ **注意**：即便外层预下载加了 ignore_patterns，`FlagEmbedding` 内部仍会自己调 `snapshot_download` 再次触发 403。需要配合坑 3 的方案。

### 坑 3：FlagEmbedding 内部触发 403

**现象**：预下载成功，但 `BGEM3FlagModel(...)` 初始化时仍然报 403

**原因**：`FlagEmbedding` 库内部在初始化时会独立调用 `snapshot_download`，忽略外层的 ignore_patterns

**解决**：运行时设置 `HF_HUB_OFFLINE=1`，强制使用本地缓存

```bash
export HF_HUB_OFFLINE=1
python -c "from FlagEmbedding import BGEM3FlagModel; model = BGEM3FlagModel('BAAI/bge-m3')"
```

## 完整部署命令（AI-knowledge 项目）

```bash
# 1. 设置镜像
export HF_ENDPOINT=https://hf-mirror.com

# 2. 预下载模型（忽略 403 文件）
python -c "
from huggingface_hub import snapshot_download
snapshot_download('BAAI/bge-m3', ignore_patterns=['*.DS_Store', 'imgs/*'])
"

# 3. 安装依赖
pip install FlagEmbedding qdrant-client torch

# 4. 运行（强制离线缓存）
HF_HUB_OFFLINE=1 python -c "from src.embedder import embed_text; print(embed_text('hello'))"
```

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型 ID | `BAAI/bge-m3` |
| 维度 | 1024（稠密向量） |
| 模型大小 | ~2.14 GB |
| 缓存位置 | `~/.cache/huggingface/hub/models--BAAI--bge-m3/` |
| 支持语言 | 100+ 语言（中英文最优） |

## 验证方法

```python
from src.embedder import embed_text
vec = embed_text("你好世界")
print(len(vec))  # 应输出 1024
```

## 相关文件

- `references/bge-m3-download-log.md` — 完整下载记录与文件清单
- `references/bge-family-compare.md` — BGE 模型家族对比
