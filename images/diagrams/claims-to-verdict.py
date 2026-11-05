"""Writes six-claims.svg, claims-to-verdict.svg, claims-to-verdict-wide.svg and their -dark twins.
Run: python3 claims-to-verdict.py, then python3 render.py <names> for the PNGs the pages show.

The phone version is drawn 340 wide, the width of a docs column on a phone, with 11px
labels at the least, and split in two, one under the other: the six claims, then the rule
that turns them into one of three verdicts. The wide version is one image, drawn 536 wide,
the width of the Maple column on a desktop, so it shows at a scale of 1.
"""
import os
from lib import D

ARIA_CLAIMS = ("The six claims the kernel checks: signed, unchanged, witnessed, complete, agreed and "
               "follows the rules. Each claim is proven, disproven or not proven.")

ARIA = ("How the claims become one verdict. The rule is read in order. If any claim is disproven, the "
        "verdict is Failed, exit 1. If not, and any claim is not proven, the verdict is Incomplete, exit 2. "
        "Otherwise the verdict is Verified, exit 0. Below, a note: a pack built in the Sandbox that verifies "
        "exits 3. Sandbox is a label on the result, not a verdict.")

ARIA_WIDE = ARIA_CLAIMS + " " + ARIA


def claims(dark=False):
    d = D(340, 314, ARIA_CLAIMS, dark, big=True)
    d.zone(10, 10, 320, 294, "Six claims")
    rows = [("Signed", "the named key signed it"),
            ("Unchanged", "bytes match what was signed"),
            ("Witnessed", "a stamp covers it"),
            ("Complete", "the pack holds all it declares"),
            ("Agreed", "both sides of a hand-off agree"),
            ("Follows the rules", "follows the record format")]
    for i, (a, b) in enumerate(rows):
        d.node(24, 52 + i * 40, a, [b])
    d.text(24, 292, "each: proven, disproven, not proven")
    return d


def verdict(dark=False):
    d = D(340, 422, ARIA, dark, big=True)

    d.zone(10, 10, 150, 294, "The rule")
    d.text(22, 62, "1", 'step')
    d.text(38, 62, "Any claim", 'lbl')
    d.text(38, 77, "disproven?", 'lbl')
    d.text(22, 152, "2", 'step')
    d.text(38, 152, "Any claim", 'lbl')
    d.text(38, 167, "not proven?", 'lbl')
    d.text(22, 242, "3", 'step')
    d.text(38, 242, "Otherwise", 'lbl')
    d.arrow([(60, 88), (60, 136)], dashed=True)
    d.text(68, 114, "no")
    d.arrow([(60, 178), (60, 224)], dashed=True)
    d.text(68, 205, "no")

    d.zone(190, 10, 140, 294, "Three verdicts")
    d.node(202, 62, "Failed", ["exit 1", "a claim is", "disproven"])
    d.node(202, 152, "Incomplete", ["exit 2", "none disproven,", "some not proven"])
    d.accent_box(198, 216, 124, 76)
    d.text(208, 238, "Verified", 'acc')
    d.text(208, 253, "exit 0")
    d.text(208, 267, "every claim in")
    d.text(208, 281, "scope proven")

    for y in (66, 156):
        d.arrow([(160, y), (190, y)])
        d.text(175, y - 8, "yes", anchor='middle')
    d.arrow([(160, 254), (190, 254)])

    d.zone(10, 326, 320, 86, "Sandbox")
    d.text(24, 372, "Sandbox evidence that verifies exits 3.")
    d.text(24, 386, "Sandbox is a label on the result,")
    d.text(24, 400, "never a verdict or a claim.")
    return d


def wide(dark=False):
    """One image, 536 wide: the width of the Maple column on a desktop, so it shows at a scale of 1.
    The claims sit on top in two columns; the rule and the three verdicts sit side by side below."""
    d = D(536, 540, ARIA_WIDE, dark, big=True)

    d.zone(10, 10, 516, 176, "Six claims")
    rows = [("Signed", "the named key signed it"),
            ("Unchanged", "bytes match what was signed"),
            ("Witnessed", "a stamp covers it"),
            ("Complete", "the pack holds all it declares"),
            ("Agreed", "both sides of a hand-off agree"),
            ("Follows the rules", "follows the record format")]
    for i, (a, b) in enumerate(rows):
        d.node(24 + (i % 2) * 256, 52 + (i // 2) * 40, a, [b])
    d.text(24, 172, "each: proven, disproven, not proven")
    d.arrow([(115, 186), (115, 222)])

    d.zone(10, 222, 210, 224, "The rule")
    d.text(22, 264, "1", 'step')
    d.text(38, 264, "Any claim disproven?", 'lbl')
    d.text(22, 327, "2", 'step')
    d.text(38, 327, "Any claim not proven?", 'lbl')
    d.text(22, 390, "3", 'step')
    d.text(38, 390, "Otherwise", 'lbl')
    d.arrow([(60, 274), (60, 313)], dashed=True)
    d.text(68, 298, "no")
    d.arrow([(60, 337), (60, 376)], dashed=True)
    d.text(68, 361, "no")

    d.zone(262, 222, 264, 224, "Three verdicts")
    d.node(276, 264, "Failed", ["exit 1", "a claim is disproven"])
    d.node(276, 327, "Incomplete", ["exit 2", "none disproven, some not proven"])
    d.accent_box(270, 372, 248, 60)
    d.text(282, 394, "Verified", 'acc')
    d.text(282, 409, "exit 0")
    d.text(282, 423, "every claim in scope proven")

    for y in (260, 323):
        d.arrow([(220, y), (262, y)])
        d.text(241, y - 8, "yes", anchor='middle')
    d.arrow([(220, 386), (262, 386)])

    d.zone(10, 458, 516, 72, "Sandbox")
    d.text(24, 504, "Sandbox evidence that verifies exits 3.")
    d.text(24, 518, "Sandbox is a label on the result, never a verdict or a claim.")
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    for name, fn in (("six-claims", claims), ("claims-to-verdict", verdict), ("claims-to-verdict-wide", wide)):
        fn().save(f"{here}/{name}.svg")
        fn(True).save(f"{here}/{name}-dark.svg")
