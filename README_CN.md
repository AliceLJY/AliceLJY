<h3 align="center">这里每一个仓库，都是跟 Claude 聊出来的。</h3>
<p align="center">医学出身 → 文化口工作 → Claude 重度用户<br/>不会写 for 循环。30+ 个仓库全部诞生于中文对话。</p>
<p align="center"><a href="README.md">🇬🇧 English</a></p>

---

### 怎么就一发不可收拾了

**2026年1月**：「Claude，帮我写篇公众号文章。」*（Claude 桌面版）*

**2026年2月**：「那就做一个 Bot 吧……」*（还在桌面版）*

**2026年3月**：在终端输了 `claude`。Claude Code 时代开始。回不去了。

**2026年4月**：Codex 入场。现在有两个了。它俩互相 review 代码，我在旁边围观。

**2026年5月**：搞了个「E-twin」——Telegram 上一个数字版的我，说话像我。有点诡异但很好用。

**现在**：

```
  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────┐
  │ AntiBot  │  │    睿智   │  │ AWS-bot  │  │  小试AI   │  │LanceDB Test│
  │ Opus 4.7 │  │Gemini 3.1│  │Codex 5.5 │  │MiniMax M2│  │  Opus 4.7  │
  └──────────┘  └──────────┘  └──────────┘  └──────────┘  └────────────┘
              5 个 Bot · 1 个 E-twin · 30+ 仓库 · 0 行手写代码
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
| 代码审查 | 开第二个 Claude 去怼第一个 |
| 需要图片 | 叫 Gemini。Gemini 基本只干这个。 |
| 需要第二意见 | 「帮我 duo 一下 Codex」——Claude 通过 relay-cli 喊出 Codex。现在是常态，不再罕见。 |
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
                          ║  cc-genius · studio · remote    ║
                          ╠═══════════════════════════════╣
                          ║     🏰 环境层                   ║
                          ║        cc-empire                ║
                          ║  hooks · rules · methodology    ║
                          ╠═══════════════════════════════╣
                          ║     🌉 桥接层                   ║
                          ║  telegram · wechat · tunnel     ║
                          ╠═══════════════════════════════╣
                          ║     🧠 记忆层                   ║
                          ║   recallnest · babel-memory      ║
                          ╠═══════════════════════════════╣
                          ║     ✍️ 内容层                    ║
                          ║  alchemy · publisher · clone    ║
                          ╠═══════════════════════════════╣
                          ║     🪞 镜像层                   ║
                          ║          etwin-bot              ║
                          ╠═══════════════════════════════╣
                          ║     🎯 编排层                   ║
                          ║  workflow-orch · relay-cli      ║
                          ╚═══════════════════════════════╝
                          30+ 个仓库 · 7 层架构 · 0 个 for 循环
```

**🎨 界面层** — 点按的地方

| | |
|---|---|
| [cc-genius](https://github.com/AliceLJY/cc-genius) | Web PWA 客户端，iPad 可用，不需要 API key |
| [claude-code-studio](https://github.com/AliceLJY/claude-code-studio) | 多个 Claude 实例组队干活。官方 Teams？我先做的。 |
| [cc-remote-term](https://github.com/AliceLJY/cc-remote-term) | CLI 的 Web 远程终端。xterm.js + node-pty。iPad 友好。 |

**🏰 环境层** — 指挥中心

| | |
|---|---|
| [cc-empire](https://github.com/AliceLJY/cc-empire) | Hooks、rules、方法论、框架——整个生态的连接组织 |

**🌉 桥接层** — 把 Claude 装进口袋

| | |
|---|---|
| [telegram-ai-bridge](https://github.com/AliceLJY/telegram-ai-bridge) | Telegram 上用 CC。地铁上、床上、午饭间隙——没有理由不在 build。 |
| [wechat-ai-bridge](https://github.com/AliceLJY/wechat-ai-bridge) | 微信上用 CC，iLink API |
| [openclaw-tunnel](https://github.com/AliceLJY/openclaw-tunnel) | Docker 容器的 HTTP 任务队列桥 |

**🧠 记忆层** — 它忘了我叫什么。我记仇的。

| | |
|---|---|
| [recallnest](https://github.com/AliceLJY/recallnest) | 共享记忆 MCP。Claude、Codex、Gemini——现在谁都不会忘了。 |
| [babel-memory](https://github.com/AliceLJY/babel-memory) | 27+ 语言 BM25 预处理。RecallNest + UltraMemory 都在用。 |

**✍️ 内容层** — 文章工厂

| | |
|---|---|
| [content-publisher](https://github.com/AliceLJY/content-publisher) | 图片生成 + 排版 + 微信公众号发布 |
| [digital-clone-skill](https://github.com/AliceLJY/digital-clone-skill) | 我的人格，复制了一份。有时候写得比我还好。尽量不去想。 |

**🪞 镜像层** — Telegram 上的我

| | |
|---|---|
| [etwin-bot](https://github.com/AliceLJY/etwin-bot) | E-Twin。Telegram 上一个数字版的我，说话像我。偶尔抓到我会漏掉的事。PoC，跑在 Mac mini 上。 |

**🎯 编排层** — 说人话，流水线自己跑

| | |
|---|---|
| [workflow-orchestrator](https://github.com/AliceLJY/workflow-orchestrator) | 自然语言流水线：构思 → 多角色审查 → 执行 → 上线。不需要记命令。 |
| [relay-cli](https://github.com/AliceLJY/relay-cli) | duo —— Claude ↔ Codex 互通 relay。都能说话，都能被人类急刹车。三角制衡那层。 |

<details>
<summary>🪦 <b>归档</b>（为了后人牺牲的仓库）</summary>

| 仓库 | 死因 |
|---|---|
| `openclaw-worker` + `openclaw-cli-bridge` | 合并进了 **openclaw-tunnel**。二合一，挺浪漫的。 |
| `openclaw-content-alchemy` + `content-alchemy-new` | 进化成了 **content-alchemy** + **content-publisher** |
| `openclaw-cli-pipeline` · `openclaw-mas-guide` | 光荣退役 |
| `cc-shell` | cc-genius 更好覆盖 iPad 使用场景 |
| `cc-genius` | 被 cc-remote-term 接班。Web 客户端时代结束。 |
| `cc-hooks-gallery` + `cc-rules-cookbook` | 合并进了 **cc-empire**。规则和 hooks 现在同住一个屋檐下。 |
| `agent-nexus` | 被 **cc-empire** 吸收。快速启动器变成了帝国本体。 |
| `content-alchemy` | 已迁成 skill 形式（`~/.claude/skills/content-alchemy/`），独立仓退役。 |
| `telegram-cli-bridge` | 被 **telegram-ai-bridge** 接班。原型时代的产物。 |
| `a2a-js` · `wechat-decrypt` | 一次性 fork/镜像，活完任务退场。 |
| `DS-V3-info` · `BlazorGeminiChat` · `grokbot` | 早期作品。我们不谈早期。 |

</details>

---

<p align="center">
  <img src="wechat-qrcode.jpg" alt="我的AI小木屋 微信公众号二维码" width="200" /><br/>
  <b>我的AI小木屋</b>（微信公众号）· 一个不会写代码的人跟 Claude 过日子的真实记录<br/>
  <a href="https://weibo.com/u/1240841220">微博: 安闲静雅</a>
</p>
