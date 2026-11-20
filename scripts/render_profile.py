#!/usr/bin/env python3
"""Render the profile's SVG pieces from profile.json.

    python3 scripts/render_profile.py

Writes into assets/:
  stats-{en,zh}-{light,dark}.svg    number tiles (refreshed weekly by the Action)
  now-{en,zh}.svg                   animated terminal: who is on shift
  empire-{en,zh}-{light,dark}.svg   the six-layer map with a flowing feedback loop
  showcase/<slug>-{en,zh}.svg       playground cards, built from showcase/<slug>.jpg

Standard library only. Every animation starts from a hidden state and ends
visible, so turning animations off (prefers-reduced-motion) still shows everything.
"""
import base64
import json
import re
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

SANS = ("ui-rounded,'SF Pro Rounded','Nunito','Segoe UI',system-ui,-apple-system,"
        "'PingFang SC','Hiragino Sans GB','Microsoft YaHei','Noto Sans CJK SC',sans-serif")
MONO = ("ui-monospace,'SF Mono','JetBrains Mono',Menlo,Consolas,"
        "'PingFang SC','Microsoft YaHei',monospace")

# Crayon colours lifted from the banner.
ORANGE, PINK, PURPLE, LIME, BLUE, YELLOW = "#F97316", "#FF5FA2", "#8B5CF6", "#84CC16", "#3B82F6", "#EAB308"
THEMES = {
    "light": {"bg": "#FBF5E9", "card": "#FFFDF8", "ink": "#2B2140", "muted": "#7A6F86", "line": "#E7DCC8"},
    "dark": {"bg": "#17141F", "card": "#221D2D", "ink": "#F4EEE3", "muted": "#A79DB4", "line": "#3A3248"},
}
REDUCED = "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"


def svg(w, h, body, style="", label=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(label, {chr(34): "&quot;"})}"><style>{style}{REDUCED}</style>{body}</svg>\n')


def t(x):
    return escape(str(x))


def write(name, text):
    path = ASSETS / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------- stats
def stats(data, lang, theme):
    s, c = data["stats"], THEMES[theme]
    pg = s["playground_games"] + s["playground_exhibits"] + s["playground_behind"] + s["playground_tools"]
    if lang == "en":
        tiles = [
            (s["public_active"], "public repos, active", f"+ {s['public_retired']} retired with honours", PURPLE),
            (s["merged_prs"], "merged pull requests", f"{s['merged_prs_elsewhere']} landed in others' repos", BLUE),
            (pg, "playground pieces", f"{s['playground_games']} games · {s['playground_exhibits']} 3D exhibits", LIME),
            (s["for_loops"], "for-loops written", "by me. Claude wrote the rest.", ORANGE),
        ]
        foot = f"checked every week by a GitHub Action · numbers as of {s['as_of']}"
    else:
        tiles = [
            (s["public_active"], "在役公开仓库", f"另有 {s['public_retired']} 个光荣退役", PURPLE),
            (s["merged_prs"], "已合并 PR", f"其中 {s['merged_prs_elsewhere']} 个合进别人的项目", BLUE),
            (pg, "playground 作品", f"{s['playground_games']} 个小游戏 · {s['playground_exhibits']} 个 3D 展页", LIME),
            (s["for_loops"], "手写 for 循环", "剩下的都是 Claude 写的", ORANGE),
        ]
        foot = f"GitHub Action 每周自动核对 · 数字截至 {s['as_of']}"
    w, h, gap, tw = 880, 176, 16, 208
    body = []
    for i, (num, label, sub, col) in enumerate(tiles):
        x = i * (tw + gap)
        d = 0.15 + i * 0.18
        body.append(
            f'<g class="tile" style="animation-delay:{d:.2f}s">'
            f'<rect x="{x}" y="0" width="{tw}" height="146" rx="18" fill="{c["card"]}" stroke="{c["line"]}"/>'
            f'<rect class="bar" x="{x + 18}" y="16" width="{tw - 36}" height="6" rx="3" fill="{col}" '
            f'style="animation-delay:{d + 0.2:.2f}s"/>'
            f'<text x="{x + 18}" y="78" font-family="{SANS}" font-size="44" font-weight="800" fill="{col}">{t(num)}</text>'
            f'<text x="{x + 18}" y="104" font-family="{SANS}" font-size="15" font-weight="700" fill="{c["ink"]}">{t(label)}</text>'
            f'<text x="{x + 18}" y="126" font-family="{SANS}" font-size="12" fill="{c["muted"]}">{t(sub)}</text>'
            f'</g>')
    body.append(f'<text x="{w / 2}" y="168" text-anchor="middle" font-family="{SANS}" font-size="11.5" '
                f'fill="{c["muted"]}">{t(foot)}</text>')
    style = (".tile{animation:up .7s cubic-bezier(.2,.8,.2,1) both}"
             "@keyframes up{from{opacity:0;transform:translateY(14px)}}"
             ".bar{transform-box:fill-box;transform-origin:left;animation:grow .9s ease-out both}"
             "@keyframes grow{from{transform:scaleX(0)}}")
    label = " · ".join(f"{n} {l}" for n, l, _, _ in tiles)
    return svg(w, h, "".join(body), style, label)


