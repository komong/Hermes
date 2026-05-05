# Hermes — 沉淀的知识与技能

该仓库收录了我们为 Hermes Agent 积累的自定义技能（Skills）和输出文档。每个技能都是一个可复用的 AI 工作流，涵盖系统配置、群组交互、QA 测试、Apple 设备管理、域名情报等多个领域。

## 📂 目录结构

```
├── skills/               # Hermes Agent 自定义技能
│   ├── sogou-pinyin-ubuntu/  # 搜狗输入法 Ubuntu 安装
│   ├── yuanbao/              # 元宝群组 @提及/私信
│   ├── dogfood/              # Web 应用 QA 自动测试
│   │   ├── references/       # 问题分类规范
│   │   └── templates/        # 报告模板
│   ├── apple/                # macOS 技能组
│   │   ├── apple-notes/      #  Apple Notes 管理
│   │   ├── apple-reminders/  #  Apple Reminders 管理
│   │   ├── findmy/           #  设备/AirTag 追踪
│   │   └── imessage/         #  iMessage 收发
│   ├── domain/               # 域名情报调查
│   └── inference-sh/         # AI 云平台 (150+ 服务)
│
└── docs/                    # 输出文档
    └── 搜狗输入法安装说明.md
```

## 🧠 技能一览

| 技能 | 分类 | 说明 | 平台 |
|------|------|------|------|
| [sogou-pinyin-ubuntu](./skills/sogou-pinyin-ubuntu/README.md) | 系统配置 | Ubuntu 22.04 自动安装搜狗输入法 | Linux |
| [yuanbao](./skills/yuanbao/README.md) | 群组交互 | 元宝群组 @提及、私信、信息查询 | 跨平台 |
| [dogfood](./skills/dogfood/README.md) | QA 测试 | Web 应用探索性测试 + Bug 报告 | 跨平台 |
| [apple-notes](./skills/apple/apple-notes/README.md) | 效率工具 | 管理 Apple Notes 笔记 | macOS |
| [apple-reminders](./skills/apple/apple-reminders/README.md) | 效率工具 | 管理提醒事项 | macOS |
| [findmy](./skills/apple/findmy/README.md) | 设备追踪 | 追踪 Apple 设备/AirTag 位置 | macOS |
| [imessage](./skills/apple/imessage/README.md) | 消息通讯 | 收发 iMessage/SMS 短信 | macOS |
| [domain](./skills/domain/README.md) | 情报收集 | 被动域名情报（子域名、SSL、WHOIS） | 跨平台 |
| [inference-sh](./skills/inference-sh/README.md) | AI 服务 | 150+ AI 服务聚合调用 | 跨平台 |

## 📄 文档

- [搜狗输入法 Ubuntu 安装说明](./docs/搜狗输入法安装说明.md) — 完整的搜狗输入法安装指南（适合直接阅读）

## 🔧 词条说明

每个技能文件夹包含：
- **SKILL.md** — Hermes Agent 直接读取的技能定义
- **README.md**（中文） — 面向人类的说明文档

## 🚀 如何使用

这些技能通过 Hermes Agent 加载使用。在 Hermes 中可以通过以下方式生效：

```bash
# 将技能链接到 Hermes 技能目录
ln -s /path/to/Hermes/skills/* ~/.hermes/skills/
```

然后在对话中对 Agent 说出相关的需求，Agent 会自动加载对应的技能并执行。
