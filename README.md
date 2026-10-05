# aglassett.com

Portfolio site for Andrew Glassett — Senior Product Designer & Consultant.

Plain HTML, CSS, and a few lines of vanilla JavaScript. No frameworks, no build step. Brutalist and minimal by design.

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
├── css/style.css         # All styles
└── js/main.js            # Hover preview on the work index
```

All links are relative, so the site works at a custom domain or at a GitHub Pages project URL.

## Running locally

```bash
python3 -m http.server 4000
```

Then open http://localhost:4000.
