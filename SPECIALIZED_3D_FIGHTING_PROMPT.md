# Specialized 3D Fighting Game Prompt (Godot / Summer Engine)

Read [`MASTER_PROMPT.md`](MASTER_PROMPT.md) first. This specialist workflow supplements it; the GDD approval gate, Git safeguards, and project organization remain mandatory.

## Preferred fighting-game starting point

- **3D Fighter:** https://github.com/clintcan/3d-fighter
- **Optional Steam extension:** https://godotengine.org/asset-library/asset/2445
- **GodotSteam documentation:** https://godotsteam.com/getting_started/introduction/
- **Optional multiplayer skill:** https://github.com/cranebeaker/coop-anything
- **Netfox (only if technically justified):** https://github.com/foxssake/netfox

For one-on-one 3D fighting games inspired by Tekken or Street Fighter, verify and favor the 3D Fighter repository rather than building movement, combat and rollback from nothing. Its README documents deterministic 60 Hz simulation, custom rollback, training, online lobbies, sidesteps and replays. Its documented runtime is Godot 4.7; check the current code, Summer compatibility, and run headless tests before proceeding. Audit the code license (MIT) and separate asset licenses/attribution.

**Do not add Netfox automatically.** Preserve one authoritative rollback/simulation system. Only propose a Netfox migration if a proven requirement cannot be met otherwise, and first prototype, benchmark and test the change.

For optional Steam multiplayer, install the actual GodotSteam GDExtension, adapt lobby discovery/invites and transport to the fighter's network interface, and retain its custom rollback. Verify with two real accounts and exported builds; do not promise host migration, relay support or plug-and-play integration without tests.

For multiplayer beyond 1v1, tag-team, or free-roaming 3D arena fighting, explain the increased architectural scope before deciding to use the repository as a main base versus reference only.

## Copy-ready beginner request

```text
I want to make an original 3D fighting game with Tekken-style sidesteps, combos, throws and responsive controls. Read this repository and its docs first: https://github.com/clintcan/3d-fighter. Check its Godot version, rollback and simulation tests, and licenses. Reuse its fighting framework and built-in rollback rather than installing Netfox unnecessarily. Ask me if I need Steam multiplayer; if yes, plan a GodotSteam GDExtension integration separately. Help me make a one-page GDD with 2 fighters, 1 stage and local versus as the first milestone. Explain everything in beginner-friendly language. Wait for GDD approval and START DEVELOPMENT before coding.
```



### Fighter rollback selection — the user decides

**Default:** Start with [clintcan/3d-fighter](https://github.com/clintcan/3d-fighter) and preserve its existing deterministic combat and rollback. **Do not install Netfox or Rollback in a Box just because they exist.** For wall-running, aerial combat, and breakable buildings, first prototype scripted movement and synchronized intact/damaged/collapsed collision states; cosmetic debris can remain visual-only.

**Only if a verified limitation arises**, explain the alternatives in plain English and ask the user to choose:

- **Keep the fighter's built-in rollback** — preferred when sufficient; no extra framework or wasted tokens.
- **Netfox** — consider only for a concrete networking need that justifies migrating/reworking the fighter's rollback; it does not inherently make rigid-body physics deterministic.
- **Rollback in a Box** — consider only if gameplay-critical moving rigid bodies or destructible rubble demand reproducible 3D physics, and prove integration in a small test.

**Do not choose or integrate either optional system without explicit user approval.** Never run two competing rollback systems. If approved, use one simulation clock, one snapshot/rollback authority, and multi-client/desync tests. GodotSteam is a separate optional lobby/transport decision.

