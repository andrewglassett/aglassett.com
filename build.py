"""Build the case study pages.

Each file in src/work/<slug>.html starts with `key: value` lines, then a blank
line, then the article sections. This script wraps them in the shared page
shell and writes work/<slug>/index.html.

    python3 build.py

Shorthand inside a source file:
    [img 05 Alt text|Optional caption]  ->  <figure> for images/<slug>/05.webp
"""
import glob
import os
import re

RESUME = "resume/Andrew-Glassett_Senior-Product-Designer.pdf"
META_FIELDS = ["Role", "Skills", "Deliverable", "Length", "Status"]


def text_color(hex_bg):
    """Black or paper text, whichever reads better on the TL;DR background."""
    r, g, b = (int(hex_bg[i:i + 2], 16) / 255 for i in (1, 3, 5))
    lin = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    lum = 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)
    return "#000" if lum > 0.22 else "#f2f1ec"


def build(src):
    raw = open(src, encoding="utf-8").read()
    head, body = raw.split("\n\n", 1)
    m = dict(line.split(": ", 1) for line in head.strip().splitlines())
    slug = m["slug"]
    up = "../../"

    meta = "".join(
        f'\n      <div><dt>{k}</dt><dd>{m[k]}</dd></div>' for k in META_FIELDS if k in m
    )
    kpis = "".join(
        '\n          <li><strong>{}</strong><span>{}</span></li>'.format(*[p.strip() for p in m[k].split("|", 1)])
        for k in sorted(m) if k.startswith("kpi")
    )
    bg = m["tldr_bg"]

    page = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{m['title']} — Andrew Glassett</title>
  <meta name="description" content="{m['description']}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;800;900&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
  <link rel="stylesheet" href="{up}css/style.css">
  <link rel="icon" href="{up}favicon.svg" type="image/svg+xml">
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>

  <header class="site-header">
    <a class="home" href="{up}">Andrew Glassett</a>
    <nav aria-label="Primary">
      <a href="{up}#work" aria-current="page">Work</a>
      <a href="{up}about/">About</a>
      <a href="{up}{RESUME}" download>Resume ↓</a>
    </nav>
  </header>

  <main id="main">
    <header class="case-head">
      <p class="label">{m['num']} / {m['client']}</p>
      <h1>{m['h1']}</h1>
    </header>

    <dl class="meta">{meta}
    </dl>

    <div class="case-intro">
      <aside class="tldr" style="--tldr-bg: {bg}; --tldr-ink: {text_color(bg)}" aria-label="Summary">
        <p class="label">TL;DR</p>
        <p class="tldr-summary">{m['tldr']}</p>
        <ul class="tldr-kpis">{kpis}
        </ul>
      </aside>
      <figure class="cover"><img src="{up}images/{slug}/01.webp" alt="{m['cover_alt']}" width="1800" height="{m.get('cover_h', '935')}"></figure>
    </div>

    <article class="case">
{body.rstrip()}
    </article>

    <a class="next" href="../{m['next_slug']}/"><span class="label">Next — {m['next_num']}</span><strong>{m['next_title']}</strong></a>
  </main>

  <footer class="site-footer">
    <a class="cta" href="mailto:andrewglassett@gmail.com">Let's talk</a>
    <ul class="links">
      <li><a href="mailto:andrewglassett@gmail.com">andrewglassett@gmail.com</a></li>
      <li><a href="https://www.linkedin.com/in/andrewglassett/" target="_blank" rel="noopener">LinkedIn ↗</a></li>
      <li><a href="{up}{RESUME}" download>Resume ↓</a></li>
      <li>Fort Collins, CO</li>
    </ul>
  </footer>
</body>
</html>
'''

    def figure(mm):
        alt, _, cap = mm.group(2).partition("|")
        caption = f"<figcaption>{cap.strip()}</figcaption>" if cap.strip() else ""
        return f'<figure><img src="{up}images/{slug}/{mm.group(1)}.webp" alt="{alt.strip()}" loading="lazy">{caption}</figure>'

    page = re.sub(r"\[img (\d\d) ([^\]]*)\]", figure, page)

    out = f"work/{slug}/index.html"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w", encoding="utf-8").write(page)
    print("built", out)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    for src in sorted(glob.glob("src/work/*.html")):
        build(src)