# ---------------------------------------------------------------- now
def now(data, lang):
    rows = data["now"]
    cmd = "claude --who-is-on-shift"
    w, top, lh = 880, 92, 30
    h = top + len(rows) * lh + 46
    bg, bar, ink, muted = "#1B1726", "#2A2338", "#F4EEE3", "#8E84A0"
    cols = [ORANGE, PINK, PURPLE, LIME, BLUE, YELLOW, "#22D3EE"]
    b = [f'<rect width="{w}" height="{h}" rx="16" fill="{bg}"/>',
         f'<path d="M0 16a16 16 0 0 1 16-16h{w - 32}a16 16 0 0 1 16 16v20H0z" fill="{bar}"/>',
         f'<circle cx="24" cy="18" r="6" fill="#FF5F57"/><circle cx="44" cy="18" r="6" fill="#FEBC2E"/>'
         f'<circle cx="64" cy="18" r="6" fill="#28C840"/>',
         f'<text x="{w / 2}" y="23" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{muted}">'
         f'~/cabin — the crew</text>',
         '<clipPath id="type"><rect class="typer" x="52" y="44" width="300" height="30"/></clipPath>',
         f'<text x="28" y="64" font-family="{MONO}" font-size="16" fill="{LIME}">❯</text>',
         f'<text x="52" y="64" font-family="{MONO}" font-size="16" fill="{ink}" clip-path="url(#type)">{t(cmd)}</text>']
    for i, (key, en, zh) in enumerate(rows):
        y = top + i * lh + 10
        d = 1.9 + i * 0.32
        b.append(f'<g class="row" style="animation-delay:{d:.2f}s">'
                 f'<text x="40" y="{y}" font-family="{MONO}" font-size="15" font-weight="700" '
                 f'fill="{cols[i % len(cols)]}">{t(key)}</text>'
                 f'<text x="196" y="{y}" font-family="{MONO}" font-size="15" fill="{ink}">'
                 f'{t(en if lang == "en" else zh)}</text></g>')
    end = top + len(rows) * lh + 16
    b.append(f'<text x="28" y="{end}" font-family="{MONO}" font-size="16" fill="{LIME}">❯</text>'
             f'<rect class="cursor" x="52" y="{end - 15}" width="10" height="19" fill="{ink}"/>')
    steps = len(cmd)
    style = (f".typer{{transform-box:fill-box;transform-origin:left;animation:type 1.4s steps({steps}) .3s both}}"
             "@keyframes type{from{transform:scaleX(0)}}"
             ".row{animation:in .45s ease-out both}@keyframes in{from{opacity:0;transform:translateX(-8px)}}"
             ".cursor{animation:blink 1.1s steps(1) infinite}@keyframes blink{50%{opacity:0}}")
    label = "; ".join(f"{k}: {en if lang == 'en' else zh}" for k, en, zh in rows)
    return svg(w, h, "".join(b), style, label)


