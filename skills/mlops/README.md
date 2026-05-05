# MLOps 技能组

> 机器学习运维相关的 Hermes Agent 技能集合

本组涵盖模型下载、推理服务、微调训练、评测等 MLOps 全流程技能。

## 包含的技能

| 技能 | 功能 | 依赖 |
|------|------|------|
| [bge-m3-download](./bge-m3-download/README.md) | 在国内网络下下载 BAAI/bge-m3 嵌入模型 | huggingface-hub |
| [huggingface-hub](./huggingface-hub/README.md) | HuggingFace 模型/数据集搜索与下载 | huggingface-hub |
| [llama-cpp](./llama-cpp/README.md) | 本地 GGUF 推理 | llama.cpp |
| [serving-llms-vllm](./serving-llms-vllm/README.md) | vLLM 高吞吐推理服务 | vLLM |
| [fine-tuning-with-trl](./fine-tuning-with-trl/README.md) | SFT/DPO/GRPO 微调 | TRL, transformers |

## 使用前准备

部分技能需要特定环境变量或 GPU 支持，请参考各技能文档。
