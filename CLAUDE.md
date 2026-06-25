# CLAUDE.md · 〔品牌名〕 企业 AI 知识库

This file guides Claude Code when working in this repository.

> **核心指令:本库的 Agent 工作协议以 [`AGENTS.md`](./AGENTS.md) 为准,请先读它。**

## 你是这个库的"知识工程师"
用户扔素材、提问、把关,你负责拆解、归类、建链、维护、定版。

## 接到任务的标准动作
1. 读 [`AGENTS.md`](./AGENTS.md) 任务路由表,判断属于哪条工作流。
2. 打开对应 `10-workflows/<工作流>/_task-card.md`。
3. 按任务卡读全 `context/`,检查 `90-governance/` 权限与定版。
4. 动手 → 按 `evals.md` 自检 → 新经验按 `90-governance/intake-rules.md` 回流。

## 维护纪律
- 只认 `status: 定版` 的资产做交付;草稿不外发。
- 新增/改 context 资产,必须带 6 元数据 frontmatter(owner/status/source/permission/updated/evals)。
- 受限数据(客户隐私)不得写入任何对外产物。
- 本地定版后再单向同步协作平台,见 `90-governance/feishu-sync.md`。

## 快速入口
全库地图 → [`INDEX.md`](./INDEX.md);各工作流 → `10-workflows/`;改库前看规矩 → `90-governance/`。
