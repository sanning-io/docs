"""Writes how-it-works-capture.svg, how-it-works-verify.svg and their -dark twins.
Run: python3 how-it-works.py, then python3 render.py <names> for the PNGs the pages show.

Drawn 340 wide, the width of a docs column on a phone, with 11px labels at the least,
so the labels stay readable when the image is scaled into the column. The flow is
split in two, one under the other: steps 1 to 3 (capture, sign, anchor) and step 4
(hand over, verify).

Colour carries meaning only: the accent marks the step numbers, what goes to
Sanning (signed hashes, no content) and the stamp. Everything else is ink and hairline.
"""
import os
from lib import D

ARIA_CAPTURE = ("How Sanning works, steps 1 to 3. Your agent and its adapter capture each step. "
                "The content goes to your own log store. Only signed hashes go to Sanning, with no "
                "content. Sanning receives the records and seals them into a stamp, and puts one "
                "stamp per interval on the public record. The stamp shows when the records existed.")

ARIA_VERIFY = ("How Sanning works, step 4. Sanning's records and stamp proofs, and your content "
               "from your log store, make the evidence pack. You hand the pack to the reviewer, who "
               "verifies it on their own machine. The reviewer also checks the stamp on the public "
               "record. Sanning is not needed to verify.")


def stamp_box(d, y):
    d.accent_box(22, y, 296, 46)
    d.text(36, y + 24, "The stamp", 'acc')
    d.text(36, y + 39, "shows when the records existed")


def capture(dark=False):
    d = D(340, 436, ARIA_CAPTURE, dark, big=True)
    t = d.t

    d.zone(10, 10, 320, 166, "Your systems")
    d.box(22, 38, 296, 50)
    d.node(34, 62, "Your agent + adapter", ["captures each step"], num=1)
    d.arrow([(60, 88), (60, 114)])
    d.text(68, 105, "content")
    d.box(22, 114, 248, 50)
    d.node(34, 138, "Your log store", ["your content, kept by you"])

    d.arrow([(300, 88), (300, 220)], color=t["accent"])
    d.text(292, 194, "2  Sign", 'step', anchor='end')
    d.text(292, 208, "signed hashes, no content", 'step', anchor='end')

    d.zone(10, 220, 320, 76, "Sanning")
    d.node(24, 266, "Receives the records", ["seals them into a stamp"])

    d.arrow([(300, 296), (300, 340)])
    d.text(292, 313, "3  Anchor", 'step', anchor='end')
    d.text(292, 327, "one stamp per interval", anchor='end')

    d.zone(10, 340, 320, 86, "Public record")
    stamp_box(d, 368)
    return d


def verify(dark=False):
    d = D(340, 588, ARIA_VERIFY, dark, big=True)
    t = d.t

    d.zone(10, 10, 320, 72, "Sanning")
    d.node(24, 56, "Receives the records", ["seals them into a stamp"])

    d.arrow([(300, 82), (300, 226)])
    d.text(292, 106, "records and stamp proofs", anchor='end')

    d.zone(10, 122, 320, 184, "Your systems")
    d.box(22, 150, 248, 50)
    d.node(34, 174, "Your log store", ["your content, kept by you"])
    d.arrow([(60, 200), (60, 226)])
    d.text(68, 217, "your content")
    d.box(22, 226, 296, 68)
    d.node(34, 250, "Evidence pack", ["Sanning's records and stamp", "proofs, plus your content"])

    d.arrow([(60, 294), (60, 346)])
    d.text(68, 328, "hands over")

    d.zone(10, 346, 320, 106, "The reviewer")
    d.node(24, 392, "Verifies", ["on their own machine"], num=4)
    # Sanning is not needed to verify: a ring with a cross.
    d.ring(32, 434, 8)
    d.line(28.5, 430.5, 35.5, 437.5, color=t["ink"])
    d.line(35.5, 430.5, 28.5, 437.5, color=t["ink"])
    d.text(48, 438, "Sanning: not needed to verify")

    d.arrow([(300, 452), (300, 492)], dashed=True)
    d.text(292, 476, "checks the stamp", anchor='end')

    d.zone(10, 492, 320, 86, "Public record")
    stamp_box(d, 520)
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in (("how-it-works-capture", capture), ("how-it-works-verify", verify)):
        fn().save(f"{here}/{name}.svg")
        fn(True).save(f"{here}/{name}-dark.svg")
