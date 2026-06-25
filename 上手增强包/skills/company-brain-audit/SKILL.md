---
name: company-brain-audit
description: >
  给企业 AI 知识库(company-brain 建的库)做治理体检:查定版冲突、权限/隐私风险、孤儿资产、
  元数据缺失、INDEX 不一致、工作流缺任务卡/evals。
  当用户说「体检知识库」「audit 公司知识库」「检查知识库」「知识库健康检查」
  「有没有定版冲突」「检查权限/隐私」「知识库该清理了」时触发。
  扫描 → 分 Errors/Warnings/Info 三级报告 → 经确认后修复。
allowed-tools: Bash Read Write Edit Glob Grep
---

# company-brain-audit · 企业知识库治理体检

> 企业库会随时间腐化:多版本打架、隐私泄漏风险、孤儿资产、元数据缺失。定期体检保持健康。
> 前提:已有 company-brain 建的库。

## 工作流(扫描 → 分级 → 修复)

### 1. 定位库
找有 AGENTS.md 的知识库根目录。

### 2. 八项检查(用 Bash + 读文件)

| # | 检查 | 怎么查 | 级别 |
|---|---|---|---|
| 1 | **定版冲突** | 同主题多文件,有没有恰好一个 `status: 定版` | 🔴 Error |
| 2 | **权限/隐私风险** | `permission: 受限` 的内容有没有被引用进对外产物;客户姓名/手机号/微信号有没有出现在 公开/内部 资产 | 🔴 Error |
| 3 | **元数据缺失** | context 资产缺 6 元数据(owner/status/source/permission/updated/evals) | 🟡 Warning |
| 4 | **孤儿资产** | 没有任何 `[[wikilink]]` 指向、也不在任何任务卡 Context 里的资产 | 🟡 Warning |
| 5 | **工作流不完整** | `10-workflows/<slug>/` 缺 `_task-card.md` 或 `evals.md` | 🟡 Warning |
| 6 | **INDEX 不一致** | INDEX 列的资产文件不存在 / 存在的资产没进 INDEX | 🟡 Warning |
| 7 | **破损链接** | `[[X]]` 指向的资产找不到 | 🟡 Warning |
| 8 | **过时资产** | `status: 待更新`,或 `updated` 距今过久的高频资产 | 🔵 Info |

参考命令:
```bash
# 缺 status 的 context 资产
for f in $(find 10-workflows -path '*/context/*.md'); do grep -q '^status:' "$f" || echo "缺元数据: $f"; done
# 破损 wikilink(粗查)
grep -rho '\[\[[^]]*\]\]' . | sort -u
# 受限内容是否泄漏(查手机号样式)
grep -rn '1[3-9][0-9]\{9\}' --include=*.md . | grep -v permission
```

### 3. 分级报告
按 **Errors(必须修) / Warnings(应修) / Info(可修)** 输出,每项写清:
- **What**(什么问题)· **Where**(哪个文件)· **Fix**(怎么修)

### 4. 修复(经用户确认)
问"要我修哪些?",然后:定版冲突→帮定一个版其余归档;元数据缺失→补 frontmatter;孤儿→建链接或归档;破损链接→修正或建缺失资产。修完汇报改动。

## 铁律
1. **隐私泄漏是最高优先级** —— 受限数据出现在对外/内部资产 = Error,立即处理
2. **定版冲突优先修** —— agent 拿错版本去交付后果严重
3. **修复前先报告 + 确认** —— 不擅自大改

## 关联
建库 `company-brain`,喂料 `company-brain-ingest`,治理规范见库内 `90-governance/`。
