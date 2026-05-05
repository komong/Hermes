# BGE-M3 模型下载工具

> 在中国大陆网络环境下，通过 HuggingFace 镜像下载 BAAI/bge-m3 嵌入模型（~2.1GB）的完整指南

## 概述

**BGE-M3** 是 BAAI（FlagAI）开源的多语言嵌入模型，支持 100+ 语言，中英文检索效果优秀。本技能解决在国内下载该模型时遇到的三层网络障碍。

适用系统：Linux（Ubuntu 22.04 等）、Windows + WSL、macOS

## 快速上手

```bash
# 第一步：设置镜像源
export HF_ENDPOINT=https://hf-mirror.com

# 第二步：预下载模型（忽略触发 403 的文件）
pip install huggingface-hub
python -c "
from huggingface_hub import snapshot_download
snapshot_download('BAAI/bge-m3', ignore_patterns=['*.DS_Store', 'imgs/*'])
"

# 第三步：验证（强制离线，避免 FlagEmbedding 内部再次触发 403）
export HF_HUB_OFFLINE=1
python -c "
from FlagEmbedding import BGEM3FlagModel
model = BGEM3FlagModel('BAAI/bge-m3')
print(model.encode('hello'))
"
```

## 三个坑及解决方案

### 坑 1：HuggingFace 直连超时

| 项目 | 说明 |
|------|------|
| 现象 | `ConnectTimeout` 或无响应 |
| 原因 | 大陆网络无法访问 huggingface.co |
| 解决 | `export HF_ENDPOINT=https://hf-mirror.com` |

### 坑 2：hf-mirror 返回 403

| 项目 | 说明 |
|------|------|
| 现象 | `HTTPError 403 Forbidden` 对 `.DS_Store` 或 `imgs/` |
| 原因 | hf-mirror 对隐藏文件/目录有限制 |
| 解决 | `snapshot_download(..., ignore_patterns=['*.DS_Store', 'imgs/*'])` |

### 坑 3：FlagEmbedding 初始化时 403

| 项目 | 说明 |
|------|------|
| 现象 | 预下载成功，但 `BGEM3FlagModel(...)` 仍报 403 |
| 原因 | FlagEmbedding 内部独立调用 snapshot_download，忽略外层 ignore_patterns |
| 解决 | `export HF_HUB_OFFLINE=1`（强制只用本地缓存） |

## 模型信息

| 属性 | 值 |
|------|-----|
| 模型 ID | `BAAI/bge-m3` |
| 向量维度 | 1024（稠密向量） |
| 模型大小 | ~2.14 GB |
| 缓存路径 | `~/.cache/huggingface/hub/models--BAAI--bge-m3/` |
| 支持语言 | 100+（中英文最优） |
| 下载耗时 | ~7 分钟（hf-mirror.com，约 6MB/s） |

## 文件结构

```
bge-m3-download/
├── SKILL.md                    # Hermes Agent 技能定义
├── README.md                   # 本文件 · 用户指南
└── references/
    ├── bge-m3-download-log.md  # 完整下载记录与文件清单
    └── bge-family-compare.md   # BGE 模型家族对比
```
