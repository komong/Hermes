# Find My 设备追踪工具

> Hermes Agent 技能：通过屏幕截图 + AI 视觉分析追踪 Apple 设备和 AirTag 的位置

## 概述

由于 Apple 没有为 Find My 提供官方 CLI 或 API，该技能通过 AppleScript 打开 Find My 应用，截取屏幕，然后使用 AI 视觉分析读取设备位置。

## 前置条件

| 条件 | 说明 |
|------|------|
| 系统 | macOS（需要 Find My 应用 + iCloud 登录） |
| 设备 | 已在 Find My 中注册的设备/AirTag |
| 权限 | 屏幕录制权限（System Settings → Privacy → Screen Recording） |
| 推荐工具 | `peekaboo` — `brew install steipete/tap/peekaboo`（更可靠的 UI 自动化） |

## 使用方式

对 Agent 说类似以下的话：

```
我的 iPhone 在哪？
帮我找我家的钥匙（AirTag）
追踪我的猫的行踪
查一下我的 AirPods 位置
```

## 工作流程

Agent 会自动执行：
1. 通过 AppleScript 打开 Find My 应用
2. 切换到"设备"或"物品"标签页
3. 截取屏幕
4. 用 AI 视觉分析读取位置信息
5. 将结果回复给你

## 注意事项

- AirTag 只在页面打开时更新位置（最小化后停止更新）
- 位置精度取决于附近 Apple 设备的 Find My 网络覆盖
- 持续追踪建议使用定时任务定期截图记录

## 文件结构

```
findmy/
├── SKILL.md    # Hermes Agent 技能定义
└── README.md   # 本文件 · 使用说明
```
