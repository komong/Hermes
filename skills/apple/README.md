# Apple / macOS 技能组

> 适用于 macOS 系统的 Hermes Agent 技能集合

该组技能需要通过 macOS 自带的 `osascript`（AppleScript）和第三方 CLI 工具与 Apple 原生应用交互。**仅在 macOS 上可用。**

## 包含的技能

| 技能 | 功能 | 依赖 |
|------|------|------|
| [📝 Apple Notes](./apple-notes/README.md) | 创建、搜索、编辑 Apple Notes | `memo` CLI |
| [✅ Apple Reminders](./apple-reminders/README.md) | 添加、查看、完成提醒事项 | `remindctl` CLI |
| [📍 Find My](./findmy/README.md) | 追踪设备/AirTag 位置 | FindMy.app + 屏幕截图 |
| [💬 iMessage](./imessage/README.md) | 收发 iMessage / SMS 短信 | `imsg` CLI |

## 使用前准备

每个子技能都有特定的前置条件，请参考对应的 README 了解详情。通用的 macOS 权限包括：
- **辅助功能权限**（System Settings → Privacy → Accessibility）
- **完全磁盘访问权限**（Full Disk Access）
- **屏幕录制权限**（Screen Recording，Find My 需要）