# ---------------------------------------------------------------- empire
def empire(data, lang, theme):
    e, c = data["empire"], THEMES[theme]
    zh = lang == "zh"
    cols = {"1": PINK, "2": PURPLE, "3": BLUE, "4": LIME, "5": ORANGE, "0": YELLOW}
    w, cx, cw, ch, y0, step = 880, 150, 600, 66, 84, 88
    b = [f'<rect width="{w}" height="664" rx="22" fill="{c["bg"]}"/>']
    # me
    me = e["me"][1 if zh else 0]
    b.append(f'<g class="card" style="animation-delay:0s"><rect x="{cx}" y="22" width="{cw}" height="40" rx="20" '
             f'fill="{c["card"]}" stroke="{c["line"]}" stroke-dasharray="5 5"/>'
             f'<text x="{cx + cw / 2}" y="47" text-anchor="middle" font-family="{SANS}" font-size="15" '
             f'fill="{c["ink"]}">💬  {t(me)}</text></g>')
    # spine with flowing dashes
    spine_x = cx + 40
    b.append(f'<line x1="{spine_x}" y1="62" x2="{spine_x}" y2="{y0 + 4 * step}" stroke="{c["line"]}" stroke-width="4"/>'
             f'<line class="flow" x1="{spine_x}" y1="62" x2="{spine_x}" y2="{y0 + 4 * step}" stroke="{c["muted"]}" '
             f'stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round"/>')
    centers = {}
    for i, layer in enumerate(e["layers"][:5]):
        num, name, q_en, s_en, q_zh, s_zh = layer
        y = y0 + i * step
        centers[num] = y + ch / 2
        b.append(card(cx, y, cw, ch, num, name, q_zh if zh else q_en, s_zh if zh else s_en, cols[num], c, 0.15 + i * 0.14))
    # feedback loop: out of FACTORY, up the right side, back into MEMORY and ARSENAL
    rx = cx + cw + 56
    y5, y3, y4 = centers["5"], centers["3"], centers["4"]
    loop = f"M{cx + cw} {y5} H{rx - 14} Q{rx} {y5} {rx} {y5 - 14} V{y3 + 14} Q{rx} {y3} {rx - 14} {y3} H{cx + cw + 10}"
    b.append(f'<path d="{loop}" fill="none" stroke="{c["line"]}" stroke-width="4"/>'
             f'<path class="flow" d="{loop}" fill="none" stroke="{ORANGE}" stroke-width="4" '
             f'stroke-dasharray="2 14" stroke-linecap="round"/>'
             f'<path d="M{rx} {y4} H{cx + cw + 10}" stroke="{c["line"]}" stroke-width="4"/>'
             f'<path class="flow" d="M{rx} {y4} H{cx + cw + 10}" stroke="{LIME}" stroke-width="4" '
             f'stroke-dasharray="2 14" stroke-linecap="round"/>'
             f'<path d="M{cx + cw + 16} {y3 - 7} l-9 7 l9 7" fill="none" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>'
             f'<path d="M{cx + cw + 16} {y4 - 7} l-9 7 l9 7" fill="none" stroke="{LIME}" stroke-width="3" stroke-linecap="round"/>')
    ly = y0 + 4 * step + ch + 30
    b.append(f'<text x="{cx + cw}" y="{ly}" text-anchor="end" font-family="{SANS}" font-size="13.5" '
             f'font-style="italic" fill="{c["muted"]}">↺  {t(e["loop"][1 if zh else 0])}</text>')
    # ground
    gy = ly + 26
    b.append(f'<line x1="40" y1="{gy}" x2="{w - 40}" y2="{gy}" stroke="{c["line"]}" stroke-width="2"/>'
             f'<line x1="40" y1="{gy + 6}" x2="{w - 40}" y2="{gy + 6}" stroke="{c["line"]}" stroke-width="2"/>')
    num, name, q_en, s_en, q_zh, s_zh = e["layers"][5]
    b.append(card(40, gy + 22, w - 80, ch, num, name, q_zh if zh else q_en, s_zh if zh else s_en, cols[num], c, 0.95))
    style = (".card{animation:up .7s cubic-bezier(.2,.8,.2,1) both}"
             "@keyframes up{from{opacity:0;transform:translateY(12px)}}"
             ".flow{animation:flow 1.2s linear infinite}@keyframes flow{to{stroke-dashoffset:-32}}")
    label = "; ".join(f"{l[0]} {l[1]}: {l[4] if zh else l[2]}" for l in e["layers"])
    return svg(w, 664, "".join(b), style, label)


def card(x, y, w, h, num, name, q, sub, col, c, delay):
    return (f'<g class="card" style="animation-delay:{delay:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{c["card"]}" stroke="{c["line"]}"/>'
            f'<rect x="{x}" y="{y}" width="8" height="{h}" rx="4" fill="{col}"/>'
            f'<circle cx="{x + 40}" cy="{y + h / 2}" r="17" fill="{col}"/>'
            f'<text x="{x + 40}" y="{y + h / 2 + 6}" text-anchor="middle" font-family="{SANS}" font-size="17" '
            f'font-weight="800" fill="#FFFFFF">{t(num)}</text>'
            f'<text x="{x + 72}" y="{y + 29}" font-family="{SANS}" font-size="17" font-weight="800" '
            f'letter-spacing="1.5" fill="{c["ink"]}">{t(name)}'
            f'<tspan dx="12" font-size="15" font-weight="500" letter-spacing="0">{t(q)}</tspan></text>'
            f'<text x="{x + 72}" y="{y + 51}" font-family="{SANS}" font-size="13" fill="{c["muted"]}">{t(sub)}</text>'
            f'</g>')


