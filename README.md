<h3 align="center">Every repo here was chatted into existence with Claude.</h3>
<p align="center">Medical bg → cultural sector day job → self-taught Claude power user<br/>Can't write a for-loop. 40+ repos anyway. All born from conversations in Chinese.</p>
<p align="center"><a href="README_CN.md">🇨🇳 中文版</a> · <a href="https://aliceljy.github.io">🏠 aliceljy.github.io</a></p>

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
| Need a second opinion | "帮我喊 Codex 来看看" — Claude pulls Codex in via agent-room-cli. Now standard, not rare. |
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
                          ║ studio · remote-term · docshell ║
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
                          ║      workflow · agent-room      ║
                          ║         trio-handoff            ║
                          ╠═══════════════════════════════╣
                          ║     🔧 TOOLS                   ║
                          ║ slidesmith · vision · scenecast ║
                          ╠═══════════════════════════════╣
                          ║     🎭 WHIMSY                  ║
                          ║        copium · cobbler         ║
                          ╚═══════════════════════════════╝
                          40+ repos · 9 layers · 0 for-loops
```

**🎨 Interface** — where you click things

| | |
|---|---|
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | Multiple Claude instances as a coordinated team. Official Teams? Built mine first. |
| [cc-remote-term](https://github.com/AliceLJY/cc-remote-term) | Web-based remote terminal for the CLI. xterm.js + node-pty. iPhone + iPad friendly (any browser). |
| [docshell](https://github.com/AliceLJY/docshell) | Document-style interface for the CLI. Input and replies are document paragraphs; tool calls become margin comments. No chat bubbles, no terminal. |

**🏰 Environment** — the command center

| | |
|---|---|
| [cc-empire](https://github.com/AliceLJY/cc-empire) | Hooks, rules, methodology, frameworks — the connective tissue of the whole ecosystem |
| [repo-insight](https://github.com/AliceLJY/repo-insight) | Skill for deep architectural analysis of open-source projects. Why > What philosophy. |
| Prism *(private)* | "Verify-truth" skill: see through rhetoric, spot logic holes, turn gut-feel "something's off" into articulable reasons. Born from medical differential-diagnosis thinking. |

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
| hippo *(private)* | Researched-knowledge wiki + MCP. Cold reference knowledge (concepts / papers / sources), complementing RecallNest's hot session memory. |

**✍️ Content** — the article factory

| | |
|---|---|
| content-alchemy *(private)* | 5-stage AI writing pipeline: topic mining → source-check → draft → refine. Powers the "我的AI小木屋" WeChat account. |
| content-publisher *(private)* | Image generation + layout + one-click WeChat publishing. The downstream of content-alchemy. |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | My personality, replicated. Sometimes it writes better than me. |

**🪞 Mirror** — me but on Telegram

| | |
|---|---|
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | E-Twin. A digital me on Telegram. Talks in my voice. Sometimes catches things I'd miss. PoC, runs on Mac mini. |

**🎯 Orchestration** — speak naturally, pipeline flows automatically

| | |
|---|---|
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | Natural language pipeline: ideation → multi-role review → execution → shipping. No commands. |
| [trio-handoff](https://github.com/AliceLJY/trio-handoff) | Bidirectional handoff bundles for two coding agents reviewing each other's work. The handoff format behind the trio protocol. |
| [agent-room-cli](https://github.com/AliceLJY/agent-room-cli) | Local CLI room. Humans, Claude Code, Codex — mention-based routing. |

**🔧 Tools** — single-purpose, sharp

| | |
|---|---|
| [slidesmith](https://github.com/AliceLJY/slidesmith) | HTML slides → editable PowerPoint. Local-first, no upload, no limits. |
| [slidesmith-vision](https://github.com/AliceLJY/slidesmith-vision) | Vision-to-deck companion: turns visual slide specs into SlideSmith HTML + PPTX. |
| [scenecast](https://github.com/AliceLJY/scenecast) | Render a paginated HTML deck into an element-level motion video. The HTML stays the only visual source. |

**🎭 Whimsy** — built because I wanted to

| | |
|---|---|
| [copium](https://github.com/AliceLJY/copium) | COPIUM Anxiety ER — a cyberpunk emergency room for anxiety. Walk in panicked, walk out laughing. |
| [cobbler](https://github.com/AliceLJY/cobbler) | My old CC Buddy robot that "died" when the feature was sunset — reborn as an Android virtual pet. Its nest runs on the mini and sends me an "on this day" card every morning. |

<details>
<summary>📜 <b>Origins & Evolution</b> — a non-coder's 14-month trail (archived ≠ forgotten)</summary>

Nothing here "died." Every starting point below grew into something still running today.

**2025-03 · Day zero** — `grokbot` · `DS-V3-info` · `OpenAI-Autogen-Comparison` · `BlazorGeminiChat`
A full year before the rest. A non-coder's first "I made a thing." We don't talk about the code — we talk about the nerve it took to start.

**Even earlier · the Windows era** — before any of this reached GitHub: .NET MAUI multi-AI mobile clients (Qwen / DeepSeek editions + a 4-in-1 Claude·Gemini·Grok·GPT-4o compare app, Android/iOS/Win/mac), Blazor chat apps, an OpenAI-Agents **visual workflow designer**, and AutoGen / Magentic-One **multi-agent experiments** (Qwen- & Grok-driven). Mostly local snapshots — proof I was wiring up cross-platform, multi-model, multi-agent stuff well before it was cool.

**Then it grew, line by line:**

| Line | Started as | Became |
|---|---|---|
| 🧠 Memory | `memory-lancedb-pro` | **recallnest** — mine; sparked by an idea, then went its own way · + babel-memory · hippo |
| 🌉 Remote | `cc-shell` → `cc-genius` · `telegram-cli-bridge` | **cc-remote-term** · **telegram-ai-bridge** + **tg-bridge-channel** |
| 🤝 Multi-agent | `claude-code-studio` — the "let a few CCs talk to each other" spark | `agent-room-cli` → **duo** → group chat |
| 🎯 Workflow | `workflow-orchestrator` + 3 pipeline skills | **/trio** |
| ☁️ OpenClaw era | `openclaw-worker` · `cli-bridge` · `a2a-gateway` · `cli-pipeline` · `mas-guide` | Hermes + **openclaw-tunnel** |
| 📦 Quick-start | `agent-nexus` · `cc-rules-cookbook` + `cc-hooks-gallery` | **cc-empire** |
| ✍️ Content | early experiments | a private content + publishing pipeline |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 WeChat QR Code" width="200" /><br/>
  <b>我的AI小木屋</b> (WeChat) · A non-coder's real journey building with Claude<br/>
  <a href="https://weibo.com/u/1240841220">Weibo: 安闲静雅</a>
</p>
