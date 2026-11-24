> **双语版本 / Bilingual Edition (简体中文 + English)**  
> 中文优先帮助中国学生理解；保留英文原文、技术名称、命令与 URL，便于直接让 AI 编程代理执行。  
> **Language tip:** Ask your coding agent: “请用简体中文解释操作，但不要翻译代码、文件名和命令。”

# 各游戏类型示例提示词 / Game Genre Prompt Examples

**使用方法：** 请先让 AI 阅读 `MASTER_PROMPT_cn.md`，然后挑选一种类型，把下面的中文示例粘贴给它。所有示例都应先输出一页 GDD 让学生审批，而不是直接开发。

| 类型 / Genre | 可直接复制的中文示例 / Chinese example |
|---|---|
| 2D 平台跳跃 / Platformer | 帮我设计一个像素风小青蛙在钟楼里墙跳的平台游戏。只做一关、三个检查点、90 秒挑战；先写一页 GDD。 |
| 类银河恶魔城 / Metroidvania | 设计机械鲸鱼体内的小型冒险关卡，获取一个新能力后能开启捷径。最初只做一个互联区域。 |
| 肉鸽 / Roguelike | 设计俯视角 2D 肉鸽：一局五分钟、三种敌人、两把武器、一次升级选择。先解释玩法循环。 |
| 弹幕射击 / Bullet Hell | 做一款 2D 太空射击小游戏：一个 Boss、容易看清的弹幕、三条命和积分系统。 |
| 解谜 / Puzzle | 设计魔法茶馆材料分类游戏：六个短关卡，提示清楚，结局有成就感。 |
| 视觉小说 / Visual Novel | 设计含三个角色、五个短场景、两个结局的悬疑故事；给出分支流程图和 GDD。 |
| 3D 铁拳格斗 / 3D Fighter | 以 clintcan/3d-fighter 作为首选基础，先做两个原创角色和一个场地的 1v1。优先保留原有回滚；是否用 Netfox 或 Rollback in a Box 由我决定。 |
| 2D 格斗 / 2D Fighting | 做两个角色的本地双人格斗原型，支持轻重攻击、防御和倒计时。 |
| 3D 动漫 / Anime RPG | 设计只有一个角色、一个竞技场、一个敌人的小型动漫动作 RPG；先阅读动漫专用提示词，并说明 Charakuru 和 Ensō 的成本与许可证。 |
| 3D 平台 / 3D Platformer | 做上发条玩具爬上巨大书桌的低模游戏：一个房间、移动平台、可收集齿轮和终点。 |
| 3D 恐怖 / Horror | 做复古 PS1 风格地铁恐怖游戏：一个追逐者、三把钥匙、没有战斗、十五分钟流程。 |
| 3D 派对 / Party | 设计原创四人扔箱子派对游戏；先做单机一个竞技场、机器人对手、胜负结算和重赛，联机第二阶段再评估。 |
| FPS 射击 / FPS | 做复古竞技场 FPS：一张地图、两把武器、三个机器人和拾取物，先优化操作手感。 |
| 赛车 / Racing | 做低模卡丁车计时赛：一条赛道、漂移加速、检查点和幽灵回放。 |
| 双人合作生存 / Co-op | 做双人合作生存原型：一间木屋、一个夜晚、可收集燃料和一个怪物。先讨论是否值得做 Steam 联机。 |
| 怪物狩猎与烹饪 / Monster Hunt | 做哥特风格狩猎与烹饪游戏；先只有一只怪、一场狩猎、一份食谱。 |
| RPG / Role Playing | 做俯视角村庄悬疑 RPG：一条任务线、两个 NPC、一次战斗和有意义的结局选择。 |
| 塔防 / Tower Defense | 做一条路线、三种塔、三类敌人、五波进攻的塔防小游戏。 |
| 潜行 / Stealth | 做快递员潜入博物馆的俯视角游戏；一关、警卫视野锥形区和固定巡逻路线。 |
| 农场经营 / Farming | 做温馨屋顶农场：种植、浇水、收获、出售，先做一个地块和七天日历。 |
| 体育 / Sports | 做 2v2 休闲躲避球，先本地双人和机器人，再独立评估 Netfox。 |
| 音乐节奏 / Rhythm | 用原创音乐做一首 60 秒、三轨道节奏小游戏，提供明确的判定与反馈。 |
| 魂类 / Soulslike | 使用 Cat’s Godot 4 Modular Souls-like Template 作为可选基础：翻滚、锁定、弹反和一个敌人；若 `.blend` 导入报错，经许可安装 Blender。 |
| 高机动空战斗 / Arena Fighter | 基于 clintcan/3d-fighter 构想空中冲刺、跑墙、可坍塌建筑。先用状态化破坏；额外确定性物理框架必须让我决定。 |

