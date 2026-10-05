# aglassett.com

Portfolio site for Andrew Glassett — Senior Product Designer & Consultant.

Plain HTML, CSS, and a few lines of vanilla JavaScript. No frameworks. Brutalist and minimal by design.

## Structure

```
├── index.html            # Home: hero + work index
├── about/                # Bio, work history, side projects
├── work/
│   ├── sony-payments/    # 01 Royalty payments — The Orchard / Sony Music
│   ├── anvil/            # 02 Entrepreneur advice marketplace — Anvil
│   ├── tenspot/          # 03 Hybrid workforce software — Ten Spot
│   ├── alteryx/          # 04 Admin & licensing portal — Alteryx
│   ├── orchard/          # 05 Inventory management redesign — The Orchard
│   ├── walmart/          # 06 Coffee maker finder — Walmart / Eko
│   ├── vimeo/            # 07 Mobile web video optimization — Vimeo
│   └── design-system/    # 08 Lean design system — Sony Music
├── images/<project>/     # WebP images, 01.webp is each project's cover
├── resume/               # Downloadable resume PDF (linked from every page)
├── src/work/<slug>.html  # Case study sources (edit these, not work/)
├── build.py              # Builds work/<slug>/index.html from src/work
├── css/style.css         # All styles
└── js/main.js            # Hover preview on the work index
```

All links are relative, so the site works at a custom domain or at a GitHub Pages project URL.

## Editing case studies

Case study pages are generated. Edit `src/work/<slug>.html`, then run:

```bash
python3 build.py
```

Each source file starts with `key: value` lines (title, role, TL;DR summary,
`kpi1`–`kpi3` as `value | label`, and `tldr_bg`, the TL;DR background color
sampled from the cover image), then a blank line, then the article sections.
`[img 05 Alt text|Caption]` expands to a figure for `images/<slug>/05.webp`.

The home and about pages are plain HTML, edited directly.

## Running locally

```bash
python3 -m http.server 4000
```

Then open http://localhost:4000.
