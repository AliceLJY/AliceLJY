#!/usr/bin/env python3
"""Refresh the numbers in profile.json from GitHub, then the stats cards get re-rendered.

    GITHUB_TOKEN=... python3 scripts/refresh_stats.py

Counts:
  public repos   owned, not forks; archived ones count as retired
  merged PRs     authored by AliceLJY, in public repos only (the Action token cannot see
                 private ones, and anyone can verify a public count); "elsewhere" = not owned by AliceLJY
  playground     cards per shelf on the playground front page

Any failed request raises, so the Action run turns red and the old numbers stay.
"""
import datetime
import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

USER = "AliceLJY"
ROOT = Path(__file__).resolve().parent.parent
API = "https://api.github.com"


def get(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": "profile-refresh"})
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        body = r.read().decode("utf-8")
    return body if raw else json.loads(body)


def merged(query):
    q = urllib.parse.quote(f"is:pr is:public author:{USER} is:merged {query}".strip())
    return get(f"{API}/search/issues?q={q}&per_page=1")["total_count"]


def main():
    repos, page = [], 1
    while True:
        batch = get(f"{API}/users/{USER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            break
        page += 1
    own = [r for r in repos if not r["fork"] and not r["private"]]
    retired = sum(1 for r in own if r["archived"])

    html = get(f"https://raw.githubusercontent.com/{USER}/playground/main/index.html", raw=True)
    shelves = {}
    for chunk in re.split(r'<h2 class="shelf">', html)[1:]:
        title = chunk.split("<", 1)[0].strip()
        shelves[title] = len(re.findall(r'class="card"', chunk))
    need = ["小游戏", "3D 展页", "AI 幕后"]
    if not all(k in shelves for k in need):
        raise SystemExit(f"playground shelves changed, found {list(shelves)}")

    path = ROOT / "profile.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    s = data["stats"]
    fresh = {
        "public_active": len(own) - retired,
        "public_retired": retired,
        "merged_prs": merged(""),
        "merged_prs_elsewhere": merged(f"-user:{USER}"),
        "playground_games": shelves["小游戏"],
        "playground_exhibits": shelves["3D 展页"],
        "playground_behind": shelves["AI 幕后"],
        "playground_tools": sum(v for k, v in shelves.items() if k not in need),
    }
    if all(s.get(k) == v for k, v in fresh.items()):
        print("no number moved")
        return
    s.update(fresh, as_of=datetime.date.today().isoformat())  # as_of = when a number last moved
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(s, ensure_ascii=False))


if __name__ == "__main__":
    main()
