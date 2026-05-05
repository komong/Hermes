# Apple Notes 管理工具

> Hermes Agent 技能：通过命令行管理 Apple Notes，支持创建、搜索、编辑笔记

## 概述

使用 `memo` CLI 工具在终端中管理 Apple Notes。笔记通过 iCloud 同步到所有 Apple 设备（iPhone、iPad、Mac）。

## 前置条件

| 条件 | 说明 |
|------|------|
| 系统 | macOS（需要 Notes.app） |
| 工具 | `memo` CLI — 通过 `brew tap antoniorodr/memo && brew install antoniorodr/memo/memo` 安装 |
| 权限 | 授予终端对 Notes.app 的自动化控制权限 |

## 使用方式

对 Agent 说类似以下的话：

```
帮我创建一个笔记 "购物清单"
查一下我有哪些笔记
搜索包含"会议"的笔记
把这条信息记到 Apple Notes 里
```

## 常用功能

| 功能 | 说明 |
|------|------|
| 列出笔记 | 查看所有笔记，可按文件夹筛选 |
| 搜索笔记 | 模糊搜索笔记标题和内容 |
| 创建笔记 | 快速创建带标题的笔记 |
| 编辑笔记 | 打开编辑器修改已有笔记 |
| 导出笔记 | 导出为 HTML / Markdown |
| 移动笔记 | 将笔记移动到指定文件夹 |
| 删除笔记 | 交互式选择后删除 |

## 局限

- 不能编辑包含图片或附件的笔记
- 交互式操作需要终端 PTY 支持
- 仅限 macOS 平台

## 文件结构

```
apple-notes/
├── SKILL.md    # Hermes Agent 技能定义
└── README.md   # 本文件 · 使用说明
```
