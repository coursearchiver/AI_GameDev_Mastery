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
