---
asset: 协作平台同步规则
owner: 〔知识库负责人〕
status: 定版
permission: 内部
updated: 2026-06-25
---

# 同步规则 · 本地车间 → 协作前台

> 解决"本地库 vs 协作平台库割裂、两头维护、不知哪个全"的痛。

## 核心原则:单向同步
```
本地知识库(生产车间)  ──单向同步──>  协作平台(飞书/Notion 等,前台)
  Coding Agent 编辑/定版            团队日常调用,只读为主
```
- **本地 = 唯一信息源(source of truth)**,所有编辑、定版在本地
- **协作平台 = 展示/协作镜像**,定版后同步过去
- **绝不双头维护**:要改回本地改完再同步

## 同步什么
- ✅ 只同步 `status: 定版` 且 `permission: 公开/内部` 的资产
- ❌ 草稿、🔴 受限、隐私 → 不同步

## 飞书 lark-cli 操作约定（如用飞书）
- space_id：`〔飞书 space_id，可选〕`
- 更新内容：`lark-cli docs +update --doc <obj_token> --mode overwrite --markdown "$(cat file.md)"`
- 建议:协作平台一级节点对齐本库工作流
