# 搜狗输入法 Ubuntu 安装工具

> Hermes Agent 技能：在 Ubuntu 22.04 LTS 上自动化安装搜狗输入法（Sogou Pinyin）

## 概述

该技能帮助你在 **Ubuntu 22.04 LTS (x86_64)** 系统上安装搜狗拼音输入法。全程通过命令行完成，从 fcitx4 框架安装、Qt5 依赖、CDN 下载 deb 包到配置环境变量，一步到位。

适用的系统环境：
- ✅ Ubuntu 22.04 LTS
- ✅ X11 会话（非 Wayland）
- ✅ x86_64 架构

## 前置条件

| 条件 | 说明 |
|------|------|
| 操作系统 | Ubuntu 22.04 LTS |
| 会话类型 | X11（`echo $XDG_SESSION_TYPE` 应返回 `x11`） |
| 架构 | x86_64（`uname -m` 应返回 `x86_64`） |

## 使用方式

对 Hermes Agent 说类似以下的话即可触发：

```
帮我在 Ubuntu 上装搜狗输入法
安装中文输入法
设置搜狗拼音
```

Agent 将自动执行：
1. 检测系统环境（架构、会话类型）
2. 安装 fcitx4 框架
3. 配置环境变量（`~/.xprofile`）
4. 安装 Qt5 依赖
5. 从 CDN 下载搜狗输入法 deb 包
6. 安装并修复依赖

## 安装后操作

安装完成后需要：
- 重启系统（或登出后重新登录）
- 打开 **Settings → Region & Language → Manage Installed Languages**
- 将 **Keyboard input method system** 设为 `fcitx`
- 点击 **Apply System-Wide**
- 在 fcitx 配置中添加 `Sogou Pinyin` 输入法

## 常见问题

| 问题 | 解决方案 |
|------|----------|
| 官方 CDN 下载失败（403） | 自动使用备用 CDN `ime.gtimg.com` |
| 搜狗在输入法列表找不到 | 取消勾选 "Only Show Current Language" |
| 安装后无法切换输入法 | 执行 `fcitx -d` 手动启动服务 |
| 之前装了 fcitx5 | 会自动检测并提示卸载冲突 |

## 文件结构

```
sogou-pinyin-ubuntu/
├── SKILL.md    # Hermes Agent 技能定义（自动执行）
└── README.md   # 本文件 · 使用说明
```