### 还没有创意？ / No idea yet?

```text
我从来没设计过游戏。请先问我喜欢哪类游戏、想要 2D 还是 3D、是否需要联机。推荐三个简单、能完成的小点子，解释每个点子的优点、难度和最小可玩版本。等我选择一个后，请写一页简体中文 GDD 并让我审核；在我输入 START DEVELOPMENT 前不要编程。
```

---

## Original English Prompts / 英文原版示例

# Game Genre Example Prompts

Use any of these after the [master prompt](MASTER_PROMPT.md).

Paste any of these **after the master prompt**. All examples begin with design/GDD approval, not immediate coding. Keep content original.

| Genre | Copy-ready example request |
|---|---|
| **2D Platformer** | “Design a one-level pixel-art platformer where a frog wall-jumps through a rainy clocktower. Include 3 checkpoints and a 90-second goal. Start with a GDD.” |
| **2D Metroidvania** | “Design a small 2D metroidvania set inside a mechanical whale. One ability unlocks a shortcut. Build only one interconnected area for the MVP.” |
| **2D Roguelike** | “Design a top-down 2D roguelike with a 5-minute run, 3 enemy types, 2 weapons and one upgrade choice. Show the loop and GDD.” |
| **Bullet Hell** | “Design a 2D space shooter with one boss, readable projectile patterns, 3 lives and score chasing. Make a controller-friendly MVP.” |
| **Puzzle / Cozy** | “Design a cozy 2D café puzzle about sorting magical tea ingredients. 6 short levels, clear hints and a satisfying finish.” |
| **Visual Novel** | “Design a branching mystery visual novel with 3 characters, 5 short scenes and 2 endings. Consider Novel-to-Game skills; present a narrative flowchart and GDD.” |
| **3D Fighting / Tekken-style** | “Design an original 1v1 3D fighter using https://github.com/clintcan/3d-fighter as the preferred base. Reuse its built-in rollback and deterministic 60 Hz combat; do not automatically install Netfox. Start with 2 fighters, one stage and local versus, then assess Steam lobbies through GodotSteam separately. Verify Godot 4.7 compatibility, run tests, review asset licenses, and show me a one-page GDD before coding.” |
| **2D Fighting** | “Design a simple local two-player fighting prototype with 2 original characters, light/heavy attacks, block and a round timer. Separate game logic from animations.” |
| **Anime / Gacha RPG** | “Design a small original 3D anime action RPG with one character, one arena, one enemy, and a short quest. Read `SPECIALIZED_3D_ANIME_PROMPT.md`; evaluate Charakuru for VRM character creation and Ensō for scenery. Show a one-page GDD and tool/licensing costs before any downloads.” |
| **3D Platformer** | “Design a low-poly 3D platformer about a wind-up toy climbing a giant desk. One room, moving platforms, collectible gears and a goal bell.” |
| **3D Horror** | “Design a PS1-style first-person horror game in a deserted subway. One pursuer, 3 keys, no combat and a 15-minute level. Show the full game flow.” |
| **3D Party Game** | “Design an original 4-player crate-throwing party game inspired by classic PS1 minigames. Start offline with one arena, bots, win/lose, results and rematch; discuss Netfox online play as phase 2.” |
| **3D FPS** | “Design a compact retro arena shooter with one map, 2 weapons, 3 bots and pickups. Responsive movement comes before visual polish.” |
| **3D Racing** | “Design a low-poly kart time-trial game with one loop track, drift boost, checkpoints and a ghost replay. Test handling before online racing.” |
| **Co-op Survival** | “Design a 2-player co-op survival prototype with one cabin, one night, collectible fuel and one monster. Ask whether online or Steam lobbies are worth the complexity.” |
| **Monster Hunt + Cooking** | “Design an original gothic monster-hunting-and-cooking game. Start with one monster, one hunt, ingredient collection and one recipe. Use a Game Soul and a one-page GDD; defer large-scale co-op.” |
| **RPG** | “Design a small top-down RPG village mystery with one quest chain, two NPCs, one combat encounter and a meaningful final choice.” |
| **Tower Defense / Strategy** | “Design a tower defense game with one lane, 3 towers, 3 enemy types and 5 waves. Prioritize readable information and balance.” |
| **Stealth** | “Design a top-down stealth game where a courier sneaks through one museum. Guards have vision cones and predictable patrols; start with one level.” |
| **Farming / Sim** | “Design a cozy 3D rooftop garden game with plant–water–harvest–sell gameplay and a seven-day calendar. One playable plot first.” |
| **Sports** | “Design a simple 2v2 arcade dodgeball game. Begin with local play and bots; assess Netfox rollback suitability separately.” |
| **Rhythm** | “Design a 2D original-music rhythm game with one 60-second song, 3 note lanes, clear timing windows and performance feedback.” |

