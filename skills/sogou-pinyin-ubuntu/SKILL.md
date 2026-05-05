---
name: sogou-pinyin-ubuntu
description: Install Sogou Pinyin (搜狗输入法) on Ubuntu 22.04 LTS with fcitx4. Covers environment detection, fcitx4 setup, Qt5 deps, deb download from working CDN mirror, dpkg install, and .xprofile configuration.
category: productivity
---

# 搜狗输入法 Ubuntu 22.04 安装指南

## 适用环境
- **系统**: Ubuntu 22.04 LTS (x86_64)
- **会话**: X11 (非 Wayland)
- **输入法框架**: fcitx4 (搜狗依赖 fcitx4，不是 fcitx5)

## 前置检查

```bash
# 确认架构和会话类型
uname -m          # 应返回 x86_64
echo $XDG_SESSION_TYPE  # 应返回 x11

# 检查是否已有 fcitx5（需卸载）
dpkg -l | grep fcitx5
# 如有: sudo apt purge fcitx5* && sudo apt autoremove
```

## 安装步骤

### 1. 安装 fcitx4 输入法框架

```bash
sudo apt install fcitx fcitx-bin fcitx-table
# 注意: fcitx-config-gtk2 在 22.04 已废弃，不影响功能，可忽略
```

### 2. 配置环境变量（写入 ~/.xprofile）

```bash
cat << 'EOF' > ~/.xprofile
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS="@im=fcitx"
EOF
```

> **关键**: `.xprofile` 是 X11 会话加载环境变量的最佳位置，比 `.profile` 更早加载，确保输入法在桌面会话启动时就生效。

### 3. 设置 im-config

```bash
im-config -n fcitx
```

### 4. 安装 Qt5 核心依赖（搜狗输入法面板依赖）

```bash
sudo apt install libgsettings-qt1 libqt5quickwidgets5
# libqt5qml5 libqt5quick5 qml-module-qtquick2 通常已预装
```

### 5. 下载搜狗输入法 deb 包

**⚠️ 关键发现**: 搜狗官方 CDN (`ime-sec.gtimg.com`) 封锁了非浏览器直接下载，但 `ime.gtimg.com` 子域名可用。

```bash
# 可用下载源（按顺序尝试）
URL="https://ime.gtimg.com/pc/dl/gzindex/1680521603/sogoupinyin_4.2.1.145_amd64.deb"
# 备用 CDN（需带 Referer 头）
# URL="https://ime-sec.gtimg.com/pc/dl/gzindex/1680521603/sogoupinyin_4.2.1.145_amd64.deb"

cd ~/Downloads
curl -L -o sogoupinyin.deb "$URL"
```

**镜像源检测脚本**:
```bash
# 测试各 CDN 是否可达
for cdn in "ime.gtimg.com" "imgcache.gtimg.com" "pinyin.cdn.sogou.com"; do
  status=$(curl -sI --max-time 5 "https://$cdn/pc/dl/gzindex/1680521603/sogoupinyin_4.2.1.145_amd64.deb" 2>/dev/null | head -1)
  echo "$cdn: $status"
done
```

### 6. 安装 deb 包

```bash
cd ~/Downloads
sudo dpkg -i sogoupinyin.deb
# 如有依赖问题:
sudo apt --fix-broken install
```

### 7. 系统语言设置（需图形界面操作）

重启后打开: **Settings → Region & Language → Manage Installed Languages**
- **Keyboard input method system** → 选择 **`fcitx`**
- 点击 **"Apply System-Wide"**

### 8. 添加搜狗拼音到输入法列表

1. 右上角托盘点击 **键盘图标** → **Configure**
2. 点击 **"+"** → 搜索 `Sogou Pinyin`
3. 如找不到 → **取消勾选 "Only Show Current Language"** 再搜索
4. 确认搜狗在列表中

## 验证

```bash
# 检查服务状态
fcitx-dbus &
sogou-qimpanel &

# 查看已安装的输入法
fcitx-dbus list
```

## 常见问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 官方 CDN 返回 403 | 防盗链封锁 | 改用 `ime.gtimg.com` 或浏览器下载 |
| `.xprofile` 不生效 | 文件权限或加载顺序 | `chmod 644 ~/.xprofile`，确认 im-config 为 fcitx |
| 搜狗找不到 | 勾选了"仅显示当前语言" | 取消勾选后再搜索 |
| fcitx 选项不存在 | 系统默认 fcitx5 | `sudo apt purge fcitx5* && sudo apt autoremove` |
| 候选框显示异常 | fcitx4 + 新版 GTK 兼容性问题 | 不影响输入，可忽略 |

## 双拼配置

搜狗内置小鹤双拼。进入搜狗配置 → "双拼布局" → 选择 **"小鹤双拼"**。

## 卸载

```bash
sudo apt purge sogoupinyin fcitx fcitx-bin fcitx-table fcitx-*
sudo apt autoremove
rm ~/.xprofile
im-config -n ibus  # 恢复 ibus
```
