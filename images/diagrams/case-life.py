"""Writes case-life.svg, case-life-review.svg and their -dark twins.
Run: python3 case-life.py, then python3 render.py <names> for the PNGs the pages show.

Drawn 340 wide, the width of a docs column on a phone, with 11px labels at the least.
The picture is split in two, one under the other: the case over time, then the
evidence pack, the reviewer and the verdict.
"""
import os
from lib import D

ARIA = ("The life of one case. Two agents work on one case over time. Every record in their three runs "
        "carries the case ID. The intake agent has run 1. The review agent has run 2 and run 3. A run ends "
        "with a closing record. At the end of each interval, Sanning seals the new records into a stamp "
        "on the public record. Time runs from left to right.")

ARIA_REVIEW = ("What happens to the case's records. You build one evidence pack for the case, from the "
               "records, the stamp proofs and your own content, and hand it to the reviewer. The reviewer "
               "checks the pack on their own machine, checks the stamps on the public record, and reads "
               "the verdict.")


def pill(d, x1, x2, y, label):
    d.text(x1 + 2, y - 15, label)
    d.add(f'<rect x="{x1}" y="{y - 10}" width="{x2 - x1}" height="20" rx="10" fill="none" '
          f'stroke="{d.t["hair"]}" stroke-width="1"/>')


def square(d, x, y, fill=None):
    fill = fill or d.t["ink"]
    d.add(f'<rect x="{x - 3.5}" y="{y - 3.5}" width="7" height="7" fill="{fill}"/>')


def run(d, x1, x2, y, label, dots, close_x):
    pill(d, x1, x2, y, label)
    for x in dots:
        d.dot(x, y)
    square(d, close_x, y)


def case(dark=False):
    d = D(340, 436, ARIA, dark, big=True)

    d.zone(10, 10, 320, 222, "Your agents, one case")
    d.text(24, 56, "case-4b19de is on every record", 'acc')
    d.text(24, 86, "Intake agent", 'lbl')
    run(d, 22, 160, 122, "run 1", [38, 53, 68, 83, 98], 146)
    d.text(24, 166, "Review agent", 'lbl')
    run(d, 168, 240, 202, "run 2", [180, 194, 208], 229)
    run(d, 248, 320, 202, "run 3", [260, 274, 288], 309)

    d.zone(10, 262, 320, 100, "Public record")
    for x in (128, 219, 298):
        d.line(x, 232, x, 296, dashed=True)
        d.add(f'<rect x="{x - 7}" y="296" width="14" height="14" fill="none" stroke="{d.t["accent"]}" stroke-width="1.5"/>')
    d.text(24, 308, "stamps", 'acc')
    d.text(24, 336, "a stamp at the end of each interval")
    d.text(24, 350, "seals the new records")

    d.arrow([(22, 392), (288, 392)])
    d.text(298, 396, "time")
    d.dot(28, 418, 3.2)
    d.text(38, 422, "record")
    square(d, 104, 418)
    d.text(114, 422, "closing record of a run")
    return d


def review(dark=False):
    d = D(340, 430, ARIA_REVIEW, dark, big=True)

    d.zone(10, 10, 320, 52, "Your agents, one case")
    d.text(24, 50, "case-4b19de is on every record", 'acc')
    d.arrow([(60, 62), (60, 102)])
    d.text(68, 86, "build")

    d.zone(10, 102, 320, 92, "You")
    d.node(24, 148, "Evidence pack", ["records, stamp proofs", "and your content"])
    d.arrow([(60, 194), (60, 234)])
    d.text(68, 218, "hand over")

    d.zone(10, 234, 320, 90, "The reviewer")
    d.accent_box(22, 262, 296, 50)
    d.text(36, 286, "Verdict", 'acc')
    d.text(36, 301, "checked on their machine")
    d.arrow([(300, 324), (300, 364)], dashed=True)
    d.text(292, 348, "checks", anchor='end')

    d.zone(10, 364, 320, 56, "Public record")
    d.text(24, 408, "stamps", 'acc')
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in (("case-life", case), ("case-life-review", review)):
        fn().save(f"{here}/{name}.svg")
        fn(True).save(f"{here}/{name}-dark.svg")
