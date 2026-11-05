"""Render NAME.svg to NAME.png (the PNG is what the page shows: an SVG in an img tag cannot load the Geist fonts) at 2x with the design system's Geist fonts.

Usage: python3 render.py NAME [NAME ...]
Needs SANNING_DESIGN_SYSTEM (a sanning-design-system checkout, for the fonts) and
CHROME (a headless Chromium binary, for example Playwright's chrome-headless-shell).
"""
import sys, re, subprocess, os, tempfile
OUT = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(os.environ["SANNING_DESIGN_SYSTEM"], "assets/fonts/geist")
CH = os.environ["CHROME"]
for name in sys.argv[1:]:
    svg = open(f"{OUT}/{name}.svg").read()
    m = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg); w, h = int(m[1]), int(m[2])
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:"Geist";src:url("file://{F}/Geist-Variable.ttf") format("truetype");font-weight:100 900}}
@font-face{{font-family:"Geist Mono";src:url("file://{F}/GeistMono-Variable.ttf") format("truetype");font-weight:100 900}}
html,body{{margin:0;background:#fff}} svg{{display:block}}</style></head><body>{svg.replace('<svg ', f'<svg width="{w}" height="{h}" ',1)}</body></html>"""
    p = os.path.join(tempfile.gettempdir(), f"render-{name}.html")
    open(p, "w").write(html)
    r = subprocess.run([CH, "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2", f"--window-size={w},{h}", "--virtual-time-budget=3000", f"--screenshot={OUT}/{name}.png", "file://" + p], capture_output=True, text=True)
    print(name, r.returncode, r.stderr[-200:])
