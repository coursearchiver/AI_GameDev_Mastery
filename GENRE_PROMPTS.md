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
