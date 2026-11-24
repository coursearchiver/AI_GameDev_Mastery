> **双语版本 / Bilingual Edition (简体中文 + English)**  
> 中文优先帮助中国学生理解；保留英文原文、技术名称、命令与 URL，便于直接让 AI 编程代理执行。  
> **Language tip:** Ask your coding agent: “请用简体中文解释操作，但不要翻译代码、文件名和命令。”

# 专用 3D 动漫游戏开发流程 / Specialized 3D Anime Pipeline

**适合 / For:** 虚拟主播（VTuber）、VRM 角色、二次元动作 RPG、抽卡游戏风格、动漫视觉小说。

- **角色 / Characters:** [Charakuru](https://github.com/nanocle/Charakuru) 可作为从原创角色插画到 VRM 的可选工具；务必阅读 Release 安装方法、依赖和特殊再发行许可。
- **场景 / Scenes:** [Ensō Engine](https://enso.mix3ddesign.com) 用于 Blender 风格化非写实场景与卡通材质；不要假定 Blender 的每种着色器自动在 Godot 工作。
- **运行游戏 / Runtime:** 游戏还是由 Summer Engine / Godot 负责。导出 GLB/VRM 后验证骨骼、表情、动作、材质与性能。
- **基础要求 / Baseline:** 保留主提示词规定的 Summer 安装、GDD 审核、Git、AGENTS.md、项目目录和可选 Netfox/GodotSteam。

## 中文可复制提示词 / Copy-ready Chinese Prompt

```text
我想用 Summer Engine 做一款原创小型 3D 动漫风游戏。请先阅读 MASTER_PROMPT_cn.md 和本文件。
优先以 Charakuru 研究原创角色的 VRM 骨骼/面部表情生成，以 Ensō 研究动漫风场景；先核查许可证、运行要求、付费项以及导入 Godot 的兼容性。
先做一个角色加一个房间的技术测试方案，不要先安装大量工具，也不要盲目搬运别人的动漫素材。
用简体中文帮我写一页 GDD，让我审核。我明确说 START DEVELOPMENT 之前，不得开发游戏项目。
```

---

## Original English Specialized Prompt / 英文原版专用提示词

# Specialized 3D Anime / VTuber / Gacha Game Pipeline

> **Optional add-on to [`MASTER_PROMPT.md`](MASTER_PROMPT.md).** Use this only when the approved game calls for anime-style 3D humans, VRM avatars, or stylized anime environments. It does not replace the general game-development process, GDD approval, Netfox, Git, or `AGENTS.md`.

## Copy-ready agent prompt

```text
I want to create an original 3D anime-style game with Godot or Summer Engine.

First read and follow the main MASTER_PROMPT.md in this repository. Apply this specialized anime pipeline only where it helps my approved GDD.

CHARACTERS — CHARAKURU
https://github.com/nanocle/Charakuru
https://github.com/nanocle/Charakuru/releases
Read its README, getting-started guide, AGENTS.md (in the actual toolkit), license, and asset-license terms. Charakuru is a source-available character-creation toolkit, not an ordinary permissive open-source dependency. The usable kit is in the dedicated Releases ZIP; the automatic GitHub "Source code" ZIP does NOT contain it. Follow the documented workflow for turning an original full-body illustration into a rigged VRM character. Configure required tools only with approval, including Blender, Blender MCP, VRM Add-on, and any image/Tripo services. Check fees and account access before any cloud use.

SCENES / ANIME ART — ENSO ENGINE
https://enso.mix3ddesign.com/
https://github.com/Mix3DDesign/enso-engine
Read the exact version's documentation and licensing. Ensō is a Blender-based anime/NPR authoring environment, not the Godot game runtime. Use it for original environments, cel-shaded presentation, outlines and materials where suitable. Investigate its Godot transfer/link/export workflow; do not assume every Blender shader, reflection or post effect transfers intact. Verify output in the installed Godot/Summer version.

RUNTIME — GODOT / SUMMER ENGINE
Keep the actual game in Godot/Summer Engine. Import permitted VRM/GLB and other meshes using compatible importers. Validate model scale, rig orientation, facial expressions/blendshapes, animation playback, materials, lighting, collisions, draw calls and frame rate. Recreate unsupported Blender-only effects as runtime Godot shaders where necessary. Keep asset sources and licenses documented.

PRIORITIES
This is an optional genre-specific override for anime characters/environments. The main default remains Summer built-in assets → KILN → Godogen → Blender/Tripo. Don't install every tool; run a one-character + one-room import test before building a large project.

APPROVAL
Before installing optional tools or changing project files, help me choose an original character art direction, create a one-page GDD, show any required costs or licenses, and wait for my explicit approval and START DEVELOPMENT.
```

## Beginners: what is each tool for?

| Tool | What it does | What it **doesn't** do automatically |
|---|---|---|
| **Charakuru** | Helps turn a character illustration into a rigged VRM avatar | It is not a complete game, and its kit is not licensed as a generic open-source package |
| **Ensō Engine** | Helps create stylized anime environments and NPR look in Blender | It does not automatically guarantee identical shaders inside Godot |
| **Godot / Summer Engine** | Runs the actual game, controls, combat, menus, and optional multiplayer | Does not automatically import every Blender feature |

## Small first test

1. Sketch or supply **one original full-body character** and a visual reference for **one tiny environment**.
2. Ask the agent to verify current Charakuru release, terms, required accounts/software, and Ensō download requirements.
3. Generate and import **one** rigged character; confirm facial expressions and one animation play correctly.
4. Create **one** stylized environment in Ensō; bring it into Godot and compare materials/lighting.
5. Only then choose whether this workflow is worth using for your game.

## Important licensing and costs

- **Charakuru:** source-available license with specific terms; do not redistribute the toolkit or package it into your public teaching repository. Check `LICENSE`, `ASSET_LICENSE.md`, third-party notices and commercial conditions. The actual toolkit comes from the dedicated GitHub Release asset.
- **Ensō:** confirm its current Blender-fork license and the licensing of bundled or separately sold add-ons. Do not assume everything on the product site is freely redistributable.
- **Tripo and other services:** may require authentication or payment. Ask before upload or credit consumption.
- **Imported models:** document source and license; original game characters are preferable to reproducing copyrighted gacha characters.

## Sources

- [Charakuru README](https://github.com/nanocle/Charakuru/blob/main/README.md) · [Getting started](https://github.com/nanocle/Charakuru/blob/main/docs/getting-started.md) · [License](https://github.com/nanocle/Charakuru/blob/main/LICENSE) · [Releases](https://github.com/nanocle/Charakuru/releases)
- [Ensō Engine official website](https://enso.mix3ddesign.com/) · [Source repository](https://github.com/Mix3DDesign/enso-engine)
