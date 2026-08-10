<h3 align="center">这里每一个仓库，都是跟 Claude 聊出来的。</h3>
<p align="center">医学出身 → 文化口工作 → Claude 重度用户<br/>不会写 for 循环。60+ 个仓库全部诞生于中文对话。</p>
<p align="center"><a href="README.md">🇬🇧 English</a> · <a href="https://aliceljy.github.io">🏠 aliceljy.github.io</a></p>

---

### 怎么就一发不可收拾了

**2026年1月**：「Claude，帮我写篇公众号文章。」*（Claude 桌面版）*

**2026年2月**：「那就做一个 Bot 吧……」*（还在桌面版）*

**2026年3月**：在终端输了 `claude`。Claude Code 时代开始。回不去了。

**2026年4月**：Codex 入场。现在有两个了。它俩互相 review 代码，我在旁边围观。月底阵容达到巅峰，5 个 Bot 同时在跑：

```
  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐
  │ AntiBot  │  │    睿智   │  │ AWS-bot  │  │  小试AI   │  │LanceDB Test│
  │ Opus 4.7 │  │Gemini 3.1│  │Codex 5.5 │  │MiniMax M2│  │  Opus 4.7  │
  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └────────────┘
                      巅峰阵容 — 2026年4月
```

**2026年5月**：搞了个「E-twin」——Telegram 上一个数字版的我，说话像我。有点诡异但很好用。同月还干了一件事：Hermes 大整合，睿智和小试AI 合并进 Anti。5 个 Bot 收成 3 个，吞吐没掉，零件少了一半。（小试AI 留着当公众号笔名，反正它能活到最后。）

**2026年7月**：EC2 退役了。为了跑几个 cron 单养一台服务器，实在不划算。3 个变成 2 个。

**现在**：

```
                   ┌──────────┐  ┌────────────┐
                   │   Anti   │  │LanceDB Test│
                   │ gpt-5.5  │  │  测试夹具  │
                   └──────────┘  └────────────┘
              2 个 Bot · 1 个 E-twin · 60+ 仓库 · 0 个 for 循环
```

至今不会手写 for 循环。Claude 表示无所谓。

### 本人

```
职业：      不会写代码但仓库比很多程序员还多的人
超能力：    死磕（墙不倒我不走，墙倒了换一面继续）
弱点：      社恐 + 口头表达困难 + for 循环
燃料：      高蛋白选手（肥肉不行，我有底线的）
爱好：      唱歌、游泳、笑（笑点很低那种）
性格：      急性子乐观派——搞砸得快，爬起来更快
隐藏基因：  精力旺盛到凌晨三点还在出仓库那种
搭子：      Claude——先桌面版，后 Code。比任何人类合作者都有默契。
终端技能：  claude → ^C^C → claude（没了。技能树点满了。）
```

保持乐观、幽默、纯真、幸运、好奇、活力。然后一头扎进去死磕。

### 「技术栈」

| 正经程序员 | 我 |
|---|---|
| 打开终端 | 输入 `claude`。这就是我的 IDE、Shell 和全部开发环境。|
| 写代码 | 用中文跟 Claude 描述需求。代码它来写。|
| 调试 | 「又双叒叕坏了」+ 甩截图 |
| `git rebase` | 「Claude 这啥玩意儿？」 |
| 代码审查 | 让 Claude 和 Codex 互相怼。我读它们的对话记录，然后选边站。 |
| 需要图片 | 叫 `gpt-image-2`（2026 年 4 月起）。Gemini 悄悄下岗了。 |
| 需要第二意见 | 「帮我喊 Codex 来看看」——Claude 直接 headless 调 Codex，读回结论，还得告诉我它俩哪里意见不合。现在是常态，不再罕见。 |
| 读报错日志 | 「你的逻辑呢？？？」 |
| 版本回滚 | 「你自己写的你不认识？？」 |
| 上线部署 | 「上次明明好好的！你失忆了吗！！」 |
| 杀进程 | 「辛苦了先歇会儿」（是跟 Claude 说的） |
| 赶进度 | 「急什么，用旧版本的人还没跟上呢」 |
| 写 commit message | 「谢谢你陪我熬夜」 |
| 写文档 | 哈哈哈哈哈哈哈哈哈（不写的） |

### 🏰 CC 帝国

最开始就是一句「Claude，帮我写篇文章」。

三个月后，一个终端命令之后：一个帝国。

其中一半功能官方后来也做了。我先做的，或者做得不一样。不后悔。

