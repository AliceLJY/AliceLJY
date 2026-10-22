<h3 align="center">Every repo here began as a conversation — first with Claude, now with a whole crew.</h3>
<p align="center">Medical background → cultural-sector day job → self-taught AI workflow builder<br/>Can't write a for-loop. 46 public repos anyway. All born from conversations in Chinese.</p>
<p align="center"><a href="README_CN.md">🇨🇳 中文版</a> · <a href="https://aliceljy.github.io">🏠 aliceljy.github.io</a> · <a href="https://aliceljy.github.io/playground/">🎮 playground</a></p>
<p align="center"><sub>29 active public repos · 17 retired with honors · 27 private · 132 merged PRs, 109 of them in other people's projects · 600+ articles · numbers as of 2026-10-22</sub></p>

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

**May 2026**: An "E-twin" — a digital me on Telegram. Eerie but useful. Also: the Hermes consolidation. 睿智 and 小试AI merged into Anti. Five bots collapse into three. Same throughput, half the moving parts. (小试AI stays on as a pen name — it'll outlive us all anyway.)

**Jul 2026**: The EC2 goes. Keeping a server alive just to run cron stopped making sense. Three become two.

**Sep 2026**: The OpenClaw chapter closes on the 14th. Anti, LanceDB Test and the local Docker bot stack shut down; my OpenClaw repos are archived as a record. A week later Claude Code and Codex leave my Telegram bridges, and Claude moves to the official Remote Control. Same month, the [playground](https://github.com/AliceLJY/playground) opens: a repo for things built purely for fun.

**Oct 2026**: Grok pulls up a chair at the review table. Meanwhile my prompt folder grows up into an actual system with a front desk and a bouncer ([see the Arsenal](#spotlight-the-prompt-arsenal)).

**Now**:

```
  owner         whoever I'm talking to, usually Claude Code
  reviewers     Kimi · AGY · Grok       cold reads, kept apart from each other
  consultant    ChatGPT on the web      for "is this reasoning actually sound?"
  night shift   Telegram bridges (Kimi ×2, AGY ×1) · E-twin
  Discord bots  0                       (peak was 5. we don't talk about April.)
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
Side quest:    CortexReach member · 109 PRs merged into repos that aren't mine
Partner:       Claude — Desktop first, then Code. It runs a crew now; I still talk to it most.
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
| Code review | Whoever I'm talking to owns the task. Kimi, AGY and Grok read it cold, in separate rooms, three rounds max. I read the disagreements and decide. |
| Need a second opinion | Hands-on work goes to Kimi or AGY. Pure judgement goes to ChatGPT on the web — Pro mode thinks for about 27 minutes, so only questions worth half an hour get to go. I read every outgoing message before it's sent. |
| Need an image | Gemini via AGY (Google's Antigravity CLI) by default, Grok when I'm in a hurry. Gemini was laid off in April and rehired in October. No hard feelings. |
| Need a prompt | "去弹药库找个 XX" — index → sub-index → recipe. Three hops, no scrolling. |
| Read error logs | "WHERE IS YOUR LOGIC??" |
| Rollback | "You wrote this yourself and you don't recognize it??" |
| Deploy | "It was JUST working! Did you lose your memory?!" (It did. Hence the memory layer.) |
| Kill a process | "Good job, take a rest" (yes, I'm talking to Claude) |
| Rush to ship | "Slow down — people on old versions haven't caught up yet" |
| Write commit msg | "Thanks for staying up late with me" |
| Write docs | hahahahahaha (no) |

### 🏰 The CC Empire, redrawn

The old map stacked 11 floors like a tower, and every repo got filed wherever it fit. The new map follows the work instead. A request comes in, the crew picks it up, draws on what it knows and on what it knows how to make, ships something, and whatever we learned flows back in. **Every layer answers exactly one question, and every repo sits on exactly one layer** — the one you'd check first when looking for it.

```
        me ── talking in Chinese, mostly from a phone
         │
         1  REACH ──────── where do I talk to it?
         │                 terminal · browser · Telegram · WeChat
         │
         2  CREW ───────── who does it, and who checks it?
         │                 one owner + three cold-reading reviewers
         │
  ┌────> ├── 3  MEMORY ─── what do we already know?
  │      │                 history · decisions · research
  │      │
  ├────> ├── 4  ARSENAL ── how do we make things?
  │      │                 prompts · thinking lenses · skills
  │      │
  │      5  FACTORY ────── what actually ships?
  │      │                 articles · videos · slides · apps · toys
  │      │
  └──────┘  lessons flow back into 3, good recipes into 4

  ══════════════════════════════════════════════════════════════════
         0  GROUND ─────── what keeps it all running?
                           harness · two Macs · disaster-recovery vault
```

<p align="center"><sub>6 layers · 1 feedback loop · 0 for-loops</sub></p>

#### 1 · REACH — where do I talk to it?

Both directions count. Most of these carry my words to the AI; one of them starts the conversation itself.

| | |
|---|---|
| [AgentDeck](https://github.com/AliceLJY/agentdeck) | Web terminal for Claude Code, Codex, Kimi and AGY — a tab each, tmux-backed sessions, a cross-backend history browser. Works from any phone, tablet or desktop browser. |
| [docshell](https://github.com/AliceLJY/docshell) | Claude Code as a document: paragraphs in, paragraphs out, tool calls as margin comments. No chat bubbles, no terminal. |
| [dsh-thumb](https://github.com/AliceLJY/dsh-thumb) | Phone shell for the DeepSeek Harness web GUI — the sidebar becomes a drawer, settings go single-column. Zero hardcoded host class hashes. |
| [telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | Claude Code, Codex, AGY and Kimi as separate bots in one Telegram group, talking over A2A-TG — an envelope protocol with generation counters, so they can't talk each other into an infinite loop. |
| [tg-bridge-channel](https://github.com/AliceLJY/tg-bridge-channel) | Sister bridge built on Claude Agent View background sessions. Carried my Claude Code bots from May to September 2026; they've since moved to the official Remote Control. |
| [wechat-ai-bridge](https://github.com/AliceLJY/wechat-ai-bridge) | Claude Code and Codex on WeChat, with tool approval and two-way file relay. |
| [phone-remote](https://github.com/AliceLJY/phone-remote) | Phone as a wireless keyboard + CLI launcher for the Mac. One tap opens a CLI, then dictate with the phone's own voice input — works where remote-desktop IME forwarding fails. |
| [phone-drop](https://github.com/AliceLJY/phone-drop) | Phone → Mac file drop over LAN or Tailscale, for when AirDrop can't help: a non-Apple phone, or a Mac that's sitting at home. |
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | The reverse direction — the only one that messages me first. A Telegram companion where the model decides when to ping and when to stay quiet, and `/quiet` is enforced in code. No negotiation. |

#### 2 · CREW — who does it, and who checks it?

One rule runs the whole crew: **whoever I'm talking to is the owner.** The owner plans, hands work out, reads the results back, and brings me the disagreements instead of smoothing them over. I never carry context between AIs; at most I paste a path.

| | |
|---|---|
| [mutual-review-room](https://github.com/AliceLJY/mutual-review-room) | Owner-led tmux rooms for persistent multi-model review. You talk to the owner pane; reviewers watch from read-only panes, each in its native session. |
| [agent-room-cli](https://github.com/AliceLJY/agent-room-cli) | Loopback-first local chat room for humans, Claude Code and Codex, with @-mention routing. |
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | Several Claude Code sessions working as a team: MCP messaging, task tracking, tmux/Zellij auto-wake. Official Teams? Built mine first. |
| [trio-handoff](https://github.com/AliceLJY/trio-handoff) | Evidence-rich handoff bundles for Claude Code ⇄ Codex review. Resting since October, when reviews moved to the mutual-review flow; its "show me the git evidence" habit went along. |
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | Design record: how natural-language workflow orchestration evolved, and where each idea lives now. |
| ensemble *(private)* | The crew playbook: who's good at what, and when to call whom. The protocol doesn't care who's in the room — each member gets one page. |
| consult-gpt *(private)* | Sends one well-scoped question to ChatGPT on the web, reads the whole answer back, and labels which part came from where. Every outgoing message is shown to me first. |

#### 3 · MEMORY — what do we already know?

It forgot my name once. I took that personally. Now there are three tiers: **distilled conclusions** (RecallNest), **raw transcripts** (Deja), and **researched knowledge** (hippo). Want a decision → RecallNest. Want the exact conversation → Deja. Want what the literature says → hippo.

| | |
|---|---|
| [recallnest](https://github.com/AliceLJY/recallnest) | One memory, every terminal — a shared memory layer for any MCP client. Claude Code, Codex, Kimi and AGY pick up where the last one left off. |
| [babel-memory](https://github.com/AliceLJY/babel-memory) | Language-aware full-text preprocessing for 22 language codes: CJK/Thai segmentation, mixed-script routing, Snowball stemming, zero required deps. Used by RecallNest. |
| hippo-wiki *(private)* | A 1,300+ page research wiki in Obsidian — concepts, papers, sources, borrow audits. Cold reference knowledge next to RecallNest's hot memory. |
| hippo-mcp *(private)* | Read-only retrieval server over that wiki. A library nobody can query is just a warehouse. |
| [deja-vu](https://github.com/vshulcz/deja-vu) *(upstream, not mine)* | Indexes past sessions from every AI tool on the machine. I'm a contributor with 8 merged PRs, not the author. |
| cc-ebook-fetcher *(private)* | Book-wishlist fetcher for macOS. Fail-closed on attribution; delivers into the ebook library the writing side quotes from. |

#### 4 · ARSENAL — how do we make things?

Memory is know-*what*. This layer is know-*how*: recipes, methods and skills the crew reaches for when it has to actually make something. Headliner first.

##### Spotlight: the prompt arsenal

It started in April as "save this prompt, it's pretty." By October it had a front desk, a filing system, a bouncer, and a librarian who answers in three hops.

```
 SCOUT    a Grok-powered scout drops candidates every morning; I toss in links too
   │
 GATE     0  do I already have it?        ← the busiest checkpoint
   │      1  is it actually a prompt?     an article about prompts is not a prompt
   │      2  what does it deliver?        image · video · interactive page · method
   │      3  which shelf?                 by what you want to do, never by style
   │      4  are the credits complete?    author · source · repo · date · commit + license
   │
 SHELVE   one recipe, one copy; other shelves get a pointer, not a duplicate
   │
 FETCH    "find me an XX" → index → purpose sub-index → one-shot-prompt.md
   │
 DRAW     Gemini via AGY by default, Grok when it's urgent
   │
 SHIP     article art · posters · short videos · 3D pages
```

| By the numbers (2026-10-22) | |
|---|---|
| Recipe folders | 238 |
| Copy-paste-ready one-shot prompts | 197 |
| Variants · numbered volumes | 684 · 174 |
| Purpose indexes | 16 (posters alone get six) |
| Upstream trackers | 3, each following one creator's new prompt releases |
| Commits | 512 since April, 349 of them this October |

House rules:

- **File by purpose, not by style.** Style is the prompt's own business; purpose is how I'll look for it at 11 p.m.
- **One recipe, one copy.** Two copies drift. They always drift.
- **"All duplicates" is a perfectly good result.** One batch: 117 volumes in, 111 bounced. The bouncer has standards and no quota.
- **Tested or not, say so.** 194 of the 238 folders state their test status in writing, and "not test-generated yet" is a perfectly respectable answer. Vibes are not evidence.
- **No credits, no shelf.** Every recipe carries five header lines: author, source post, official repo, date collected, upstream commit and license.

**Why it's private:** most recipes are adapted from other creators, some under non-commercial licences. Keeping their credit straight is my job; redistributing their work isn't my call. So the shelf stays private, and the method is right here.

##### The rest of the toolbox

| | |
|---|---|
| Prism / 照见 *(private)* | A two-sided council. Verify: see through rhetoric, spot logic holes, turn "something's off" into reasons you can say out loud. Mine: dig up angles nobody asked for. Born from medical differential diagnosis. |
| 20 thinking lenses *(private)* | Distilled chapter by chapter from two books, Engelke's *How to Think Like an Anthropologist* and Goffman's *The Presentation of Self in Everyday Life*. For looking at a topic from somewhere else. |
| [repo-insight](https://github.com/AliceLJY/repo-insight) | Deep architecture analysis of open-source projects: evidence-first reports, read-only handling of untrusted repos, borrow audits. Why > What. |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | Build a corpus-driven digital clone, with privacy filtering before anything gets written. My voice, bottled. Sometimes it writes better than me. I try not to think about it. |
| topic-vacuum *(private)* | Before writing: does anyone want this, and has someone already said it? Demand from Xiaohongshu and Douyin, supply from WeChat. It can't invent an angle — it only tells you whether yours is taken. |
| sogou-wechat-skill *(private)* | Search WeChat articles through Sogou, with bounded comment aggregation: paging caps, dedup, honest completeness labels. |

#### 5 · FACTORY — what actually ships?

**Writing** — 600+ articles on 我的AI小木屋 since January

| | |
|---|---|
| content-alchemy *(private)* | Five-stage writing pipeline: topic mining → source extraction → claim verification → refining → a humanized article. |
| content-publisher *(private)* | Images, social cards, editorial layout, and verified WeChat draft publishing. The downstream half. |

**Video** — the fastest-growing wing

| | |
|---|---|
| story-video-skill *(private)* | Story or repertoire → layered animated short. Story contract, low-res previz and a cold-viewer check first; then Remotion, generated art layers and local TTS. |
| cut-studio-skill *(private)* | Post-production for footage I already have: local ASR, edit by transcript, MP4 or a Jianying draft out. |
| knowledge-video *(private)* | Talking-head explainers: an IP character on camera, infographics in between, all timed to a free local voice track. |
| video-works *(private)* | The finished pile: source, narration and art recipes for 11 animated shorts. |
| [scenecast](https://github.com/AliceLJY/scenecast) | Paginated HTML deck → deterministic element-level motion video. The HTML stays the only visual source. |
| video-skill-radar *(private)* | Radar for the field: tool map, watchlist, and style PoCs. |

**Slides**

| | |
|---|---|
| [slidesmith](https://github.com/AliceLJY/slidesmith) | HTML slides → editable PowerPoint objects, with a screenshot fallback for layouts it can't convert. |
| [slidesmith-vision](https://github.com/AliceLJY/slidesmith-vision) | Validated visual slide specs → SlideSmith-ready HTML, local images inlined. |

**Apps** — screenshots in, structure out

| | |
|---|---|
| [mailuo](https://github.com/AliceLJY/mailuo) | 脉络 — chat screenshots → action cards → contact profiles → relationship insights. A personal CRM with zero manual data entry. Expo RN app; runs fully local with BYOK, or against a self-hosted backend. |
| [tenglu](https://github.com/AliceLJY/tenglu) | 誊录 — scrolling screen recording → clean, searchable text, 100% on-device with no network permission. It delivers the raw material; mailuo does the reading. |

**Toys** — built because I wanted to

| | |
|---|---|
| [playground](https://github.com/AliceLJY/playground) · [play](https://aliceljy.github.io/playground/) | One repo, one Pages site: 9 games and 6 3D exhibits. Bat a white-robed puppet back into a Yingge orchestra pit, sort herbs by their four natures, swat cockroaches with a flip-flop in a rainy Guangzhou alley. |
| [copium](https://github.com/AliceLJY/copium) | COPIUM Anxiety ER — a cyberpunk emergency room for anxiety. Walk in panicked, walk out laughing. |
| [cobbler](https://github.com/AliceLJY/cobbler) | My Claude Code Buddy robot, discontinued 18 days after she hatched — resurrected. Her nest on the Mac mini sends a "this day N months ago" card, a book and a wiki page every morning. |
| [drug-mystery-desk](https://github.com/AliceLJY/drug-mystery-desk) | 药研悬案局 — a detective game set inside clinical-trial fraud. Codex started it as an evidence notebook; Minis (my ChatGPT) rebuilt it into the game, all on the ChatGPT Apps platform. Only a complete evidence chain closes a case. |

#### 0 · GROUND — what keeps it all running?

Private on purpose. Nobody visits a building for its foundations, but nothing stands without them.

| | |
|---|---|
| a private harness repo | Hooks, rules, templates and workflow methods — the connective tissue of everything above. No longer public. |
| sync-bridge-vault *(private)* | Disaster-recovery history for the two-machine sync layer: rules, memory, skills, research. Mirroring isn't backup. |
| the two-Mac contract | Not a repo, a rulebook. A MacBook that travels, a Mac mini that never sleeps. GitHub is the source of truth, whichever machine I'm sitting at writes the code, and leaving a machine means pushing first. |

<details>
<summary>📜 <b>Origins & Evolution</b> — a non-coder's trail since 2025-03 (archived ≠ forgotten)</summary>

Some of these starting points grew into tools I still use; others have retired. The history stays here, with retirement dates where applicable.

**2025-03 · Day zero** — `grokbot` · `DS-V3-info` · `OpenAI-Autogen-Comparison` · `BlazorGeminiChat`
A full year before the rest. A non-coder's first "I made a thing." We don't talk about the code — we talk about the nerve it took to start.

**Even earlier · the Windows era** — before any of this reached GitHub: .NET MAUI multi-AI mobile clients (Qwen / DeepSeek editions + a 4-in-1 Claude·Gemini·Grok·GPT-4o compare app, Android/iOS/Win/mac), Blazor chat apps, an OpenAI-Agents **visual workflow designer**, and AutoGen / Magentic-One **multi-agent experiments** (Qwen- & Grok-driven). Mostly local snapshots — proof I was wiring up cross-platform, multi-model, multi-agent stuff well before it was cool.

**Then it grew, line by line:**

| Line | Started as | Became |
|---|---|---|
| 🧠 Memory | `memory-lancedb-pro` | **recallnest** — mine; sparked by an idea, then went its own way · + babel-memory · hippo · a contributor seat at deja-vu |
| 🌉 Remote | `cc-shell` → `cc-genius` · `telegram-cli-bridge` | **AgentDeck** · **telegram-ai-bridge** + **tg-bridge-channel** |
| 🤝 Multi-agent | `claude-code-studio` — the "let a few CCs talk to each other" spark | `agent-room-cli` · `duo` *(retired Jun 2026)* · `trio-handoff` *(out of daily use Oct 2026)* → **owner model** + mutual review with Kimi, AGY and Grok, engineered as **mutual-review-room** |
| 🎯 Workflow | `workflow-orchestrator` + 3 pipeline skills | **/trio** → **ensemble**, the crew playbook |
| 🗃️ Prompts | a "prompt lab" folder *(Apr 2026)* | **the Arsenal** — 238 recipes, 16 purpose indexes, a daily scout and a bouncer |
| ☁️ OpenClaw era | `openclaw-worker` · `cli-bridge` · `a2a-gateway` · `cli-pipeline` · `mas-guide` | Evolved into Hermes + [openclaw-tunnel](https://github.com/AliceLJY/openclaw-tunnel); **this project line retired 2026-09-14**. My related repositories are archived; earlier archive dates remain part of their history. |
| 📦 Quick-start | `agent-nexus` · `cc-rules-cookbook` + `cc-hooks-gallery` | a private harness repo (no longer public) |
| ✍️ Content | early experiments | a private writing + publishing pipeline, and then a whole video wing |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 WeChat QR Code" width="200" /><br/>
  <b>我的AI小木屋</b> (WeChat) · A non-coder's real journey building with Claude<br/>
  <a href="https://weibo.com/u/1240841220">Weibo: 安闲静雅</a>
</p>