# ---------------------------------------------------------------- showcase
def showcase_card(item, lang):
    jpg = ASSETS / "showcase" / f"{item['slug']}.jpg"
    data = base64.b64encode(jpg.read_bytes()).decode()
    w, h = 800, 450
    kind = item["kind"][0 if lang == "en" else 1]
    title = item["en" if lang == "en" else "zh"]
    tw = 30 + len(kind) * (13 if lang == "en" else 20)
    body = (f'<defs><clipPath id="r"><rect width="{w}" height="{h}" rx="22"/></clipPath>'
            f'<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset=".55" stop-color="#000" stop-opacity="0"/>'
            f'<stop offset="1" stop-color="#000" stop-opacity=".78"/></linearGradient></defs>'
            f'<g clip-path="url(#r)"><image class="zoom" width="{w}" height="{h}" href="data:image/jpeg;base64,{data}"/>'
            f'<rect width="{w}" height="{h}" fill="url(#g)"/></g>'
            f'<rect x="26" y="{h - 112}" width="{tw}" height="34" rx="17" fill="#FFFFFF" fill-opacity=".92"/>'
            f'<text x="{26 + tw / 2}" y="{h - 88}" text-anchor="middle" font-family="{SANS}" font-size="18" '
            f'font-weight="800" letter-spacing="1" fill="#2B2140">{t(kind)}</text>'
            f'<text x="26" y="{h - 34}" font-family="{SANS}" font-size="42" font-weight="800" fill="#FFFFFF">{t(title)}</text>'
            f'<text x="{w - 28}" y="{h - 36}" text-anchor="end" font-family="{SANS}" font-size="24" '
            f'font-weight="700" fill="#FFFFFF" fill-opacity=".85">{"play ↗" if lang == "en" else "去玩 ↗"}</text>')
    style = (".zoom{transform-origin:center;transform-box:fill-box;animation:kb 14s ease-in-out infinite alternate}"
             "@keyframes kb{to{transform:scale(1.07)}}")
    return svg(w, h, body, style, f"{title} ({kind})")


# ---------------------------------------------------------------- text layout helpers
def text_width(s, fs, bold=False):
    w = 0.0
    for ch in s:
        if ord(ch) >= 0x2E80 or ch in "「」（）—…·":
            w += fs * (1.0 if ord(ch) >= 0x2E80 else 0.62)
        elif ch == " ":
            w += fs * 0.28
        elif ch in "il.,;:'|!":
            w += fs * 0.3
        elif ch.isupper() or ch in "mwMW@%":
            w += fs * (0.7 if bold else 0.66)
        else:
            w += fs * (0.58 if bold else 0.54)
    return w


def wrap(s, fs, width, bold=False):
    tokens = re.findall(r"[⺀-￿]|[^\s⺀-￿]+\s*|\s+", s)
    lines, cur = [], ""
    for tok in tokens:
        if cur and text_width(cur + tok.rstrip(), fs, bold) > width:
            lines.append(cur.rstrip())
            cur = tok.lstrip()
        else:
            cur += tok
    if cur.strip():
        lines.append(cur.rstrip())
    # 中文标点不放行首：挪回上一行末尾
    for i in range(1, len(lines)):
        while lines[i] and lines[i][0] in "。，、；：！？）」』》":
            lines[i - 1] += lines[i][0]
            lines[i] = lines[i][1:]
    return [l for l in lines if l]


def tspans(lines, x, y, lh):
    return "".join(f'<tspan x="{x}" y="{y + i * lh:.1f}">{t(l)}</tspan>' for i, l in enumerate(lines))


PALETTE = [PINK, ORANGE, PURPLE, LIME, BLUE, YELLOW, "#22D3EE"]
FADE = ("@keyframes up{from{opacity:0;transform:translateY(12px)}}"
        "@keyframes left{from{opacity:0;transform:translateX(-14px)}}")


def tint(col, theme):
    return col + ("22" if theme == "light" else "33")


# ---------------------------------------------------------------- section headings
def heading(data, key, lang, theme):
    icon, en, zh, col = data["headings"][key]
    c = THEMES[theme]
    title = en if lang == "en" else zh
    tw = text_width(title, 26, True)
    w, h = 880, 64
    wave = " ".join(f"q {9} {-6 if i % 2 else 6} 18 0" for i in range(int((tw + 20) / 18) + 1))
    body = (f'<circle cx="26" cy="30" r="22" fill="{tint(col, theme)}"/>'
            f'<text x="26" y="39" text-anchor="middle" font-size="24">{icon}</text>'
            f'<text x="62" y="39" font-family="{SANS}" font-size="26" font-weight="800" fill="{c["ink"]}">{t(title)}</text>'
            f'<path class="ink" d="M60 54 {wave}" fill="none" stroke="{col}" stroke-width="4" stroke-linecap="round" '
            f'pathLength="100"/>'
            f'<circle class="spark" cx="{min(w - 20, 76 + tw + 18)}" cy="20" r="4" fill="{col}"/>'
            f'<circle class="spark s2" cx="{min(w - 12, 76 + tw + 30)}" cy="32" r="2.5" fill="{col}"/>')
    style = (".ink{stroke-dasharray:100;animation:draw 1.1s ease-out .2s both}@keyframes draw{from{stroke-dashoffset:100}}"
             ".spark{animation:tw 2.4s ease-in-out infinite}.s2{animation-delay:1.2s}"
             "@keyframes tw{50%{opacity:.15}}")
    return svg(w, h, body, style, title)


