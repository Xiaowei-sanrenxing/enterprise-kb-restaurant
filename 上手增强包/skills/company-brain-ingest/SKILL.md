---
name: company-brain-ingest
description: >
  把新素材(SOP、话术、模板、案例、文档、复盘)归入已有的企业 AI 知识库(company-brain 建的库)。
  当用户说「把这份 SOP 入库」「这个话术归进知识库」「这份资料 ingest 到公司知识库」
  「新增了一份文档想进库」「把这个归到对应工作流」时触发。
  判断归哪条工作流 → 加 6 元数据 → 重组进 context → 更新 INDEX → 提示定版后同步。
allowed-tools: Bash Read Write Edit Glob Grep
---

# company-brain-ingest · 企业知识库喂料

> 把零散新素材,变成知识库里"带元数据、归对工作流、可被 agent 用"的上下文资产。
> 前提:已有 company-brain 建的库(有 AGENTS.md + 10-workflows + 90-governance)。

## 工作流(检测 → 讨论 → 执行)

### 1. 定位库 + 读懂素材
- 确认目标知识库路径(找有 AGENTS.md 的目录)。
- 读完要 ingest 的素材,理解它讲什么、给哪类任务用。

### 2. 判断归属(讨论,先不动手)
对照库的 `AGENTS.md` 任务路由表,判断这份素材属于:
- **某条工作流的 context 资产** → `10-workflows/<slug>/context/`
- **跨工作流复用的方法论/实体** → `20-knowledge/`
- **原始大文件(PPT/视频/客户对话)** → 不进库,在 `30-raw/原始素材索引.md` 登记索引
跟用户确认归属,再执行。

### 3. 重组入库(执行)
1. 在目标位置创建资产文件(文件名用中文业务名)。
2. **必带 6 元数据 frontmatter**:
   ```yaml
   ---
   asset: 〔资产名〕
   owner: 〔谁维护〕
   status: 草稿        # 新入库默认草稿,确认后改定版
   source: 〔来源〕
   permission: 公开/内部/受限   # 客户隐私=受限
   updated: 〔日期〕
   evals: ["〔验收问题〕"]
   ---
   ```
3. 正文重组为"agent 能直接用"的颗粒度(表格/清单/步骤,不是大段原文堆砌)。
4. 用 `[[wikilink]]` 链接相关已有资产。

### 4. 更新索引 + 提示
- 在 `INDEX.md` 添加这份资产的条目。
- 如该工作流还没任务卡引用它,提示更新 `_task-card.md` 的 Context 清单。
- 提示:定版后按 `90-governance/feishu-sync.md` 单向同步协作平台。

## 铁律
1. **先判归属再动手** —— 归错工作流 = agent 以后找不到
2. **必带 6 元数据** —— 没有 status/permission = 不是资产,是垃圾
3. **大文件不进库** —— 30-raw 索引引用
4. **受限数据标清楚** —— 客户隐私 permission: 受限,绝不外发
5. **新入库默认 `status: 草稿`** —— 用户确认后才 `定版`

## 关联
建库用 `company-brain`,体检用 `company-brain-audit`,规范见库内 `90-governance/` 和 company-brain skill 的 `references/methodology.md`。
