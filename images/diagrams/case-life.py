"""Writes case-life.svg and case-life-dark.svg. Run: python3 case-life.py"""
import os
from lib import D

ARIA = ("The life of one case. Two agents work on one case over time. Every record in their three runs "
        "carries the case ID. A run ends with a closing record. At the end of each interval, Sanning "
        "seals the new records into a stamp on the public record. You build one evidence pack for the "
        "case, from the records and your own content. The reviewer checks the pack on their own machine, checks the "
        "stamps on the public record, and reads the verdict.")


def pill(d, x1, x2, y, label):
    d.text(x1, y - 15, label)
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


def build(dark=False):
    d = D(760, 330, ARIA, dark)

    d.zone(10, 10, 510, 150, "Your agents, one case")
    d.text(24, 46, "CASE_ID is on every record", 'acc')
    d.text(24, 84, "Intake agent", 'lbl')
    d.text(24, 134, "Review agent", 'lbl')
    run(d, 130, 290, 84, "run 1", [146, 170, 194, 218, 242], 268)
    run(d, 300, 410, 134, "run 2", [316, 340, 364], 390)
    run(d, 420, 512, 134, "run 3", [434, 458, 480], 498)

    d.zone(10, 180, 510, 90, "Public record")
    for x in (250, 370, 490):
        d.line(x, 160, x, 216, dashed=True)
        d.add(f'<rect x="{x - 7}" y="216" width="14" height="14" fill="none" stroke="{d.t["accent"]}" stroke-width="1.5"/>')
    d.text(24, 224, "stamps", 'acc')
    d.text(24, 252, "a stamp at the end of each interval seals the new records")

    d.arrow([(130, 298), (512, 298)])
    d.text(520, 301, "time")
    d.dot(30, 316, 3.2)
    d.text(40, 319, "record")
    square(d, 100, 316)
    d.text(110, 319, "closing record of a run")

    d.zone(570, 10, 180, 96, "You")
    d.node(584, 58, "Evidence pack", ["records, stamp proofs", "and your content"])
    d.arrow([(520, 58), (570, 58)])
    d.text(545, 50, "build", anchor='middle')

    d.zone(570, 180, 180, 90, "The reviewer")
    d.accent_box(580, 200, 160, 52)
    d.text(592, 222, "Verdict", 'acc')
    d.text(592, 236, "checked on their machine")
    d.arrow([(660, 106), (660, 180)])
    d.text(668, 148, "hand over")
    d.arrow([(570, 226), (520, 226)], dashed=True)
    d.text(545, 218, "checks", anchor='middle')
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    build().save(f"{here}/case-life.svg")
    build(True).save(f"{here}/case-life-dark.svg")
