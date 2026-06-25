#!/usr/bin/env python3
"""把知识库打包成可喂给任意 AI 的上下文文件，解决"谁读库"断点。

用法: python3 core/scaffold/pack_context.py <库目录>
产出: <库>/_上下文包/
  - 全库上下文.md         想让 AI 通览整个库就上传它
  - 工作流-<slug>.md      只问某条线的事，上传对应这个，更小更精准
  - pack_context.py       带一份自己，方便客户填料后自助刷新
排除：受限资产、_草稿区、_archive（只打包可安全喂给 AI 的内容）。
compose 会自动调用；客户填了新资料后也可单独重跑刷新。
"""
import os, sys, glob, re, shutil


def _read(p):
    return open(p, encoding="utf-8").read()


def _safe(t):
    m = re.search(r'^permission:\s*(.+)$', t, re.M)
    return not (m and "受限" in m.group(1))


def _intro(company, industry):
    return ("> 【使用说明 · 先读这段】\n"
            "> 下面是「%s · %s 企业知识库」的全部上下文。**你现在是这个库的 AI 助手。**\n"
            "> 接到我的任务时：① 按下方『任务路由表』判断属于哪条工作流 → ② 用那条工作流的资料和红线来回答 "
            "→ ③ 不确定就说不确定，绝不编造、绝不越红线（尤其客户隐私与合规）。\n\n---\n\n" % (company, industry))


def _workflow_blocks(kb):
    blocks = {}
    for wf in sorted(glob.glob(os.path.join(kb, "10-workflows", "*"))):
        if not os.path.isdir(wf):
            continue
        slug = os.path.basename(wf)
        parts = []
        for fn in ["_task-card.md", "sop.md", "evals.md"]:
            f = os.path.join(wf, fn)
            if os.path.exists(f):
                parts.append("## [%s] %s\n\n%s" % (slug, fn, _read(f)))
        for c in sorted(glob.glob(os.path.join(wf, "context", "*.md"))):
            t = _read(c)
            if _safe(t):
                parts.append("## [%s] context/%s\n\n%s" % (slug, os.path.basename(c), t))
        blocks[slug] = "\n\n---\n\n".join(parts)
    return blocks


def pack(kb, company=None, industry=None):
    kb = kb.rstrip("/")
    company = company or "本公司"
    industry = industry or "企业"
    outdir = os.path.join(kb, "_上下文包")
    os.makedirs(outdir, exist_ok=True)

    af = os.path.join(kb, "AGENTS.md")
    agents = _read(af) if os.path.exists(af) else ""
    blocks = _workflow_blocks(kb)
    gov = []
    for g in ["intake-rules.md", "permissions.md", "行业合规默认.md"]:
        f = os.path.join(kb, "90-governance", g)
        if os.path.exists(f):
            gov.append("## 治理 · %s\n\n%s" % (g, _read(f)))
    govtext = "\n\n".join(gov)

    # 全库包
    full = (_intro(company, industry)
            + "# 一、Agent 总入口（任务路由）\n\n" + agents
            + "\n\n# 二、各工作流详情\n\n" + "\n\n---\n\n".join(blocks.values())
            + "\n\n# 三、治理与红线\n\n" + govtext)
    open(os.path.join(outdir, "全库上下文.md"), "w", encoding="utf-8").write(full)

    # 每工作流包
    for slug, body in blocks.items():
        one = (_intro(company, industry)
               + "# Agent 总入口（任务路由）\n\n" + agents
               + "\n\n# 工作流：%s\n\n" % slug + body
               + "\n\n# 治理与红线\n\n" + govtext)
        open(os.path.join(outdir, "工作流-%s.md" % slug), "w", encoding="utf-8").write(one)

    # 带一份自己，方便客户填料后自助刷新
    try:
        shutil.copy(os.path.abspath(__file__), os.path.join(outdir, "pack_context.py"))
    except Exception:
        pass

    # 说明
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write(
        "# 📦 上下文包 · 把库一键喂给任意 AI\n\n"
        "- `全库上下文.md` — 想让 AI 通览整个库，上传这个\n"
        "- `工作流-<名>.md`（%d 个）— 只问某条线的事，上传对应这个，更小更精准\n\n"
        "**怎么用** → 见库根目录《谁读库指引.md》。\n"
        "**填了新资料想刷新** → 在库根目录跑：`python3 _上下文包/pack_context.py .`\n" % len(blocks))
    return outdir


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 pack_context.py <库目录>")
        sys.exit(1)
    print("✅ 上下文包已生成:", pack(sys.argv[1]))
