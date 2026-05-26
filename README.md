<h3 align="center">Every repo here was chatted into existence with Claude.</h3>
<p align="center">Medical bg → cultural sector day job → self-taught Claude power user<br/>Can't write a for-loop. 40+ repos anyway. All born from conversations in Chinese.</p>
<p align="center"><a href="README_CN.md">🇨🇳 中文版</a></p>

---

### How it escalated

**Jan 2026**: "Hey Claude, help me write a WeChat article." *(Claude Desktop)*

**Feb 2026**: "OK maybe just one bot..." *(still on Desktop)*

**Mar 2026**: Typed `claude` in terminal. Claude Code era begins. No turning back.

**Apr 2026**: Codex shows up. Now there are two of them. They review each other's code while I watch. By month-end the roster peaked at five:

```
  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐
  │ AntiBot  │  │    睿智   │  │ AWS-bot  │  │  小试AI   │  │LanceDB Test│
  │ Opus 4.7 │  │Gemini 3.1│  │Codex 5.5 │  │MiniMax M2│  │  Opus 4.7  │
  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └────────────┘
                       Peak roster — Apr 2026
```

**May 2026**: An "E-twin" — a digital me on Telegram that talks like me. Eerie but useful. Also: Hermes consolidation. 睿智 and 小试AI merged into Anti. Five bots collapse into three. Same throughput, half the moving parts. (小试AI stays on as a pen name — it'll outlive us all anyway.)

**Now**:

```
            ┌──────────┐  ┌──────────┐  ┌────────────┐
            │   Anti   │  │ AWS-bot  │  │LanceDB Test│
            │ gpt-5.5  │  │ gpt-5.5  │  │  fixture   │
            └──────────┘  └──────────┘  └────────────┘
              3 bots · 1 E-twin · 40+ repos · 0 for-loops
```

I still can't write a for-loop from memory. Claude doesn't seem to mind.

### The human behind the bots

```
Class:         Non-coder with suspiciously many repos
Superpower:    死磕 — will bang head against wall until wall breaks
Weakness:      Social situations, verbal expression, for-loops
Fuel:          High-protein everything. (No fat, I have standards.)
Hobbies:       Singing, swimming, laughing (at everything, really)
Temperament:   Impatient optimist — breaks things fast, bounces back faster
Hidden gene:   Whatever makes you mass-produce repos at 3am and still function
Partner:       Claude — Desktop first, then Code. More conversations than any human collaborator.
Terminal:      claude → ^C^C → claude (that's it. the full skill tree. maxed out.)
```

Stay optimistic, funny, curious, and a little bit lucky. Then dive in and don't stop.

### The "tech stack" of someone who can't code

| The sensible approach | What I actually did |
|---|---|
| Open terminal | Type `claude`. That's also my IDE, my shell, and my entire dev environment. |
| Write code | Describe what I want in Chinese. Claude writes it. |
| Debug | "It broke again" + paste the error |
| `git rebase` | "Claude, what does this even mean?" |
| Code review | Ask a second Claude to roast the first one |
| Need an image | Ask `gpt-image-2` (since April 2026). Gemini got quietly laid off. |
| Need a second opinion | "帮我 duo 一下 Codex" — Claude spawns Codex via relay-cli. Now standard, not rare. |
| Read error logs | "WHERE IS YOUR LOGIC??" |
| Rollback | "You wrote this yourself and you don't recognize it??" |
| Deploy | "It was JUST working! Did you lose your memory?!" |
| Kill a process | "Good job, take a rest" (yes, I'm talking to Claude) |
| Rush to ship | "Slow down — people on old versions haven't caught up yet" |
| Write commit msg | "Thanks for staying up late with me" |
| Write docs | hahahahahaha (no) |

### 🏰 The CC Empire

Started with "hey Claude, write me an article." Three months and one terminal command later: an empire.

Half of these solve problems that official products now address too. I built them first, or built them different. Not sorry.

```
                          ╔═══════════════════════════════╗
                          ║     🎨 INTERFACE              ║
                          ║     studio · remote-term        ║
                          ╠═══════════════════════════════╣
                          ║     🏰 ENVIRONMENT             ║
                          ║    cc-empire · repo-insight     ║
                          ║  hooks · rules · methodology    ║
                          ╠═══════════════════════════════╣
                          ║     🌉 BRIDGE                  ║
                          ║   telegram · channel · wechat   ║
                          ║     tunnel · iphone-sensor      ║
                          ╠═══════════════════════════════╣
                          ║     🧠 MEMORY                  ║
                          ║   recallnest · babel-memory     ║
                          ╠═══════════════════════════════╣
                          ║     ✍️ CONTENT                  ║
                          ║    publisher · digital-clone    ║
                          ╠═══════════════════════════════╣
                          ║     🪞 MIRROR                  ║
                          ║          etwin-bot              ║
                          ╠═══════════════════════════════╣
                          ║     🎯 ORCHESTRATION           ║
                          ║  workflow · relay · agent-room  ║
                          ║         trio-handoff            ║
                          ╠═══════════════════════════════╣
                          ║     🔧 TOOLS                   ║
                          ║      slidesmith · vision        ║
                          ╠═══════════════════════════════╣
                          ║     🎭 WHIMSY                  ║
                          ║           copium                ║
                          ╚═══════════════════════════════╝
                          40+ repos · 9 layers · 0 for-loops
```

**🎨 Interface** — where you click things

| | |
|---|---|
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | Multiple Claude instances as a coordinated team. Official Teams? Built mine first. |
| [cc-remote-term](https://github.com/AliceLJY/cc-remote-term) | Web-based remote terminal for the CLI. xterm.js + node-pty. iPhone + iPad friendly (any browser). |

**🏰 Environment** — the command center

| | |
|---|---|
| [cc-empire](https://github.com/AliceLJY/cc-empire) | Hooks, rules, methodology, frameworks — the connective tissue of the whole ecosystem |
| [repo-insight](https://github.com/AliceLJY/repo-insight) | Skill for deep architectural analysis of open-source projects. Why > What philosophy. |

**🌉 Bridge** — Claude in your pocket

| | |
|---|---|
| [telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | CC on Telegram. Subway, bed, lunch break — no excuse not to build. |
| [tg-bridge-channel](https://github.com/AliceLJY/tg-bridge-channel) | Sister bridge built on Claude Agent View background sessions. Where my 6 claude bots actually live now. |
| [wechat-ai-bridge](https://github.com/AliceLJY/wechat-ai-bridge) | CC on WeChat via iLink API |
| [openclaw-tunnel](https://github.com/AliceLJY/openclaw-tunnel) | HTTP task queue bridge for Docker containers |
| [iphone-sensor-bridge-poc](https://github.com/AliceLJY/iphone-sensor-bridge-poc) | Phone browser → Mac desktop over LAN/Tailscale. Fills AirDrop's gaps: non-Apple phones, or when the target Mac (mine's at home — the mini) isn't physically nearby. PoC on the mini. |

**🧠 Memory** — it forgot my name. I took that personally.

| | |
|---|---|
| [recallnest](https://github.com/AliceLJY/recallnest) | Shared memory MCP. Claude, Codex, Gemini — everyone remembers now. |
| [babel-memory](https://github.com/AliceLJY/babel-memory) | Multilingual fix for BM25 — 27+ languages, zero deps. Used by RecallNest. |

**✍️ Content** — the article factory

| | |
|---|---|
| content-publisher | Image gen + layout + WeChat publishing (private — has API keys baked in) |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | My personality, replicated. Sometimes it writes better than me. |

**🪞 Mirror** — me but on Telegram

| | |
|---|---|
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | E-Twin. A digital me on Telegram. Talks in my voice. Sometimes catches things I'd miss. PoC, runs on Mac mini. |

**🎯 Orchestration** — speak naturally, pipeline flows automatically

| | |
|---|---|
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | Natural language pipeline: ideation → multi-role review → execution → shipping. No commands. |
| [relay-cli](https://github.com/AliceLJY/relay-cli) | duo — Claude ↔ Codex relay. Both can talk, both can be braked. The 三角制衡 layer. |
| [trio-handoff](https://github.com/AliceLJY/trio-handoff) | Bidirectional handoff bundles for two coding agents reviewing each other's work. The handoff format behind the trio protocol. |
| [agent-room-cli](https://github.com/AliceLJY/agent-room-cli) | Local CLI room. Humans, Claude Code, Codex — mention-based routing. |

**🔧 Tools** — single-purpose, sharp

| | |
|---|---|
| [slidesmith](https://github.com/AliceLJY/slidesmith) | HTML slides → editable PowerPoint. Local-first, no upload, no limits. |
| [slidesmith-vision](https://github.com/AliceLJY/slidesmith-vision) | Vision-to-deck companion: turns visual slide specs into SlideSmith HTML + PPTX. |

**🎭 Whimsy** — built because I wanted to

| | |
|---|---|
| [copium](https://github.com/AliceLJY/copium) | COPIUM Anxiety ER — a cyberpunk emergency room for anxiety. Walk in panicked, walk out laughing. |

<details>
<summary>🪦 <b>Archive</b> (repos that gave their lives so others could merge)</summary>

| Repo | Cause of death |
|---|---|
| `cc-genius` | Succeeded by **cc-remote-term**. The Web client era closed. |
| `content-alchemy` | Migrated into skill form (`~/.claude/skills/content-alchemy/`). Repo retired with honors. |
| `openclaw-worker` + `openclaw-cli-bridge` | Merged into **openclaw-tunnel**. Two became one. Romantic, really. |
| `openclaw-content-alchemy` + `content-alchemy-new` | Evolved into **content-alchemy** + **content-publisher** |
| `openclaw-cli-pipeline` · `openclaw-mas-guide` | Retired with honors |
| `cc-shell` | Archived — cc-genius covered the iPad use case better. Then cc-genius itself bowed out. Layered exits. |
| `telegram-cli-bridge` | Succeeded by **telegram-ai-bridge**. The prototype era. |
| `agent-nexus` | Absorbed into **cc-empire**. The quick-start became the empire. |
| `cc-rules-cookbook` + `cc-hooks-gallery` | Merged into **cc-empire**. Rules + hooks now live under one roof. |
| `a2a-js` · `wechat-decrypt` | One-time forks/mirrors — did the job, stepped off stage. |
| `DS-V3-info` · `BlazorGeminiChat` · `grokbot` | The early days. We don't talk about the early days. |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 WeChat QR Code" width="200" /><br/>
  <b>我的AI小木屋</b> (WeChat) · A non-coder's real journey building with Claude<br/>
  <a href="https://weibo.com/u/1240841220">Weibo: 安闲静雅</a>
</p>