```
                          ╔═══════════════════════════════╗
                          ║     🎨 界面层                  ║
                          ║ studio · remote-term · docshell ║
                          ╠═══════════════════════════════╣
                          ║     🏰 环境层                   ║
                          ║    cc-empire · repo-insight     ║
                          ║  hooks · rules · methodology    ║
                          ║   vault · prism · tinkering     ║
                          ╠═══════════════════════════════╣
                          ║     🌉 桥接层                   ║
                          ║   telegram · channel · wechat   ║
                          ║     tunnel · iphone-sensor      ║
                          ╠═══════════════════════════════╣
                          ║     🧠 记忆层                   ║
                          ║ recallnest · babel · hippo-wiki ║
                          ╠═══════════════════════════════╣
                          ║     ✍️ 内容层                    ║
                          ║    publisher · digital-clone    ║
                          ╠═══════════════════════════════╣
                          ║     🎬 视频层                   ║
                          ║   story-video · cut-studio      ║
                          ║     scenecast · radar           ║
                          ╠═══════════════════════════════╣
                          ║     🪞 镜像层                   ║
                          ║          etwin-bot              ║
                          ╠═══════════════════════════════╣
                          ║     🎯 编排层                   ║
                          ║      workflow · agent-room      ║
                          ║   trio-handoff · codex-plugin   ║
                          ╠═══════════════════════════════╣
                          ║     🔧 工具层                   ║
                          ║ slidesmith · vision · sogou-wx  ║
                          ╠═══════════════════════════════╣
                          ║     🎭 玩票层                   ║
                          ║        copium · cobbler         ║
                          ╚═══════════════════════════════╝
                          60+ 个仓库 · 10 层架构 · 0 个 for 循环
```

**🎨 界面层** — 点按的地方

