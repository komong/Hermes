# iMessage 消息收发工具

> Hermes Agent 技能：通过 `imsg` CLI 发送和读取 iMessage / SMS 短信

## 概述

使用 `imsg` 命令行工具在 macOS 上收发 iMessage 和 SMS 短信。消息通过 macOS Messages.app 发送，支持纯文本和附件。

## 前置条件

| 条件 | 说明 |
|------|------|
| 系统 | macOS（需要 Messages.app 已登录） |
| 工具 | `imsg` — 通过 `brew install steipete/tap/imsg` 安装 |
| 权限 | 完全磁盘访问权限（System Settings → Privacy → Full Disk Access） |
| 权限 | 授予终端对 Messages.app 的自动化控制权限 |

## 使用方式

对 Agent 说类似以下的话：

```
给妈妈发条短信说我晚点到
帮我查一下最近的消息
给 +86 138xxxxxxx 发 "到楼下了"
看一下我和张三的聊天记录
```

## 常用功能

| 功能 | 说明 |
|------|------|
| 列出聊天 | 查看最近的聊天列表 |
| 查看历史 | 查看某个聊天的消息记录（支持附件信息） |
| 发送消息 | 给指定号码或联系人发消息 |
| 发送附件 | 附带图片或文件 |
| 选择服务 | 强制 iMessage（蓝色气泡）或 SMS（绿色气泡） |

## 安全规则

- 发送前必须确认接收人和消息内容
- 不向未知号码发送消息
- 不批量/群发消息

## 文件结构

```
imessage/
├── SKILL.md    # Hermes Agent 技能定义
└── README.md   # 本文件 · 使用说明
```
