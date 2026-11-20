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


def main():
    data = json.loads((ROOT / "profile.json").read_text(encoding="utf-8"))
    for lang in ("en", "zh"):
        write(f"now-{lang}.svg", now(data, lang))
        for theme in THEMES:
            write(f"stats-{lang}-{theme}.svg", stats(data, lang, theme))
            write(f"empire-{lang}-{theme}.svg", empire(data, lang, theme))
        for item in data["showcase"]:
            write(f"showcase/{item['slug']}-{lang}.svg", showcase_card(item, lang))
    print("rendered into", ASSETS)


if __name__ == "__main__":
    main()
