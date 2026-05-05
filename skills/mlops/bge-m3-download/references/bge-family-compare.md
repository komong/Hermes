# BGE 模型家族对比

BGE（Baidu General Embedding）是 BAAI（FlagAI）开源的嵌入模型系列。以下是各模型的对比。

## 模型对比表

| 模型 | HuggingFace ID | 维度 | 模态 | 支持语言 | 模型大小 | 推荐场景 |
|------|---------------|------|------|---------|---------|---------|
| **BGE-M3** | `BAAI/bge-m3` | 1024 | Dense + Sparse + ColBERT | 100+（含中英） | ~2.1 GB | 多语言检索、RAG、本地知识库 |
| BGE-Large-ZH | `BAAI/bge-large-zh-v1.5` | 1024 | Dense | 中文 | ~1.3 GB | 中文专用检索 |
| BGE-Small-ZH | `BAAI/bge-small-zh-v1.5` | 512 | Dense | 中文 | ~130 MB | 中文轻量场景 |
| BGE-Small-EN | `BAAI/bge-small-en-v1.5` | 384 | Dense | 英文 | ~40 MB | 英文轻量场景 |

## BGE-M3 的优势

1. **多语言统一**：一个模型覆盖 100+ 语言，无需为每种语言单独部署
2. **三种向量输出**：Dense（稠密）、Sparse（稀疏）、ColBERT（交互式），灵活适配不同检索场景
3. **中英文兼顾**：对中英文混合内容的检索效果优异
4. **长文本支持**：max_length=8192，适合文档级别检索

## BGE-M3 下载问题汇总

| 问题 | 原因 | 解决方案 |
|------|------|---------|
| ConnectTimeout | HF 直连被墙 | `HF_ENDPOINT=https://hf-mirror.com` |
| 403 Forbidden | hf-mirror 对 .DS_Store/imgs/ 限制 | `ignore_patterns=['*.DS_Store', 'imgs/*']` |
| 初始化仍 403 | FlagEmbedding 内部再调用 snapshot_download | `HF_HUB_OFFLINE=1` |
| 速度慢 | hf-mirror 单线程下载 | 大文件用 `curl -C - -o` 后台下载 |

## 选型建议

- **多语言 RAG / 本地知识库** → BGE-M3（推荐）
- **中文专用、重性能** → BGE-Large-ZH
- **中文轻量、内存敏感** → BGE-Small-ZH
- **英文轻量** → BGE-Small-EN
