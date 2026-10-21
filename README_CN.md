<h3 align="center">这里每一个仓库，都从对话开始——最早是 Claude，现在是一整个班子。</h3>
<p align="center">医学出身 → 文化口工作 → 自学成才的 AI 工作流搭建者<br/>不会写 for 循环。46 个公开仓库全部诞生于中文对话。</p>
<p align="center"><a href="README.md">🇬🇧 English</a> · <a href="https://aliceljy.github.io">🏠 aliceljy.github.io</a> · <a href="https://aliceljy.github.io/playground/">🎮 playground</a></p>
<p align="center"><sub>29 个在役公开仓库 · 17 个光荣退役 · 27 个私有 · 132 个已合并 PR，其中 109 个合进了别人的项目 · 600+ 篇文章 · 数据截至 2026-10-22</sub></p>

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

**2026年5月**：搞了个「E-twin」——Telegram 上一个数字版的我。有点诡异但很好用。同月还干了一件事：Hermes 大整合，睿智和小试AI 合并进 Anti。5 个 Bot 收成 3 个，吞吐没掉，零件少了一半。（小试AI 留着当公众号笔名，反正它能活到最后。）

**2026年7月**：EC2 退役了。为了跑几个 cron 单养一台服务器，实在不划算。3 个变成 2 个。

