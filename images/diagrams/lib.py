import math
from xml.sax.saxutils import escape

THEMES = {
    False: dict(ground="#FFFFFF", hair="#D8D8D2", ink="#16181D", sub="#5D636B", zone="#8A9098", accent="#2C2E6B"),
    True:  dict(ground="#0E1118", hair="#262B36", ink="#F5F5F2", sub="#A3A9B1", zone="#8A9098", accent="#7D8CFF"),
}

# "big" sizes are for diagrams drawn at the width of a docs column (about 340 wide),
# so that no label drops under 11px once the image is scaled into the column.
def style(t, big=False):
    if big:
        return f"""<style>
  .lbl  {{ font-family:"Geist",sans-serif; font-size:13px; font-weight:500; fill:{t['ink']}; }}
  .sub  {{ font-family:"Geist Mono",monospace; font-size:11px; letter-spacing:.02em; fill:{t['sub']}; }}
  .zone {{ font-family:"Geist Mono",monospace; font-size:11px; letter-spacing:.08em; fill:{t['zone']}; }}
  .step {{ font-family:"Geist Mono",monospace; font-size:11px; letter-spacing:.04em; fill:{t['accent']}; }}
  .acc  {{ font-family:"Geist",sans-serif; font-size:13px; font-weight:500; fill:{t['accent']}; }}
</style>"""
    return f"""<style>
  .lbl  {{ font-family:"Geist",sans-serif; font-size:12px; font-weight:500; fill:{t['ink']}; }}
  .sub  {{ font-family:"Geist Mono",monospace; font-size:9px; letter-spacing:.03em; fill:{t['sub']}; }}
  .zone {{ font-family:"Geist Mono",monospace; font-size:8.6px; letter-spacing:.13em; fill:{t['zone']}; }}
  .step {{ font-family:"Geist Mono",monospace; font-size:9px; letter-spacing:.07em; fill:{t['accent']}; }}
  .acc  {{ font-family:"Geist",sans-serif; font-size:12px; font-weight:500; fill:{t['accent']}; }}
</style>"""

class D:
    def __init__(self, w, h, aria, dark=False, big=False):
        self.w, self.h, self.aria, self.big = w, h, aria, big
        self.sub0, self.subd = (15, 14) if big else (12, 11)
        self.stepdx = 16 if big else 14
        self.t = THEMES[dark]
        self.o = []
    def add(self, s): self.o.append(s)
    def text(self, x, y, s, cls='sub', anchor='start'):
        self.add(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}">{escape(s)}</text>')
    def zone(self, x, y, w, h, label):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{self.t["hair"]}" stroke-width="1"/>')
        self.text(x+(12 if self.big else 10), y+(19 if self.big else 16), label.upper(), 'zone')
    def box(self, x, y, w, h):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{self.t["hair"]}" stroke-width="1"/>')
    def accent_box(self, x, y, w, h):
        self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="{self.t["accent"]}" stroke-width="1"/>')
    def node(self, x, y, label, subs=(), num=None):
        """y is the label baseline; subs below at +12, +11 steps."""
        dx = 0
        if num is not None:
            self.text(x, y, str(num), 'step'); dx = self.stepdx if num < 10 else self.stepdx + 6
        self.text(x+dx, y, label, 'lbl')
        for i, s in enumerate(subs):
            self.text(x+dx, y+self.sub0+i*self.subd, s)
    def arrow(self, pts, dashed=False, color=None, dotted=False, head=True):
        color = color or self.t["ink"]
        pts = list(pts)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        L = math.hypot(x2-x1, y2-y1); ux, uy = (x2-x1)/L, (y2-y1)/L
        px, py = -uy, ux
        end = (x2-5*ux, y2-5*uy) if head else (x2, y2)
        body = pts[:-1] + [end]
        dash = ' stroke-dasharray="3 3"' if dashed else (' stroke-dasharray="1.5 2.5"' if dotted else '')
        p = ' '.join(f'{round(a,1)},{round(b,1)}' for a, b in body)
        self.add(f'<polyline points="{p}" fill="none" stroke="{color}" stroke-width="1"{dash}/>')
        if head:
            b = (x2-6*ux, y2-6*uy)
            self.add(f'<polygon points="{round(x2,1)},{round(y2,1)} {round(b[0]+3*px,1)},{round(b[1]+3*py,1)} {round(b[0]-3*px,1)},{round(b[1]-3*py,1)}" fill="{color}"/>')
    def line(self, x1, y1, x2, y2, color=None, dashed=False):
        color = color or self.t["ink"]
        dash = ' stroke-dasharray="3 3"' if dashed else ''
        self.add(f'<line fill="none" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="1"{dash}/>')
    def dot(self, x, y, r=3.2, fill=None):
        fill = fill or self.t["ink"]
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
    def ring(self, x, y, r=3.2):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{self.t["ground"]}" stroke="{self.t["ink"]}" stroke-width="1"/>')
    def span(self, x1, x2, y, tick=4):
        self.line(x1, y, x2, y)
        self.line(x1, y-tick, x1, y+tick); self.line(x2, y-tick, x2, y+tick)
    def save(self, path):
        head = (f'<svg viewBox="0 0 {self.w} {self.h}" xmlns="http://www.w3.org/2000/svg" role="img"\n'
                f'   aria-label="{escape(self.aria, {chr(34): "&quot;"})}">\n{style(self.t, self.big)}\n'
                f'<rect x="0" y="0" width="{self.w}" height="{self.h}" fill="{self.t["ground"]}"/>\n')
        open(path, 'w').write(head + '\n'.join(self.o) + '\n</svg>\n')
