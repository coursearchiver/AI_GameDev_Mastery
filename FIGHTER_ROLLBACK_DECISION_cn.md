> **双语版本 / Bilingual Edition (简体中文 + English)**  
> 中文优先帮助中国学生理解；保留英文原文、技术名称、命令与 URL，便于直接让 AI 编程代理执行。  
> **Language tip:** Ask your coding agent: “请用简体中文解释操作，但不要翻译代码、文件名和命令。”

# 格斗游戏：是否需要额外回滚框架？ / Fighter Rollback Decision

**默认选择 / Default:** 使用 [clintcan/3d-fighter](https://github.com/clintcan/3d-fighter) 现有的确定性 60 Hz 战斗与回滚。**不要默认安装 Netfox 或 Rollback in a Box**。

| 你的需求 / Your need | 建议 / Recommendation |
|---|---|
| 1v1 铁拳式格斗、普通击打/连段 | 先保留原项目回滚 / Keep built-in rollback |
| 2–4 人、高机动空战斗、跑墙 | 先用原系统做小型测试 / Prototype before replacing netcode |
| 建筑只有完整、损坏、坍塌三种状态 | 同步状态和碰撞，无须完整物理回滚 / State-based destruction |
| 大块碎石会移动、互撞并堵路 | 可评估 Rollback in a Box 的确定性 3D 物理 / Consider deterministic rigid-body simulation |
| Steam 房间、邀请、P2P | 单独评估 GodotSteam / Separate transport decision |

**决定权属于用户 / User decides:** AI 只能先分析现有方案的限制，再介绍 Netfox 和 Rollback in a Box 的好处、缺点及额外工作量。没有用户明确批准，不得增加或更换回滚框架，也不得同时运行两个回滚系统。

---

## Original English Guide / 英文原版说明

# Fighter rollback: keep it simple

Default: [clintcan/3d-fighter](https://github.com/clintcan/3d-fighter) with its built-in rollback. No additional rollback package by default.

| Situation | Approach |
|---|---|
| Standard 1v1 fighting | Keep the fighter's existing rollback. |
| Wall-running, launchers, air dashes | Implement as deterministic gameplay states first. |
| Buildings collapse and block paths | Use synchronized pre-fractured / intact–damaged–collapsed states first. |
| Cosmetic dust and debris | Visual-only effects; no gameplay-critical rigid-body simulation. |
| Real colliding, movable debris changes gameplay | **Ask the user** whether to evaluate [Rollback in a Box](https://github.com/pdaddyo/rollback-in-a-box). |
| A verified networking feature is missing | **Ask the user** whether to evaluate [Netfox](https://github.com/foxssake/netfox). |
| Steam lobbies/invites | Optional [GodotSteam](https://godotengine.org/asset-library/asset/2445) transport/lobby integration; not a rollback replacement. |

**User approval is mandatory before selecting or migrating to either optional framework.** Do not install both. Preserve one authoritative simulation and rollback coordinator. Verify with automated replay/state comparisons, multi-client tests and latency/loss simulation. Reassess 2–4 player support instead of assuming 1v1 code scales unchanged.

## Starter prompt

> Use clintcan/3d-fighter as my starting point. Keep its current rollback unless we prove it cannot satisfy my approved game. Start with a small one-arena, two-character playable prototype. Explain any reason to consider Netfox or Rollback in a Box, but let me make that decision. Do not add either automatically. Create a one-page GDD for approval before development.