# ---------------------------------------------------------------- timeline
def timeline(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    w, x0, tx, tw_, fs, lh = 880, 34, 194, 660, 15, 23
    y, parts = 14, []
    rows = data["timeline"]
    for i, (m_en, s_en, m_zh, s_zh) in enumerate(rows):
        col = PALETTE[i % len(PALETTE)]
        lines = wrap(s_zh if zh else s_en, fs, tw_)
        hh = max(52, len(lines) * lh + 26)
        last = i == len(rows) - 1
        d = 0.1 + i * 0.12
        parts.append(
            f'<g class="row" style="animation-delay:{d:.2f}s">'
            f'<rect x="{x0 + 34}" y="{y}" width="{w - x0 - 40}" height="{hh}" rx="14" fill="{c["card"]}" stroke="{c["line"]}"/>'
            f'<rect x="{x0 + 48}" y="{y + 14}" width="92" height="26" rx="13" fill="{col}"/>'
            f'<text x="{x0 + 94}" y="{y + 32}" text-anchor="middle" font-family="{SANS}" font-size="13.5" '
            f'font-weight="800" fill="#FFFFFF">{t(m_zh if zh else m_en)}</text>'
            f'<text font-family="{SANS}" font-size="{fs}" fill="{c["ink"]}">{tspans(lines, tx, y + 32, lh)}</text>'
            f'<circle cx="{x0}" cy="{y + 27}" r="{9 if last else 7}" fill="{col}" stroke="{c["bg"]}" stroke-width="3"/>'
            + (f'<circle class="pulse" cx="{x0}" cy="{y + 27}" r="9" fill="none" stroke="{col}" stroke-width="2"/>' if last else "")
            + '</g>')
        y += hh + 12
    h = y + 2
    rail = (f'<linearGradient id="rail" x1="0" y1="0" x2="0" y2="1">'
            + "".join(f'<stop offset="{k / 6:.2f}" stop-color="{PALETTE[k]}"/>' for k in range(7)) + '</linearGradient>')
    body = (f'<defs>{rail}</defs><rect x="{x0 - 2}" y="20" width="4" height="{h - 40}" rx="2" fill="url(#rail)" opacity=".7"/>'
            + "".join(parts))
    style = (".row{animation:left .6s cubic-bezier(.2,.8,.2,1) both}" + FADE +
             ".pulse{transform-box:fill-box;transform-origin:center;animation:pulse 1.8s ease-out infinite}"
             "@keyframes pulse{from{transform:scale(1);opacity:.9}to{transform:scale(2.4);opacity:0}}")
    label = " · ".join(r[2] if zh else r[0] for r in rows)
    return svg(w, h, body, style, label)


# ---------------------------------------------------------------- character sheet
def human(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    w = 880
    rows = data["human"]
    lx, vx, vw, fs, lh = 300, 424, 420, 14.5, 21
    y, parts = 78, []
    for i, (l_en, v_en, l_zh, v_zh) in enumerate(rows):
        col = PALETTE[i % len(PALETTE)]
        lines = wrap(v_zh if zh else v_en, fs, vw)
        d = 0.35 + i * 0.08
        parts.append(f'<g class="row" style="animation-delay:{d:.2f}s">'
                     f'<text x="{lx}" y="{y}" font-family="{SANS}" font-size="12" font-weight="800" letter-spacing="1" '
                     f'fill="{col}">{t((l_zh if zh else l_en).upper())}</text>'
                     f'<text font-family="{SANS}" font-size="{fs}" fill="{c["ink"]}">{tspans(lines, vx, y, lh)}</text></g>')
        y += len(lines) * lh + 10
    portrait = base64.b64encode((ASSETS / "portrait.jpg").read_bytes()).decode()
    bars = []
    by = 330
    for i, (en, zhl, v) in enumerate(data["human_stats"]):
        col = [ORANGE, PINK, BLUE, PURPLE][i]
        yy = by + i * 46
        bars.append(f'<text x="44" y="{yy}" font-family="{SANS}" font-size="11.5" font-weight="800" letter-spacing="1" '
                    f'fill="{c["muted"]}">{t(zhl if zh else en)}</text>'
                    f'<text x="252" y="{yy}" text-anchor="end" font-family="{MONO}" font-size="12" font-weight="700" '
                    f'fill="{col}">{v}</text>'
                    f'<rect x="44" y="{yy + 8}" width="208" height="10" rx="5" fill="{c["line"]}"/>'
                    + (f'<rect class="bar" x="44" y="{yy + 8}" width="{208 * v / 100:.0f}" height="10" rx="5" fill="{col}" '
                       f'style="animation-delay:{0.6 + i * 0.15:.2f}s"/>' if v else ""))
    bottom = max(y + 10, by + 4 * 46)
    motto = data["human_motto"][1 if zh else 0]
    mlines = wrap(motto, 15, w - 120)
    h = bottom + 24 + len(mlines) * 22 + 20
    head = "CHARACTER SHEET" if not zh else "角色卡"
    body = (f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" rx="22" fill="{c["card"]}" stroke="{c["line"]}" stroke-width="2"/>'
            f'<path d="M1 23a22 22 0 0 1 22-22h{w - 46}a22 22 0 0 1 22 22v21H1z" fill="{ORANGE}"/>'
            f'<text x="26" y="29" font-family="{MONO}" font-size="13" font-weight="700" letter-spacing="2" fill="#FFFFFF">'
            f'{t(head)}</text>'
            f'<text x="{w - 26}" y="29" text-anchor="end" font-family="{MONO}" font-size="13" font-weight="700" fill="#FFFFFF">'
            f'AliceLJY · Lv. 2026 · HP ∞</text>'
            f'<clipPath id="pc"><rect x="44" y="70" width="208" height="208" rx="24"/></clipPath>'
            f'<rect x="38" y="64" width="220" height="220" rx="28" fill="none" stroke="{ORANGE}" stroke-width="4" '
            f'stroke-dasharray="10 7" class="ring"/>'
            f'<image x="44" y="70" width="208" height="208" clip-path="url(#pc)" href="data:image/jpeg;base64,{portrait}"/>'
            + "".join(bars) + "".join(parts) +
            f'<line x1="44" y1="{bottom + 6}" x2="{w - 44}" y2="{bottom + 6}" stroke="{c["line"]}" stroke-dasharray="4 6"/>'
            f'<text font-family="{SANS}" font-size="15" font-style="italic" font-weight="600" fill="{ORANGE}" '
            f'text-anchor="middle">{tspans(mlines, w / 2, bottom + 38, 22)}</text>')
    style = (".row{animation:left .5s ease-out both}" + FADE +
             ".bar{transform-box:fill-box;transform-origin:left;animation:grow 1s cubic-bezier(.2,.8,.2,1) both}"
             "@keyframes grow{from{transform:scaleX(0)}}"
             ".ring{animation:spin 18s linear infinite}@keyframes spin{to{stroke-dashoffset:-170}}")
    label = "; ".join(f"{r[2] if zh else r[0]}: {r[3] if zh else r[1]}" for r in rows)
    return svg(w, h, body, style, label)


# ---------------------------------------------------------------- tech stack
def stack(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    w, lw, rx, rw, fs, lh = 880, 196, 236, 620, 14.5, 21
    (h_en_l, h_en_r, h_zh_l, h_zh_r), rows = data["stack"][0], data["stack"][1:]
    parts = [f'<text x="20" y="22" font-family="{SANS}" font-size="12" font-weight="800" letter-spacing="1.5" '
             f'fill="{c["muted"]}">{t((h_zh_l if zh else h_en_l).upper())}</text>'
             f'<text x="{rx + 6}" y="22" font-family="{SANS}" font-size="12" font-weight="800" letter-spacing="1.5" '
             f'fill="{PURPLE}">{t((h_zh_r if zh else h_en_r).upper())}</text>']
    y = 38
    for i, (l_en, r_en, l_zh, r_zh) in enumerate(rows):
        col = PALETTE[i % len(PALETTE)]
        left = l_zh if zh else l_en
        lines = wrap(r_zh if zh else r_en, fs, rw - 36)
        llines = wrap(left, 14, lw - 24)
        hh = max(40, len(lines) * lh + 18, len(llines) * 19 + 18)
        mid = y + hh / 2
        d = 0.08 + i * 0.07
        ltw = min(lw - 24, max(text_width(l, 14) for l in llines))
        parts.append(
            f'<g class="row" style="animation-delay:{d:.2f}s">'
            f'<text font-family="{SANS}" font-size="14" fill="{c["muted"]}">'
            f'{tspans(llines, 20, mid - (len(llines) - 1) * 9.5 + 5, 19)}</text>'
            + "".join(f'<line class="strike" x1="18" y1="{mid - (len(llines) - 1) * 9.5 + k * 19:.1f}" '
                      f'x2="{22 + min(ltw, text_width(l, 14))}" y2="{mid - (len(llines) - 1) * 9.5 + k * 19:.1f}" '
                      f'stroke="{PINK}" stroke-width="2" style="animation-delay:{d + 0.35:.2f}s"/>'
                      for k, l in enumerate(llines)) +
            f'<rect x="{rx}" y="{y}" width="{rw}" height="{hh}" rx="14" fill="{tint(col, theme)}"/>'
            f'<path d="M{rx} {mid - 7} l-9 7 l9 7z" fill="{tint(col, theme)}"/>'
            f'<rect x="{rx}" y="{y}" width="5" height="{hh}" rx="2.5" fill="{col}"/>'
            f'<text font-family="{SANS}" font-size="{fs}" fill="{c["ink"]}">'
            f'{tspans(lines, rx + 20, y + 14 + (hh - len(lines) * lh) / 2 + 2, lh)}</text></g>')
        y += hh + 10
    style = (".row{animation:up .5s ease-out both}" + FADE +
             ".strike{transform-box:fill-box;transform-origin:left;animation:grow .5s ease-out both}"
             "@keyframes grow{from{transform:scaleX(0)}}")
    label = "; ".join(f"{r[2] if zh else r[0]} → {r[3] if zh else r[1]}" for r in rows)
    return svg(w, y + 4, "".join(parts), style, label)


# ---------------------------------------------------------------- arsenal: pipeline, numbers, rules
def pipeline(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    w, nx, dx = 880, 24, 196
    cols = {"SCOUT": BLUE, "GATE": PINK, "SHELVE": PURPLE, "FETCH": LIME, "DRAW": ORANGE, "SHIP": YELLOW}
    y, parts, centers = 16, [], []
    for i, st in enumerate(data["arsenal_stages"]):
        key, en, zhname, zhd = st
        col = cols[key]
        d = 0.1 + i * 0.15
        if key == "GATE":
            gate = data["arsenal_gate"]
            hh = 44 + len(gate) * 40 + 10
            rowsvg = []
            for j, (n, q_en, note_en, q_zh, note_zh) in enumerate(gate):
                gy = y + 52 + j * 40
                rowsvg.append(f'<circle cx="{dx + 22}" cy="{gy}" r="12" fill="{col}"/>'
                              f'<text x="{dx + 22}" y="{gy + 4.5}" text-anchor="middle" font-family="{MONO}" font-size="13" '
                              f'font-weight="800" fill="#FFFFFF">{n}</text>'
                              f'<text x="{dx + 44}" y="{gy + 5}" font-family="{SANS}" font-size="14.5" font-weight="700" '
                              f'fill="{c["ink"]}">{t(q_zh if zh else q_en)}</text>'
                              f'<text x="{dx + 290}" y="{gy + 5}" font-family="{SANS}" font-size="13" fill="{c["muted"]}">'
                              f'{t(note_zh if zh else note_en)}</text>')
            box = (f'<rect x="{dx}" y="{y}" width="{w - dx - 16}" height="{hh}" rx="16" fill="{c["card"]}" '
                   f'stroke="{col}" stroke-width="2" stroke-dasharray="6 5"/>'
                   f'<text x="{dx + 18}" y="{y + 27}" font-family="{SANS}" font-size="14.5" font-weight="800" '
                   f'fill="{col}">{t(zhd if zh else en)}</text>' + "".join(rowsvg))
        else:
            lines = wrap(zhd if zh else en, 15, w - dx - 52)
            hh = max(48, len(lines) * 22 + 24)
            box = (f'<rect x="{dx}" y="{y}" width="{w - dx - 16}" height="{hh}" rx="16" fill="{c["card"]}" stroke="{c["line"]}"/>'
                   f'<text font-family="{SANS}" font-size="15" fill="{c["ink"]}">'
                   f'{tspans(lines, dx + 20, y + hh / 2 - (len(lines) - 1) * 11 + 5, 22)}</text>')
        cy = y + 24
        centers.append(cy)
        label = zhname if zh else key
        parts.append(f'<g class="row" style="animation-delay:{d:.2f}s">'
                     f'<rect x="{nx}" y="{cy - 17}" width="140" height="34" rx="17" fill="{col}"/>'
                     f'<text x="{nx + 70}" y="{cy + 5.5}" text-anchor="middle" font-family="{MONO}" font-size="14.5" '
                     f'font-weight="800" letter-spacing="1.5" fill="#FFFFFF">{t(label)}</text>{box}</g>')
        y += hh + 16
    rail = (f'<line x1="{nx + 70}" y1="{centers[0]}" x2="{nx + 70}" y2="{centers[-1]}" stroke="{c["line"]}" stroke-width="4"/>'
            f'<line class="flow" x1="{nx + 70}" y1="{centers[0]}" x2="{nx + 70}" y2="{centers[-1]}" stroke="{c["muted"]}" '
            f'stroke-width="4" stroke-dasharray="2 14" stroke-linecap="round"/>')
    style = (".row{animation:up .6s ease-out both}" + FADE +
             ".flow{animation:flow 1.2s linear infinite}@keyframes flow{to{stroke-dashoffset:-32}}")
    label = " → ".join(s[2] if zh else s[0] for s in data["arsenal_stages"])
    return svg(w, y, rail + "".join(parts), style, label)


def numbers(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    rows = data["arsenal_numbers"]["rows"]
    w, tw, th, gap = 880, 284, 112, 14
    parts = []
    for i, (l_en, v_en, l_zh, v_zh) in enumerate(rows):
        col = PALETTE[(i + 2) % len(PALETTE)]
        x, y = (i % 3) * (tw + gap), (i // 3) * (th + gap)
        v = v_zh if zh else v_en
        m = re.match(r"^\d[\d ·]*\d|^\d+", v)
        big = m.group(0) if m else re.search(r"\d+", v).group(0)
        rest = v[len(big):].strip(" ,，") if m else v
        sub = wrap(rest, 12, tw - 36)[:2] if rest else []
        parts.append(f'<g class="row" style="animation-delay:{0.1 + i * 0.1:.2f}s">'
                     f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="16" fill="{c["card"]}" stroke="{c["line"]}"/>'
                     f'<rect x="{x}" y="{y + 18}" width="5" height="{th - 36}" rx="2.5" fill="{col}"/>'
                     f'<text x="{x + 20}" y="{y + 44}" font-family="{SANS}" font-size="32" font-weight="800" fill="{col}">'
                     f'{t(big)}</text>'
                     f'<text x="{x + 20}" y="{y + 68}" font-family="{SANS}" font-size="13.5" font-weight="700" '
                     f'fill="{c["ink"]}">{t(l_zh if zh else l_en)}</text>'
                     f'<text font-family="{SANS}" font-size="12" fill="{c["muted"]}">{tspans(sub, x + 20, y + 88, 16)}</text>'
                     f'</g>')
    h = 2 * (th + gap) + 14
    foot = (f"as of {data['arsenal_numbers']['as_of']}" if not zh else f"数字截至 {data['arsenal_numbers']['as_of']}")
    parts.append(f'<text x="{w / 2}" y="{h - 2}" text-anchor="middle" font-family="{SANS}" font-size="11.5" '
                 f'fill="{c["muted"]}">{t(foot)}</text>')
    label = "; ".join(f"{r[2] if zh else r[0]}: {r[3] if zh else r[1]}" for r in rows)
    return svg(w, h, "".join(parts), ".row{animation:up .6s ease-out both}" + FADE, label)


def rules(data, lang, theme):
    c, zh = THEMES[theme], lang == "zh"
    w, cw, gap = 880, 433, 14
    items = data["arsenal_rules"]
    laid = []
    for i, (ti_en, b_en, ti_zh, b_zh) in enumerate(items):
        lone = i == len(items) - 1 and len(items) % 2 == 1
        width = (w if lone else cw) - 76
        tl = wrap(ti_zh if zh else ti_en, 16, width, True)
        bl = wrap(b_zh if zh else b_en, 13.5, width)
        laid.append((tl, bl, 30 + len(tl) * 22 + len(bl) * 20 + 14))
    parts, y = [], 0
    for r in range(0, len(laid), 2):
        pair = laid[r:r + 2]
        full = len(pair) == 1
        hh = max(p[2] for p in pair)
        for k, (tl, bl, _) in enumerate(pair):
            i = r + k
            col = PALETTE[i % len(PALETTE)]
            x = k * (cw + gap)
            ww = w if full else cw
            parts.append(f'<g class="row" style="animation-delay:{0.1 + i * 0.12:.2f}s">'
                         f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" rx="16" fill="{tint(col, theme)}"/>'
                         f'<text x="{x + 30}" y="{y + 46}" text-anchor="middle" font-family="{SANS}" font-size="34" '
                         f'font-weight="800" fill="{col}">{i + 1}</text>'
                         f'<text font-family="{SANS}" font-size="16" font-weight="800" fill="{c["ink"]}">'
                         f'{tspans(tl, x + 58, y + 32, 22)}</text>'
                         f'<text font-family="{SANS}" font-size="13.5" fill="{c["muted"]}">'
                         f'{tspans(bl, x + 58, y + 32 + len(tl) * 22 + 4, 20)}</text></g>')
        y += hh + gap
    label = "; ".join(r[2] if zh else r[0] for r in items)
    return svg(w, y, "".join(parts), ".row{animation:up .6s ease-out both}" + FADE, label)


def main():
    data = json.loads((ROOT / "profile.json").read_text(encoding="utf-8"))
    for lang in ("en", "zh"):
        write(f"now-{lang}.svg", now(data, lang))
        for theme in THEMES:
            write(f"stats-{lang}-{theme}.svg", stats(data, lang, theme))
            write(f"empire-{lang}-{theme}.svg", empire(data, lang, theme))
            write(f"timeline-{lang}-{theme}.svg", timeline(data, lang, theme))
            write(f"human-{lang}-{theme}.svg", human(data, lang, theme))
            write(f"stack-{lang}-{theme}.svg", stack(data, lang, theme))
            write(f"arsenal-flow-{lang}-{theme}.svg", pipeline(data, lang, theme))
            write(f"arsenal-numbers-{lang}-{theme}.svg", numbers(data, lang, theme))
            write(f"arsenal-rules-{lang}-{theme}.svg", rules(data, lang, theme))
            for key in data["headings"]:
                write(f"headings/{key}-{lang}-{theme}.svg", heading(data, key, lang, theme))
        for item in data["showcase"]:
            write(f"showcase/{item['slug']}-{lang}.svg", showcase_card(item, lang))
    print("rendered into", ASSETS)


if __name__ == "__main__":
    main()
