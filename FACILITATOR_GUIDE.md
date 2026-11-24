# Workshop Facilitator Guide

**Session:** Vibe-Code Your First Game (60 minutes)  
**Audience:** Students and complete beginners  
**Visual approach:** Original GBA/32-bit-inspired pixel-art teaching deck; editable PowerPoint text.

## Before class

- Install/test Summer Engine or standard Godot on a classroom PC, along with a local coding agent and Git.
- Check sign-in, network access, model limits, subscriptions/credits, and permissions before involving students.
- Prepare a working **offline 2D template**, a completed one-page GDD, and an example Git checkpoint as a fallback.
- Keep a local copy of the PowerPoint: online services, model availability, and plugin versions can change.
- Optional: bring an MP4 gameplay sample (one minute, legally usable) to demonstrate observation vs copying.

## Timing and slide walkthrough

| Slides | Minutes | What to demonstrate |
|---|---:|---|
| 1–4 | 0–8 | Define vibe coding; show the idea → GDD → build → test loop. |
| 5–8 | 8–18 | Contrast agents with browser chat; discuss Summer/Godot installation and templates. |
| 9–12 | 18–28 | Show a video reference; turn a one-line pitch into a GDD; require approval. |
| 13–18 | 28–38 | Asset-tool priorities, prompt recipe, two tiny examples, genre choices and game flow. |
| 19–22 | 38–47 | Git, AGENTS.md, folder structure; explain why online/Steam multiplayer is optional. |
| 23–26 | 47–60 | One reproducible bug report, quality checks, student challenge and wrap-up. |

## Live demonstration (adapt to your equipment)

1. Display a one-page GDD for an original 2D star-collection game.
2. Have the students review the win condition and suggest one small change.
3. In the connected **local coding agent**, type `START DEVELOPMENT` after approving the GDD.
4. Ask for character movement and star collection first, then run the actual project.
5. Describe one observed bug, ask the agent to reproduce/test, and commit the fix.
6. If live generation is blocked by account credits or dependency installation, demonstrate the same steps using the preinstalled fallback project.

## Participation / assessment

Students can show three pieces of evidence even if they do not finish a game:

- A one-sentence pitch and approved one-page GDD.
- A running prototype *or* tested scene with a visible mechanic.
- A clear feedback prompt and a safe Git checkpoint or written change log.

## Important warnings

- Do not promise that one prompt creates a commercial-quality game.
- Do not enter or display passwords, access tokens, or payment details in slides or chat.
- For proprietary games, learn gameplay principles but create original code and assets.
- Do not require the entire multiplayer or local-asset stack for a one-hour beginner exercise.
- Confirm upstream repository licenses and Summer account/credit requirements before use.

## Resources

The complete copy-ready prompt, genre examples, official docs and tool links are in [README.md](README.md).

## Additional instructor notes: Soulslike and Blender

For 3D Soulslike/CAG demonstrations, point students to https://github.com/catprisbrey/Cats-Godot4-Modular-Souls-like-Template. This replaces the earlier third-person combat prototype recommendation. Review the current version and licensing, as the upstream author notes a planned v3 replacement.

If an imported Godot project displays "Blender 3.0+ is required to import '.blend' files", do not teach students to disable imports indiscriminately. Have their agent install Blender (with permission), locate Blender's executable, configure the importer, and re-run the scene.

Assume students do not know "GDD": define it as "one-page plan for what the game does" and have the AI invent three small concepts and draft the document for their review. They can paste the public repository URL into a compatible coding agent instead of learning Git commands.

Shared teaching chat: https://chatgpt.com/share/6b047749-5fcc-83ec-822e-3a76af146a33


## Mandatory Summer setup verification (November 2026 update)

Students should use Summer Engine desktop, Summer CLI and Summer MCP by default. The AI agent should inspect the current [installation](https://docs.summerengine.com/essentials/installation), [CLI](https://www.summerengine.com/cli), and [MCP](https://www.summerengine.com/mcp) documentation; configure the chosen local coding agent; run `npx -y summer-engine@latest doctor`; and verify MCP can access the running editor. Ordinary Godot is a fallback only with student approval. The instructor may prepare a Godot contingency machine for class emergencies, but must explain when it is used.
