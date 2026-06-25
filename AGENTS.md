# AGENTS.md · 〔品牌名〕 企业 AI 知识库 · Agent 总入口

> ⚠️ 这不是"文件地图",这是"可执行指令"。
> 任何 agent 接到任务,**先读这一页**,再按指引去对应工作流。

## 一、这个库是什么
〔品牌名〕 的组织上下文基础设施——给一群 agent 用的执行底座,不是文档中心。
衡量标准:agent 能不能带着正确上下文,把一件真实业务做对。
**组织主轴 = 工作流,不是部门。** 见 `10-workflows/`。

## 二、Agent 工作协议
1. 判断任务属于哪条工作流(对照下表)。
2. 打开那条工作流的 `_task-card.md`(目标/上下文/指令/工具/权限/验收)。
3. 按任务卡 Context 清单读全 `context/`,再动手。
4. 动手前检查权限(`90-governance/permissions.md`)和定版(只用 `status: 定版`,见 `90-governance/lifecycle.md`)。
5. 完成后对照 `evals.md` 自检。
6. 新经验按 `90-governance/intake-rules.md` 回流入库。

## 三、任务路由表
| 你接到的任务长这样 | 去这条工作流 | 先读这张卡 |
|---|---|---|
| 〔拓店选址筹建 相关任务〕 | `site-expansion` | `10-workflows/site-expansion/_task-card.md` |
| 〔供应链与采购 相关任务〕 | `supply-chain` | `10-workflows/supply-chain/_task-card.md` |
| 〔门店运营 相关任务〕 | `store-operation` | `10-workflows/store-operation/_task-card.md` |
| 〔会员与复购 相关任务〕 | `member-repurchase` | `10-workflows/member-repurchase/_task-card.md` |
| 〔连锁标准化与督导 相关任务〕 | `chain-standardization` | `10-workflows/chain-standardization/_task-card.md` |
| 跨工作流的方法论/实体 | (共享知识,非工作流) | `20-knowledge/` |

## 四、目录主轴
```
00-org/         DRI 责任地图 + 黑话词典
10-workflows/   ★主轴:工作流(每条=任务卡+context+sop+evals)
20-knowledge/   跨工作流复用的方法论/实体
30-raw/         原始大文件索引(不复制)
90-governance/  准入/定版/权限/同步
```

## 五、工具约定
- 本地库 = 知识生产车间;协作平台(飞书等) = 前台,定版后单向同步(见 `90-governance/feishu-sync.md`)。
- 原始大文件(PPT/视频/图片)留原地,`30-raw/` 仅索引引用。

## 六、一句话总纲
> 不要翻箱倒柜。判断任务属于哪条工作流 → 读那张任务卡 → 带全上下文 → 按 evals 验收。
> 目标不是"找到文件",是"带着正确上下文把事做对"。