**2026年9月**：14 号，OpenClaw 这一章合上了。Anti、LanceDB Test 和本机 Docker bot 环境撤除，我自己的 OpenClaw 相关仓库归档留作记录。一周后 Claude Code 和 Codex 也从我的 Telegram 桥上撤下，Claude 改走官方远程。同月 [playground](https://github.com/AliceLJY/playground) 开张：专门放纯粹因为好玩才做的东西。

**2026年10月**：Codex 的订阅月底到期，不续了。Grok 坐上了互审桌那把空椅子。与此同时，我的提示词文件夹长大成了一套正经系统，有前台、有保安（[见弹药库](#聚光灯弹药库)）。

**现在**：

```
  owner         当前跟我对话的那位，通常是 Claude Code
  reviewers     Kimi · AGY · Grok       冷读，互相隔离
  consultant    网页版 ChatGPT          专管「这推理到底站不站得住」
  night shift   Telegram 桥（Kimi ×2、AGY ×1）· E-twin
  Discord bots  0                       （巅峰是 5 个。四月的事就别提了。）
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
副本任务：  CortexReach 成员 · 109 个 PR 合进了不是我的仓库
搭子：      Claude——先桌面版，后 Code。现在它带一整个班子，我跟它说话还是最多。
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
| 代码审查 | 当前跟我对话的那位当 owner。Kimi、AGY、Grok 各自关在小黑屋里冷读，最多三轮。我看它们的分歧，最后拍板。 |
| 需要第二意见 | 要动手的交给 Kimi 或 AGY；要纯判断的交给网页版 ChatGPT——Pro 档一轮要想 27 分钟左右，所以只有值得等半小时的问题才配送过去。发出去的每一个字我都先过目。 |
| 需要图片 | 默认 Gemini（走 AGY，也就是 Google 的 Antigravity CLI），赶时间叫 Grok。Gemini 四月被裁、十月返聘。大家都很体面。 |
| 需要提示词 | 「去弹药库找个 XX」——总索引 → 子索引 → 配方，三跳到手，不用翻。 |
| 读报错日志 | 「你的逻辑呢？？？」 |
| 版本回滚 | 「你自己写的你不认识？？」 |
| 上线部署 | 「上次明明好好的！你失忆了吗！！」（它确实失忆了，所以才有了记忆层。） |
| 杀进程 | 「辛苦了先歇会儿」（是跟 Claude 说的） |
| 赶进度 | 「急什么，用旧版本的人还没跟上呢」 |
| 写 commit message | 「谢谢你陪我熬夜」 |
| 写文档 | 哈哈哈哈哈哈哈哈哈（不写的） |

### 🏰 CC 帝国，重画版

旧地图是 11 层叠起来的塔，每个仓库哪层塞得下就塞哪层。新地图改成跟着活儿走：一个需求进来，班子接手，调用「已经知道的」和「知道怎么做的」，交付出东西，学到的再流回去。**每一层只回答一个问题，每个仓库只待在一层**——就是你找它时第一个会去翻的那层。

```
        我 ── 用中文说话，多半在手机上
         │
         1  REACH ──────── 触达：我在哪儿跟它说话？
         │                 终端 · 浏览器 · Telegram · 微信
         │
         2  CREW ───────── 班子：谁来干，谁来查？
         │                 一个 owner + 三个冷读 reviewer
         │
  ┌────> ├── 3  MEMORY ─── 记忆：我们已经知道什么？
  │      │                 发生过什么 · 定过什么 · 读过什么
  │      │
  ├────> ├── 4  ARSENAL ── 弹药：东西怎么做出来？
  │      │                 提示词 · 思维透镜 · skill
  │      │
  │      5  FACTORY ────── 工厂：最后交付什么？
  │      │                 文章 · 视频 · 幻灯片 · App · 玩具
  │      │
  └──────┘  教训流回 3，好配方流回 4

  ══════════════════════════════════════════════════════════════════
         0  GROUND ─────── 地基：靠什么一直转下去？
                           harness · 两台 Mac · 容灾仓
```

<p align="center"><sub>6 层 · 1 个反馈闭环 · 0 个 for 循环</sub></p>

#### 1 · 触达 — 我在哪儿跟它说话？

两个方向都算。大多数负责把我的话送到 AI 那边，只有一个会自己先开口。

| | |
|---|---|
| [AgentDeck](https://github.com/AliceLJY/agentdeck) | Claude Code、Codex、Kimi、AGY 共用的 Web 终端——每个 CLI 一个标签页，tmux 保活，跨后端翻历史。手机、平板、电脑浏览器都能进。 |
| [docshell](https://github.com/AliceLJY/docshell) | 把 Claude Code 变成一份文档：段落进、段落出，工具调用变成页边批注。没有聊天气泡，也没有终端。 |
| [dsh-thumb](https://github.com/AliceLJY/dsh-thumb) | DeepSeek Harness 网页版的手机壳——侧栏变抽屉、设置改单列。零硬编码宿主 class hash。 |
| [telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | Claude Code、Codex、AGY、Kimi 各当一个 bot，拉进同一个 Telegram 群，走 A2A-TG 对话——一套带代数计数的信封协议，防止它们互相聊成死循环。 |
| [tg-bridge-channel](https://github.com/AliceLJY/tg-bridge-channel) | 姊妹桥，基于 Claude Agent View 后台 session。2026 年 5 月到 9 月，我的 Claude Code bot 跑在这里，之后改走官方远程。 |
| [wechat-ai-bridge](https://github.com/AliceLJY/wechat-ai-bridge) | 微信上用 Claude Code 和 Codex，带工具审批和双向传文件。 |
| [phone-remote](https://github.com/AliceLJY/phone-remote) | 手机变 Mac 的无线键盘 + CLI 启动器。一键打开 CLI，再用手机自带的语音输入口述——专治远程桌面打不进语音听写。 |
| [iphone-sensor-bridge-poc](https://github.com/AliceLJY/iphone-sensor-bridge-poc) | 手机 → Mac 传文件，走局域网或 Tailscale。补 AirDrop 帮不上的地方：非 Apple 手机，或者 Mac 留在家里。 |
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | 反方向的那一个——唯一会主动找我的。Telegram 陪伴 bot，什么时候来找我、什么时候闭嘴由模型自己判断；`/quiet` 写死在代码里，没得商量。 |

#### 2 · 班子 — 谁来干，谁来查？

整个班子只靠一条规矩运转：**当前跟我对话的那位就是 owner。** owner 负责规划、派活、读回结果，再把分歧原样摆到我面前，不和稀泥。我从不在 AI 之间搬上下文，顶多贴一个路径。

| | |
|---|---|
| [mutual-review-room](https://github.com/AliceLJY/mutual-review-room) | owner 带队的 tmux 互审房间。你只跟 owner 窗格说话，reviewer 在只读窗格旁观，各自保持原生会话。 |
| [agent-room-cli](https://github.com/AliceLJY/agent-room-cli) | 默认只监听本机的 CLI 聊天室，人类、Claude Code、Codex 同屋，@ 谁谁回。 |
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | 让几个 Claude Code 会话组队干活：MCP 传话、任务追踪、tmux/Zellij 自动唤醒。官方 Teams？我先做的。 |
| [trio-handoff](https://github.com/AliceLJY/trio-handoff) | Claude Code ⇄ Codex 互审用的证据交接包。Codex 走后不再日常使用；「拿 git 证据说话」这个习惯留在了互审流程里。 |
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | 设计记录：自然语言 workflow 编排的思路怎么演变，每个想法现在落在哪儿。 |
| ensemble *(私有)* | 班子的协作手册：谁擅长什么、什么时候该叫谁。协议本身不认人，每个成员各写一页。 |
| consult-gpt *(私有)* | 把一个边界清楚的问题交给网页版 ChatGPT，读回完整答复，并标清哪句来自哪边。发出去之前，每条消息都先给我看。 |

#### 3 · 记忆 — 我们已经知道什么？

它有一次忘了我叫什么。我记仇的。现在分三层：**提炼过的结论**（RecallNest）、**原始对话**（Deja）、**研究过的知识**（hippo）。要找定过的事 → RecallNest；要找那次对话原文 → Deja；要找文献怎么说 → hippo。

| | |
|---|---|
| [recallnest](https://github.com/AliceLJY/recallnest) | 一份记忆，所有终端共用——任何 MCP 客户端都能接的共享记忆层。Claude Code、Codex、Kimi、AGY 谁接班都能接着上一位往下做。 |
| [babel-memory](https://github.com/AliceLJY/babel-memory) | 覆盖 22 个语言代码的全文检索预处理：中日韩/泰文分词、混合文字路由、Snowball 词干，零必需依赖。RecallNest 在用。 |
| hippo-wiki *(私有)* | 1,300+ 页的 Obsidian 研究知识库——概念、论文、信源、借鉴审计。冷知识，和 RecallNest 的热记忆互补。 |
| hippo-mcp *(私有)* | 架在这个库上的只读检索服务。库再全，查不出来就只是个仓库。 |
| [deja-vu](https://github.com/vshulcz/deja-vu) *(上游项目，不是我的)* | 给本机所有 AI 工具的历史会话建索引。我是贡献者，合进去 8 个 PR，不是作者。 |
| cc-ebook-fetcher *(私有)* | macOS 上的书单抓取器。来源存疑就不下载，抓到的书投进电子书库，写作那边引书就从这里取。 |

#### 4 · 弹药 — 东西怎么做出来？

记忆层管「知道什么」，这一层管「知道怎么做」：班子真要动手做东西时伸手去拿的配方、方法和 skill。先上头牌。

##### 聚光灯：弹药库

四月它还只是一句「这个提示词好看，存一下」。到十月，它有了前台、档案柜、门口的保安，还有一位三跳之内就能帮你找到东西的图书管理员。

```
 SCOUT    侦察：Grok 侦察兵每天早上投一批候选，我自己也随手扔链接
   │
 GATE     0  这个我已经有了吗？—— 最忙的一道关
   │      1  它真的是提示词吗？—— 讲提示词的文章不算提示词
   │      2  它交付的是什么？—— 图 · 视频 · 可交互网页 · 方法
   │      3  放哪个架子？—— 按「想干什么」分，绝不按「什么风格」分
   │      4  署名齐不齐？—— 作者 · 出处 · 官方仓 · 收录日期 · 上游 commit + 许可证
   │
 SHELVE   上架：一份配方只存一份，别的架子只放指针，不放副本
   │
 FETCH    取用：「去弹药库找个 XX」→ 总索引 → 用途子索引 → one-shot-prompt.md
   │
 DRAW     出图：默认 Gemini（走 AGY），急的时候叫 Grok
   │
 SHIP     交付：文章配图 · 海报 · 短视频 · 3D 网页
```

| 数字（2026-10-22） | |
|---|---|
| 配方目录 | 238 个 |
| 复制即用的 one-shot 提示词 | 197 份 |
| 变体 · 编号卷 | 684 · 174 |
| 用途子索引 | 16 份（光海报就分了六份） |
| 上游追踪器 | 3 个，各追一位创作者的新提示词 |
| 提交 | 四月以来 512 次，其中 349 次在十月 |

馆规：

- **按用途归档，不按风格归档。** 风格是提示词自己的事，用途才是我晚上 11 点找它的路。
- **一份配方只存一份。** 两份必漂移，从来没有例外。
- **「全部撞重」是完全正常的结果。** 有一批送进来 117 卷，被拦下 111 卷。保安有标准，没有 KPI。
- **测没测过，写明白。** 238 个目录里有 194 个白纸黑字写了实测状态，「还没生图实测」是一个很体面的答案。感觉不算证据。
- **没署名，不上架。** 每份配方带五行抬头：作者、原帖出处、官方仓、收录日期、上游 commit 和许可证。

**为什么不公开：** 大部分配方改编自其他创作者，有些用的是非商用许可证。把署名记清楚是我的事，替人家二次分发不是我能做主的。所以架子保持私有，方法就摆在这里。

##### 工具箱里的其他家伙

| | |
|---|---|
| 照见 / Prism *(私有)* | 双面议会。验真面：看穿话术、揪出逻辑漏洞，把「说不出哪里不对劲」翻译成「说得出的一二三」；开矿面：挖出没人想到的角度。源自医学的鉴别诊断思维。 |
| 20 个思维透镜 *(私有)* | 从两本书逐章提炼：恩格尔克《如何像人类学家一样思考》和戈夫曼《日常生活中的自我呈现》。换个位置看一个题目时用。 |
| [repo-insight](https://github.com/AliceLJY/repo-insight) | 开源项目深度架构分析：证据先行的报告、对不可信仓库只读处理、借鉴审计。Why > What。 |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | 用语料训一个数字分身，落笔之前先做隐私过滤。我的声音，装了一瓶。有时候写得比我还好。尽量不去想。 |
| topic-vacuum *(私有)* | 动笔前先问：有没有人想看，有没有人已经说过？需求看小红书和抖音，供给看公众号。它造不出角度，只告诉你你的角度有没有被人占了。 |
| sogou-wechat-skill *(私有)* | 走搜狗检索公众号文章，评论有界聚合：分页限额、去重，完整还是部分如实标注。 |

#### 5 · 工厂 — 最后交付什么？

**写作** —— 一月以来在「我的AI小木屋」发了 600+ 篇

| | |
|---|---|
| content-alchemy 写作炼金 *(私有)* | 五阶段写作流水线：选题挖掘 → 信源提取 → 论断核查 → 精炼 → 去 AI 味成稿。 |
| content-publisher 配图发布 *(私有)* | 配图、社媒卡片、排版，以及经过核验的公众号草稿发布。流水线的下半段。 |

**视频** —— 长得最快的一翼

| | |
|---|---|
| story-video-skill *(私有)* | 故事 / 剧目 → 分层动画短片。先立故事契约、做低清预演、找陌生观众盲看，再上 Remotion、AI 生图分层素材和本地 TTS。 |
| cut-studio-skill *(私有)* | 加工已有素材：本地 ASR、按文字稿剪，出 MP4 或剪映草稿。 |
| knowledge-video *(私有)* | 知识口播视频：IP 形象出镜讲话，中间穿插信息图，全部按一条免费本地配音的时间轴走。 |
| video-works *(私有)* | 成品堆：11 支动画短片的源码、旁白和生图配方。 |
| [scenecast](https://github.com/AliceLJY/scenecast) | 把分页 HTML deck 渲染成确定性的元素级动效视频。HTML 始终是唯一视觉来源。 |
| video-skill-radar *(私有)* | 这条赛道的雷达：工具地图、蹲守清单、风格 POC。 |

**幻灯片**

| | |
|---|---|
| [slidesmith](https://github.com/AliceLJY/slidesmith) | HTML slides → 可编辑的 PowerPoint 对象，转不了的版式用截图兜底。 |
| [slidesmith-vision](https://github.com/AliceLJY/slidesmith-vision) | 校验过的视觉化 slide 规范 → SlideSmith 能直接吃的 HTML，本地图片内联。 |

**应用** —— 截图进，结构出

| | |
|---|---|
| [mailuo](https://github.com/AliceLJY/mailuo) | 脉络——聊天截图 → 行动卡片 → 人脉档案 → 关系洞察。零手动录入的个人 CRM。Expo RN app，BYOK 纯本地跑，或连自托管后端。 |
| [tenglu](https://github.com/AliceLJY/tenglu) | 誊录——滚动录屏 → 干净、能搜的文字，100% 手机本地、零联网权限。它交原料，脉络管解读。 |

**玩具** —— 纯粹因为想做

| | |
|---|---|
| [playground](https://github.com/AliceLJY/playground) · [去玩](https://aliceljy.github.io/playground/) | 一个仓、一个 Pages 站点：9 个小游戏、6 个 3D 展品。把白衣木偶打回英歌戏台的乐池、给药材按四气分篮、在下雨的广州小巷里拿人字拖拍蟑螂。 |
| [copium](https://github.com/AliceLJY/copium) | COPIUM 焦虑急诊室——披着赛博朋克皮的焦虑释放 App。慌张进，大笑出。 |
| [cobbler](https://github.com/AliceLJY/cobbler) | 我的 Claude Code Buddy 小机器人，孵出来 18 天就随功能下架了——现在复活了。她的巢在 Mac mini 上，每天早上发一张「N 个月前的今天」卡片、一本书和一页知识库。 |
| [drug-mystery-desk](https://github.com/AliceLJY/drug-mystery-desk) | 药研悬案局——以临床试验舞弊为题材的探案游戏。Codex 起的头，做成证据笔记本；Minis（我在 ChatGPT 侧的 AI）接手改造成游戏，全程在 ChatGPT Apps 上。只有完整证据链才能结案。 |

#### 0 · 地基 — 靠什么一直转下去？

有意保持私有。没人专门去参观一栋楼的地基，但没有地基什么都立不住。

| | |
|---|---|
| 一个已转私有的 harness 仓 | Hooks、rules、模板和工作流方法——上面所有东西的连接组织。 |
| sync-bridge-vault *(私有)* | 双机同步层的容灾仓：规则、记忆、skill、研究成果的历史。镜像不等于备份。 |
| 双机契约 | 不是仓库，是一本规矩。MacBook 随身走，Mac mini 永不睡。GitHub 是唯一真相源，人坐在哪台哪台写码，离开一台机之前先 push。 |

<details>
<summary>📜 <b>起点与演进</b>（一个非程序员自 2025-03 起的历程 · 归档 ≠ 遗忘）</summary>

有些起点长成了今天还在用的工具，有些已经退役。历程留在这里，退役的项目注明时间。

**2025-03 · 第 0 天** —— `grokbot` · `DS-V3-info` · `OpenAI-Autogen-Comparison` · `BlazorGeminiChat`
比其余一切早整整一年。一个不会写代码的人，第一次"我做了个东西"。我们不谈代码——谈的是动手开始的那股劲儿。

**更早 · Windows 时代** —— 在这一切上 GitHub 之前：.NET MAUI 多 AI 移动客户端（通义千问 / DeepSeek 版 + Claude·Gemini·Grok·GPT-4o 四合一对比，安卓/iOS/Win/mac）、Blazor 聊天应用、OpenAI Agents **可视化工作流设计器**、AutoGen / Magentic-One **多智能体编排实验**（通义千问、Grok 驱动）。多是本地快照——早在这些火起来之前，我就在搭跨平台、多模型、多 agent 的东西了。

**然后它一条线一条线长起来：**

| 线 | 起点 | 变成了 |
|---|---|---|
| 🧠 记忆 | `memory-lancedb-pro` | **recallnest** —— 我自己的；从一个念头起步，后来走了自己的路 · + babel-memory · hippo · deja-vu 的贡献者席位 |
| 🌉 远控 | `cc-shell` → `cc-genius` · `telegram-cli-bridge` | **AgentDeck** · **telegram-ai-bridge** + **tg-bridge-channel** |
| 🤝 多 agent | `claude-code-studio` —— "让几个 CC 互相聊起来"的念头 | `agent-room-cli` · `duo` *(2026-06 退役)* · `trio-handoff` *(2026-10 起不再日常使用)* → **owner 模型** + Kimi、AGY、Grok 三方互审，工程化成 **mutual-review-room** |
| 🎯 工作流 | `workflow-orchestrator` + 3 个 pipeline skill | **/trio** → **ensemble** 班子协作手册 |
| 🗃️ 提示词 | 一个「prompt 实验室」文件夹 *(2026-04)* | **弹药库** —— 238 个配方、16 份用途索引、每日侦察兵和门口保安 |
| ☁️ OpenClaw 时代 | `openclaw-worker` · `cli-bridge` · `a2a-gateway` · `cli-pipeline` · `mas-guide` | 后来演进为 Hermes + [openclaw-tunnel](https://github.com/AliceLJY/openclaw-tunnel)；**整条项目线于 2026-09-14 退役**。我的相关仓库已归档，此前归档的项目保留各自历史时间。 |
| 📦 快速启动 | `agent-nexus` · `cc-rules-cookbook` + `cc-hooks-gallery` | 一个已转私有的 harness 仓 |
| ✍️ 内容 | 早期实验 | 私有的写作 + 发布管线，后来又长出一整条视频线 |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 微信公众号二维码" width="200" /><br/>
  <b>我的AI小木屋</b>（微信公众号）· 一个不会写代码的人跟 Claude 过日子的真实记录<br/>
  <a href="https://weibo.com/u/1240841220">微博: 安闲静雅</a>
</p>
