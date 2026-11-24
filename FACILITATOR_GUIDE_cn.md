> **双语版本 / Bilingual Edition (简体中文 + English)**  
> 中文优先帮助中国学生理解；保留英文原文、技术名称、命令与 URL，便于直接让 AI 编程代理执行。  
> **Language tip:** Ask your coding agent: “请用简体中文解释操作，但不要翻译代码、文件名和命令。”

# 讲师指南 / Workshop Facilitator Guide

**课程目标：** 让完全不会编程、游戏设计和 Git 的学生，在一节课内理解「创意 → 一页 GDD → Summer 配置 → 小型可玩原型 → 测试 → Git 保存」的开发循环。学生不需要独自操作复杂命令；他们应该能说出自己想做的游戏，并对 AI 给出的设计提出意见。

## 课前准备 / Before Class

- 让学生提前安装带本地文件/终端访问能力的 AI 编程代理（例如 Codex、Claude Code、Gemini CLI）。不要将纯浏览器聊天当作开发工具。
- 讲师电脑预先测试 **Summer Engine 桌面端、Summer CLI、Summer MCP、Git**；避免课堂现场下载大量模型。
- 准备一个小型 2D/3D 模板，并确认需要的 Blender 安装；预先测试 `.blend` 模型能否导入。
- 选择一个没有付费依赖、没有在线联机的演示游戏，准备一个备份可玩版本。
- 学生可用 `README_cn.md` 和 `MASTER_PROMPT_cn.md`，其中保留英文命令和文件名。

## 建议 60 分钟安排 / Suggested 60-Minute Schedule

| 时间 / Minutes | 环节 / Activity | 讲师动作 / Instructor action |
|---|---|---|
| 00–10 | 介绍和点子 / Game idea | 游戏可以很小；让 AI 提出 3 个小游戏想法 |
| 10–20 | 开发环境 / Setup | 检查 Summer、CLI、MCP 和 Git 是否连接 |
| 20–30 | GDD 审核 / Game plan | 让 AI 写一页 GDD，学生提出修改并批准 |
| 30–45 | 原型制作 / Build | 做一个机制；现场运行并观察错误 |
| 45–55 | 测试与保存 / Test & Save | 复现 Bug、修复、测试后 Git 提交 |
| 55–60 | 学生展示 / Demo | 演示并说出下次最值得增加的功能 |

## 常用中文教学提示词 / Classroom Prompts

> 我是第一次做游戏的学生。请用简体中文问我喜欢什么游戏，给我三个小点子，随后写一页 GDD。先解释 GDD 是什么，得到批准前不要开发。

> Summer Engine 提示编辑器无法连接。请先检查 Summer 桌面端、CLI 和 MCP，运行官方诊断，不要擅自改用普通 Godot。

> Godot 提示 Blender 3.0+ 才能导入 `.blend` 文件。请先检查是否已有 Blender，得到我的同意后再安装并设置可执行文件路径，验证模型和动画导入成功。

## 安全与边界 / Safety Notes

- 告诉学生：AI 会犯错，不能只看代码生成成功，要 **实际运行和试玩**。
- 不得在课堂要求学生分享账号密码；付费积分、订阅和大下载必须告知并征得同意。
- 联机、Steam、复杂 3D AI 素材生成属于进阶选修，不应阻碍第一次作品完成。
- 所有 Git 提交都要以运行正常为前提，不能擅自覆盖学生其他文件。

---

## Complete English Facilitator Guide / 英文原版讲师指南

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
