"""Writes how-it-works.svg and how-it-works-dark.svg. Run: python3 how-it-works.py

Colour carries meaning only: the accent marks the step numbers, what goes to
Sanning (signed hashes, no content) and the stamp. Everything else is ink and hairline.
The font stack falls back to system fonts because an SVG in an img tag cannot load Geist.
"""
import os
from lib import D

ARIA = ("How Sanning works. Your agent and its adapter capture each step. The content goes to your own log "
        "store. Only signed hashes go to Sanning, which seals the records into a stamp on the public record "
        "at each interval. You build the evidence pack from Sanning's records and stamp proofs and your own "
        "content, and hand it to the reviewer. The reviewer verifies it on their own machine and checks "
        "the stamps on the public record, and does not need Sanning.")


def build(dark=False):
    d = D(840, 400, ARIA, dark)
    t = d.t

    d.zone(10, 10, 230, 380, "Your systems")
    d.box(24, 34, 202, 58)
    d.node(36, 58, "Your agent + adapter", ["captures each step"], num=1)
    d.box(24, 150, 202, 58)
    d.node(36, 176, "Your log store", ["your content, kept by you"])
    d.box(24, 290, 202, 84)
    d.node(36, 316, "Evidence pack", ["Sanning's records and stamp", "proofs, plus your content"])
    d.arrow([(125, 92), (125, 150)])
    d.text(133, 125, "content")
    d.arrow([(125, 208), (125, 290)])
    d.text(133, 252, "your content")

    d.zone(340, 10, 190, 96, "Sanning")
    d.node(354, 58, "Receives the records", ["seals them into a stamp"])
    d.arrow([(240, 58), (340, 58)], color=t["accent"])
    d.text(290, 48, "2  Sign", 'step', anchor='middle')
    d.text(290, 78, "signed hashes,", 'step', anchor='middle')
    d.text(290, 89, "no content", 'step', anchor='middle')

    d.zone(630, 10, 200, 96, "Public record")
    d.accent_box(644, 36, 172, 52)
    d.text(656, 58, "The stamp", 'acc')
    d.text(656, 70, "shows when the records")
    d.text(656, 81, "existed")
    d.arrow([(530, 58), (630, 58)])
    d.text(580, 48, "3  Anchor", 'step', anchor='middle')
    d.text(580, 78, "one stamp", anchor='middle')
    d.text(580, 89, "per interval", anchor='middle')

    d.arrow([(350, 106), (350, 310), (226, 310)])
    d.text(358, 200, "records and")
    d.text(358, 211, "stamp proofs")

    d.zone(400, 290, 240, 100, "The reviewer")
    d.node(414, 336, "Verifies", ["on their own machine"], num=4)
    d.arrow([(226, 352), (400, 352)])
    d.text(313, 344, "hands over", anchor='middle')
    d.arrow([(640, 352), (730, 352), (730, 106)], dashed=True)
    d.text(738, 240, "checks the")
    d.text(738, 251, "stamp")

    # Sanning is not needed to verify: a dashed link with a cross.
    d.line(470, 106, 470, 190, color=t["zone"], dashed=True)
    d.line(470, 210, 470, 290, color=t["zone"], dashed=True)
    d.ring(470, 200, 9)
    d.line(466, 196, 474, 204, color=t["ink"])
    d.line(474, 196, 466, 204, color=t["ink"])
    d.text(486, 203, "not needed to verify")
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for dark, name in ((False, "how-it-works.svg"), (True, "how-it-works-dark.svg")):
        path = f"{here}/{name}"
        build(dark).save(path)
        s = open(path).read()
        s = s.replace('"Geist",sans-serif', '"Geist",ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif')
        s = s.replace('"Geist Mono",monospace', '"Geist Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace')
        open(path, "w").write(s)
