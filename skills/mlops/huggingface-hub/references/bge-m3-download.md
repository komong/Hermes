# BGE-M3 下载记录

**日期**: 2026-05-05
**模型**: BAAI/bge-m3
**大小**: ~2.14 GB
**下载耗时**: ~7 分钟（hf-mirror.com，速度 ~6MB/s）
**下载路径**: `/home/admin/.cache/huggingface/hub/models--BAAI--bge-m3/snapshots/main/`

## 文件清单

| 文件 | 大小 |
|------|------|
| pytorch_model.bin | 2.17 GB |
| tokenizer.json | 16.3 MB |
| tokenizer_config.json | 0.4 KB |
| special_tokens_map.json | 1.0 KB |
| sentencepiece.bpe.model | 4.9 MB |
| sparse_linear.pt | 3.5 KB |
| colbert_linear.pt | 2.1 MB |
| config.json | 0.7 KB |
| modules.json | 0.3 KB |
| README.md | 16 KB |
| 1_Pooling/config.json | 0.2 KB |

## 下载步骤

1. 先下小文件（批量 curl，timeout 120s）
2. 大文件用 terminal native background mode
3. 每 60-90s 用 `ls -lh` 监控进度
4. curl 退出（exit 0）后确认文件大小

## 关于 "bge3" 命名

HuggingFace 上没有叫 "bge3" 的模型。BAAI 的向量模型最新为 **BGE-M3**（bge-m3），BGE 家族版本如下：

- bge-m3 — 多语言最新（1024维，支持100+语言）
- bge-large-zh-v1.5 — 中文大模型
- bge-small-zh-v1.5 — 中文小模型
- bge-small-en-v1.5 — 英文小模型

注：bge-m3 实际是 BGE 家族第三版（不是第四版），"bge3" 可能是用户对 BGE-M3 的简称。
