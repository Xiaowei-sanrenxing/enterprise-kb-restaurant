#!/bin/bash
# 一键安装「企业知识库」两个维护技能（喂料 ingest + 体检 audit）
# 适用：你用 Claude Code（命令行 AI 工具）。双击本文件即可安装。
# 不用 Claude Code（用飞书/网页 AI）的，不用装这个，直接看《话术速查卡.md》。

set -e
cd "$(dirname "$0")"

DEST="$HOME/.claude/skills"

echo "================================================"
echo "  企业知识库 · 维护技能一键安装"
echo "================================================"
echo ""

# 1. 检测是否装了 Claude Code（看 ~/.claude 在不在）
if [ ! -d "$HOME/.claude" ]; then
  echo "⚠️  没找到 ~/.claude 目录——你可能还没装 Claude Code。"
  echo "    这两个技能只在 Claude Code 里能用。"
  echo "    如果你用的是飞书 / 网页版 AI，不用装技能，"
  echo "    直接照《话术速查卡.md》说话就行。"
  echo ""
  read -p "    仍要继续安装吗？(y/N) " yn
  case "$yn" in [Yy]*) ;; *) echo "已取消。"; exit 0;; esac
fi

# 2. 拷贝两个 skill 到全局 skills 目录
mkdir -p "$DEST"
cp -R "skills/company-brain-ingest" "$DEST/"
cp -R "skills/company-brain-audit"  "$DEST/"

echo "✅ 安装完成！两个技能已装到："
echo "   $DEST/company-brain-ingest"
echo "   $DEST/company-brain-audit"
echo ""
echo "📌 怎么确认装好了？"
echo "   开一个新的 Claude Code 会话，输入斜杠 /company-brain"
echo "   如果能看到 ingest / audit 跳出来，就成了。"
echo ""
echo "📌 以后怎么用？（不用纠结怎么措辞，敲斜杠点名就行）"
echo "   喂新料入库 → 输入  /company-brain-ingest  再把文件丢进去"
echo "   给库做体检 → 输入  /company-brain-audit"
echo ""
echo "（其余日常用法，见同目录《话术速查卡.md》）"
echo "================================================"
