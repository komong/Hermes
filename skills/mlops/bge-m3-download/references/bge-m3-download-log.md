# BGE-M3 下载记录

**日期**: 2026-05-05  
**模型**: BAAI/bge-m3  
**大小**: ~2.14 GB  
**下载耗时**: ~7 分钟（hf-mirror.com，速度 ~6MB/s）  
**缓存路径**: `~/.cache/huggingface/hub/models--BAAI--bge-m3/snapshots/main/`  
**网络环境**: 中国大陆，HuggingFace 直连超时

## 文件清单

| 文件名 | 大小 | 说明 |
|--------|------|------|
| pytorch_model.bin | 2.17 GB | 主模型权重（最大文件） |
| tokenizer.json | 16.3 MB | 分词器数据 |
| tokenizer_config.json | ~0.4 KB | 分词器配置 |
| special_tokens_map.json | ~1.0 KB | 特殊 token 映射 |
| sentencepiece.bpe.model | 4.9 MB | SentencePiece BPE 模型 |
| sparse_linear.pt | 3.5 KB | Sparse 向量层权重 |
| colbert_linear.pt | 2.1 MB | ColBERT 向量层权重 |
| config.json | ~0.7 KB | 模型配置 |
| modules.json | ~0.3 KB | 模块映射 |
| README.md | 16 KB | 模型说明文档 |
| 1_Pooling/config.json | ~0.2 KB | Pooling 层配置 |

## 下载步骤

1. **小文件批量下载**（timeout 120s）：tokenizer.json、config.json、modules.json 等
2. **大文件用 terminal native background mode**：`curl -L -C - -o ...`  
   ⚠️ 不要用 shell `&` 后台运行，会被安全扫描拦截
3. **每 60-90s 用 `ls -lh`** 监控进度
4. curl 正常退出（exit 0）后确认文件大小

## Python 完整下载代码

```python
import os

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

from huggingface_hub import snapshot_download

# ignore_patterns 绕过 hf-mirror 对 .DS_Store 和 imgs/ 的 403 限制
snapshot_download(
    "BAAI/bge-m3",
    ignore_patterns=["*.DS_Store", "imgs/*"]
)
```

## 验证模型已正确下载

```python
import os
os.environ["HF_HUB_OFFLINE"] = "1"  # 强制离线，避免 FlagEmbedding 内部再次触发 403

from FlagEmbedding import BGEM3FlagModel
model = BGEM3FlagModel("BAAI/bge-m3")
vec = model.encode("hello world")
print(f"向量维度: {len(vec['dense_vecs'][0])}")  # 应输出 1024
```

## 关于 "bge3" 命名

HuggingFace 上没有叫 "bge3" 的模型。BAAI 的向量模型最新为 **BGE-M3**（bge-m3）。BGE 家族版本如下：

| 模型 ID | 维度 | 适用场景 |
|---------|------|---------|
| BAAI/bge-m3 | 1024 | 多语言最新，100+ 语言，中英文最优 |
| BAAI/bge-large-zh-v1.5 | 1024 | 中文专用大模型 |
| BAAI/bge-small-zh-v1.5 | 512 | 中文专用小模型 |
| BAAI/bge-small-en-v1.5 | 384 | 英文专用小模型 |

注：bge-m3 实际是 BGE 家族第三版，"bge3" 可能是用户对 BGE-M3 的简称。
