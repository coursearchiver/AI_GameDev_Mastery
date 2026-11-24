> **双语版本 / Bilingual Edition (简体中文 + English)**  
> 中文优先帮助中国学生理解；保留英文原文、技术名称、命令与 URL，便于直接让 AI 编程代理执行。  
> **Language tip:** Ask your coding agent: “请用简体中文解释操作，但不要翻译代码、文件名和命令。”

# 一页式 GDD 模板 / One-Page Game Design Document

**GDD 是什么？** Game Design Document（游戏设计文档）就是一张游戏开发计划表。零基础学生不需要自己填写，可以直接把喜欢的游戏、玩法或 MP4 录像给 AI，让 AI 先起草，再由学生审阅。

```markdown
# [游戏名称 / Game Title] — 一页式 GDD / One-Page GDD

**一句话概括 / Pitch：** 这是什么游戏？谁来玩？
**游戏类型与平台 / Genre & Platform：** 2D/3D，Windows/Steam Deck，单人或多人？
**核心循环 / Core Loop：** 玩家做什么 → 得到什么 → 再做什么？
**控制与规则 / Controls & Rules：** 移动/跳跃/攻击/交互；怎么赢、怎么输？
**模式与联机 / Modes & Multiplayer：** 离线、本地联机、网络联机或 Steam？
**游戏流程 / Game Flow：** 主菜单 → 游戏 → 胜负结果 → 重试/返回。
**美术与音乐 / Art & Audio：** 像素、PS1 低模、动漫等；主要素材有哪些？
**最小可玩版 / MVP：** 先做一张地图/一位角色/一个明确目标。
**风险与依赖 / Risks：** 哪些功能复杂或需要额外安装/付费？
**审核状态 / Approval：** 等我修改与确认；输入 START DEVELOPMENT 后才开工。
```

**可以直接对 AI 说：**「请根据我的游戏点子填写上面的 GDD，用通俗简体中文说明，我不懂专业术语。加上一个 Mermaid 游戏菜单流程图。先让我审核。」

---

## Original English Template / 英文原版模板

# One-Page GDD Template

Copy and fill this out. An agent should not start development until you approve it and say **START DEVELOPMENT**.

```markdown
# [GAME TITLE] — One-Page GDD

**One sentence:** A [genre] game where the player [action] to [goal].
**Audience / Platform:** [who plays? Windows, Steam Deck, etc.]
**Inspiration:** [references, not copyrighted assets]

## Core loop
[Start] → [Act] → [Reward / consequence] → [Try again]

## Controls & rules
- Move / interact / attack: [...] 
- Win when: [...] | Lose when: [...]
- Camera + viewpoint: [...]

## Modes and multiplayer
[Single-player first? Local / LAN / Netfox / Steam? Number of players?]

## Game flow
[Title → Play → Level → Win/Lose → Retry / Menu]

## Art and audio
[2D or 3D? palette? 3 asset needs? simple audio mood?]

## Tiny playable milestone
[ONE level, ONE main mechanic, ONE win/lose rule]

## Risks / dependencies
[Paid credits? multiplayer? local generator GPU? licenses?]

**Approval:** [ ] I reviewed this GDD. I will say START DEVELOPMENT separately.
```