### Example: optional Steam multiplayer expansion

```text
The approved offline arena prototype works. Please explain costs and extra testing for Steam multiplayer. If I approve, read ALL Netfox documentation, install the GodotSteam GDExtension (not just a demo clone), review AtomicSponge/godot-multiplayer-example for reusable code, and propose a multiplayer implementation/testing plan before changing the game. Do not promise automatic physics determinism or host migration.
```

### Example: narrative + a provided game reference

```text
I have attached legally obtained reference footage and design notes from a classic party game. Study only observable mechanics, input feel, scoring and UI flow; use REA for deeper analysis only if justified and technically supported. Design an original game with original characters and art. Create the one-page GDD and Mermaid menu flow for review.
```

## 3D Soulslike / heavy character-action combat

Starter: https://github.com/catprisbrey/Cats-Godot4-Modular-Souls-like-Template

```text
I am a complete beginner. Design an original small 3D Soulslike with dodge, lock-on, parry, one enemy, and one boss arena. Prefer Cat's Godot 4 Modular Souls-like Template as the project foundation. Read its README; verify current version/license and test that it imports before adding new mechanics. If Godot asks for Blender for .blend imports, install and configure Blender with my permission. Write the one-page GDD in plain English and get my approval before coding.
```

Do not claim this template provides full CAG combos or multiplayer without implementing and testing them.

## No game idea yet?

```text
I don't know what kind of game to make. Ask what games I like; propose 3 tiny ideas for my skill level; explain each in simple words; then write a one-page GDD for the idea I choose. Do not start coding until I approve.
```

**Example shared teaching chat:** https://chatgpt.com/share/6b047749-5fcc-83ec-822e-3a76af146a33

### Specialized anime art workflow

```text
I want an original 3D anime / VTuber / gacha-style game. Follow MASTER_PROMPT.md and SPECIALIZED_3D_ANIME_PROMPT.md. Help me choose a simple idea, then propose a one-page GDD. Use Charakuru for a character and Ensō for an environment only after verifying license, current releases and required tools; check the Godot imports before building more content. Wait for START DEVELOPMENT.
```


## Advanced 3D arena fighter (Dissidia-style)

```text
Help me design an original aerial arena fighter with wall-running, air dashes, knockback, and buildings that can collapse and block paths. Start from https://github.com/clintcan/3d-fighter and keep its existing rollback if it meets the design. Prototype simple state-based destruction first; cosmetic debris does not need deterministic physics. DO NOT install Netfox or Rollback in a Box automatically. Only if a specific limitation is demonstrated, explain their tradeoffs in plain English and let ME choose whether to keep the existing rollback, use Netfox, or investigate Rollback in a Box for gameplay-critical physics. Do not make that decision for me. First prepare a one-page GDD and wait for my approval and START DEVELOPMENT.
```
