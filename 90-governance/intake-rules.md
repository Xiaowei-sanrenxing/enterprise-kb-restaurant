---
asset: 内容准入规则
owner: 〔知识库负责人〕
status: 定版
permission: 内部
updated: 2026-06-25
---

# 准入规则 · 什么值得入库

> 知识库的敌人不是"文件太少",是"垃圾太多"。入库前过这张清单。

## ✅ 该入库（升级为 context 资产）
- 反复被用到的(话术、SOP、模板、方法论)
- 带真实数据/案例的
- 会被多条工作流复用的(→ 放 20-knowledge)
- 踩坑教训和复盘结论(喂自我进化)

## ❌ 不该入库（留 30-raw 或丢弃）
- 一次性、不复用的临时文件
- 未验证、来源不明的内容
- 大二进制文件(PPT/视频/图片)→ 留原地,30-raw 索引

## 入库标准动作
1. 判断归哪条工作流 / 还是 20-knowledge 共享
2. 写 6 元数据 frontmatter(owner/status/source/permission/updated/evals)
3. 用 `[[wikilink]]` 链接相关资产
4. 更新 `INDEX.md`
5. 定版后按 `feishu-sync.md` 同步协作平台
