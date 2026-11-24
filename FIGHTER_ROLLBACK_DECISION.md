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
