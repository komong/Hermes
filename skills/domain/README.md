# 域名情报调查工具

> Hermes Agent 技能：被动式域名情报收集，无需 API Key

## 概述

该技能使用纯 Python 标准库和公开数据源进行域名情报收集。**零依赖、零 API 密钥**，开箱即用。

## 能力列表

| 功能 | 说明 |
|------|------|
| 🔍 子域名发现 | 通过 crt.sh 证书透明度日志查找子域名 |
| 🔒 SSL 证书检查 | 查看证书有效期、加密套件、SAN、TLS 版本 |
| 🌐 WHOIS 查询 | 支持 100+ TLD 的 WHOIS 信息查询 |
| 📡 DNS 记录 | A、AAAA、MX、NS、TXT、CNAME 记录查询 |
| ✅ 域名可用性 | 通过 DNS + WHOIS + SSL 综合判断 |
| 📊 批量分析 | 并行分析最多 20 个域名 |

## 使用方式

对 Agent 说类似以下的话：

```
查一下 example.com 的子域名
检查这个域名的 SSL 证书
查一下这个域名 whois 信息
批量检查这几个域名是否可用
```

## 文件结构

```
domain/
├── SKILL.md       # Hermes Agent 技能定义
├── README.md      # 本文件 · 使用说明
└── DESCRIPTION.md # 分类描述
```