| | |
|---|---|
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | 多个 Claude 实例组队干活。官方 Teams？我先做的。 |
| [cc-remote-term](https://github.com/AliceLJY/cc-remote-term) | CLI 的 Web 远程终端。xterm.js + node-pty。iPhone + iPad 都友好（浏览器跑）。 |
| [docshell](https://github.com/AliceLJY/docshell) | CLI 的文档式界面。输入和回复都是文档段落，工具调用变成页边批注。没有聊天气泡、没有终端。 |

**🏰 环境层** — 指挥中心

| | |
|---|---|
| cc-empire *(private)* | Hooks、rules、方法论、框架——整个生态的连接组织 |
| [repo-insight](https://github.com/AliceLJY/repo-insight) | 开源项目深度架构分析 skill，Why > What 哲学 |
| 照见 / Prism *(私有)* | 验真 skill：看穿话术、识别逻辑漏洞，把"说不出哪里不对劲"翻译成"说得出的一二三"。源自医学的鉴别诊断思维。 |
| sync-bridge-vault *(私有)* | 双机同步层的容灾仓——规则 / 记忆 / skill / 研究成果的历史与第三副本。镜像不等于备份。 |
| tinkering-lab *(私有)* | prompt 实验室：可复用的实验，外加几个盯着上游仓库自动追更的轻量追踪器。 |

**🌉 桥接层** — 把 Claude 装进口袋

| | |
|---|---|
| [telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | Telegram 上用 CC。地铁上、床上、午饭间隙——没有理由不在 build。 |
| [tg-bridge-channel](https://github.com/AliceLJY/tg-bridge-channel) | 姊妹桥，基于 Claude Agent View 后台 session 引擎。这套 bot 的桥接身份实际跑在这里。 |
| [wechat-ai-bridge](https://github.com/AliceLJY/wechat-ai-bridge) | 微信上用 CC，iLink API |
| [openclaw-tunnel](https://github.com/AliceLJY/openclaw-tunnel) | Docker 容器的 HTTP 任务队列桥 |
| [iphone-sensor-bridge-poc](https://github.com/AliceLJY/iphone-sensor-bridge-poc) | 手机浏览器 → Mac 桌面，走 LAN/Tailscale。补 AirDrop 的盲区：非 Apple 手机，或目标 Mac（我家 mini）不在身边时。PoC，跑在 mini 上。 |

**🧠 记忆层** — 它忘了我叫什么。我记仇的。

| | |
|---|---|
| [recallnest](https://github.com/AliceLJY/recallnest) | 共享记忆 MCP。Claude、Codex、Kimi、AGY——四个端现在谁都不会忘了。 |
| [babel-memory](https://github.com/AliceLJY/babel-memory) | 27+ 语言 BM25 预处理。RecallNest 在用。 |
| hippo-wiki *(私有)* | 研究知识库（Obsidian）。沉淀冷门参考知识——概念 / 论文 / 信源，与 RecallNest 的热记忆互补。 |
| hippo-mcp *(私有)* | 架在这个库上的只读检索服务。库再全，召不回来也等于没有。 |

**✍️ 内容层** — 文章工厂

| | |
|---|---|
| content-alchemy 写作炼金 *(私有)* | 5 阶段 AI 写作流水线：选题挖掘 → 信源核查 → 成稿 → 精炼，支撑公众号「我的AI小木屋」。 |
| content-publisher 配图发布 *(私有)* | 图片生成 + 排版 + 微信公众号一键发布，content-alchemy 的下游。 |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | 我的人格，复制了一份。有时候写得比我还好。尽量不去想。 |

**🎬 视频层** — 最新长出来的一条线

| | |
|---|---|
| story-video-skill *(私有)* | 故事 / 剧目 → 多风格分层动画短片。Remotion + AI 生图分层素材 + 本地 TTS，按题材选风格。 |
| cut-studio-skill *(私有)* | 另一条腿：加工已有素材。本地 ASR、按文字剪，出 MP4 或剪映草稿。 |
| [scenecast](https://github.com/AliceLJY/scenecast) | 把分页 HTML deck 渲染成元素级动效视频。HTML 始终是唯一视觉来源。 |
| video-skill-radar *(私有)* | 这条赛道的雷达：工具地图、蹲守清单、手绘 / 白板 / 拼贴风格的 POC。 |

**🪞 镜像层** — Telegram 上的我

| | |
|---|---|
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | E-Twin。Telegram 上一个数字版的我，说话像我。偶尔抓到我会漏掉的事。PoC，跑在 Mac mini 上。 |

**🎯 编排层** — 说人话，流水线自己跑

| | |
|---|---|
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | 自然语言流水线：构思 → 多角色审查 → 执行 → 上线。不需要记命令。 |
| [trio-handoff](https://github.com/AliceLJY/trio-handoff) | 两个 coding agent 互审代码的双向 handoff 包，trio 协议的交接格式。 |
| [agent-room-cli](https://github.com/AliceLJY/agent-room-cli) | 本地 CLI 聊天室。人类、Claude Code、Codex —— @ 谁谁就回。 |
| [codex-plugin-cc](https://github.com/AliceLJY/codex-plugin-cc) | 在 Claude Code 里直接喊 Codex——审 diff 或派活，不用切出去。 |

**🔧 工具层** — 单一目的，刀刀见血

| | |
|---|---|
| [slidesmith](https://github.com/AliceLJY/slidesmith) | HTML slides → 可编辑 PowerPoint。本地优先，零上传，没有限制。 |
| [slidesmith-vision](https://github.com/AliceLJY/slidesmith-vision) | Vision 配套：把视觉化的 slide 规范转成 SlideSmith HTML + PPTX。 |
| sogou-wechat-skill *(私有)* | 走搜狗检索公众号文章，评论有界聚合——分页限额、去重，完整还是部分如实标注。 |
| cc-ebook-fetcher *(私有)* | macOS 上的书单抓取器。来源存疑就不下载，抓到了投进共享收件箱。 |

**🎭 玩票层** — 纯粹因为想做

| | |
|---|---|
| [copium](https://github.com/AliceLJY/copium) | COPIUM 焦虑急诊室——披着赛博朋克皮的焦虑释放 App。慌张进，大笑出。 |
| [cobbler](https://github.com/AliceLJY/cobbler) | 曾陪我写代码的 Buddy 小机器人，随官方下架"死"过一次，如今复活成 Android 电子宠物。巢跑在 mini，每天发一张「那年今日」卡。 |

<details>
<summary>📜 <b>起点与演进</b>（一个非程序员的 14 个月 · 归档 ≠ 遗忘）</summary>

这里没有谁"死了"。下面每个起点，都长成了今天还在跑的东西。

**2025-03 · 第 0 天** —— `grokbot` · `DS-V3-info` · `OpenAI-Autogen-Comparison` · `BlazorGeminiChat`
比其余一切早整整一年。一个不会写代码的人，第一次"我做了个东西"。我们不谈代码——谈的是动手开始的那股劲儿。

**更早 · Windows 时代** —— 在这一切上 GitHub 之前：.NET MAUI 多 AI 移动客户端（通义千问 / DeepSeek 版 + Claude·Gemini·Grok·GPT-4o 四合一对比，安卓/iOS/Win/mac）、Blazor 聊天应用、OpenAI Agents **可视化工作流设计器**、AutoGen / Magentic-One **多智能体编排实验**（通义千问、Grok 驱动）。多是本地快照——早在这些火起来之前，我就在搭跨平台、多模型、多 agent 的东西了。

**然后它一条线一条线长起来：**

| 线 | 起点 | 变成了 |
|---|---|---|
| 🧠 记忆 | `memory-lancedb-pro` | **recallnest** —— 我自己的；从一个念头起步，后来走了自己的路 · + babel-memory · hippo |
| 🌉 远控 | `cc-shell` → `cc-genius` · `telegram-cli-bridge` | **cc-remote-term** · **telegram-ai-bridge** + **tg-bridge-channel** |
| 🤝 多 agent | `claude-code-studio` —— "让几个 CC 互相聊起来"的念头 | `agent-room-cli` · `duo` *(2026-06 退役)* → **owner 模型交接** + 互审 |
| 🎯 工作流 | `workflow-orchestrator` + 3 个 pipeline skill | **/trio** |
| ☁️ OpenClaw 时代 | `openclaw-worker` · `cli-bridge` · `a2a-gateway` · `cli-pipeline` · `mas-guide` | Hermes + **openclaw-tunnel** |
| 📦 快速启动 | `agent-nexus` · `cc-rules-cookbook` + `cc-hooks-gallery` | **cc-empire** |
| ✍️ 内容 | 早期实验 | 私有的内容 + 发布管线 |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 微信公众号二维码" width="200" /><br/>
  <b>我的AI小木屋</b>（微信公众号）· 一个不会写代码的人跟 Claude 过日子的真实记录<br/>
  <a href="https://weibo.com/u/1240841220">微博: 安闲静雅</a>
</p>
