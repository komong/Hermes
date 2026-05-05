# Apple Reminders 提醒事项管理工具

> Hermes Agent 技能：通过 `remindctl` 管理 Apple 提醒事项

## 概述

使用 `remindctl` CLI 在终端中管理 Apple Reminders。提醒事项通过 iCloud 同步到所有 Apple 设备。

## 前置条件

| 条件 | 说明 |
|------|------|
| 系统 | macOS（需要 Reminders.app） |
| 工具 | `remindctl` — 通过 `brew install steipete/tap/remindctl` 安装 |
| 权限 | 授予 Reminders 访问权限（首次运行会提示） |

## 使用方式

对 Agent 说类似以下的话：

```
帮我添加一个提醒：明天下午3点开会
今天有哪些提醒事项？
提醒我周五买牛奶
查一下这周的提醒
```

## 常用功能

| 功能 | 示例 |
|------|------|
| 查看今日提醒 | `remindctl` 或 `remindctl today` |
| 查看本周 | `remindctl week` |
| 查看过期 | `remindctl overdue` |
| 创建提醒 | `remindctl add --title "买牛奶" --due tomorrow` |
| 完成提醒 | `remindctl complete 1` |
| 管理清单 | `remindctl list Work --create` |

## 日期格式

- `today`、`tomorrow`、`yesterday`
- `YYYY-MM-DD`
- `YYYY-MM-DD HH:mm`
- ISO 8601（`2026-01-04T12:34:56Z`）

## 文件结构

```
apple-reminders/
├── SKILL.md    # Hermes Agent 技能定义
└── README.md   # 本文件 · 使用说明
```
