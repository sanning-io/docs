"""Writes claims-to-verdict.svg and claims-to-verdict-dark.svg. Run: python3 claims-to-verdict.py"""
import os
from lib import D

ARIA = ("How six claims become one verdict. On the left are the six claims the kernel checks: signed, "
        "unchanged, witnessed, complete, agreed and follows the rules. Each claim is proven, disproven "
        "or not proven. In the middle is the rule, read in order. If any claim is disproven, the verdict "
        "is Failed. If not, and any claim is not proven, the verdict is Incomplete. Otherwise the verdict "
        "is Verified. On the right are the three verdicts and their exit codes: Failed exits 1, Incomplete "
        "exits 2 and Verified exits 0. Below, a note: a pack built in the Sandbox that verifies exits 3. "
        "Sandbox is a label on the result, not a verdict.")

def build(dark=False):
    d = D(760, 404, ARIA, dark)
    d.zone(10, 10, 230, 318, "Six claims")
    claims = [("Signed", "the named key signed it"),
              ("Unchanged", "bytes match what was signed"),
              ("Witnessed", "a stamp covers it and verifies"),
              ("Complete", "the pack holds all it declares"),
              ("Agreed", "both sides of a hand-off agree"),
              ("Follows the rules", "follows the vocabulary it names")]
    for i, (a, b) in enumerate(claims):
        d.node(24, 54 + i*42, a, [b])
    d.text(24, 312, "each: proven, disproven, not proven")

    d.zone(284, 10, 200, 318, "The rule")
    d.node(298, 90, "Any claim disproven?", num=1)
    d.node(298, 180, "Any claim not proven?", num=2)
    d.node(298, 270, "Otherwise", num=3)
    d.arrow([(466, 104), (466, 164)], dashed=True)
    d.text(474, 138, "no")
    d.arrow([(466, 194), (466, 254)], dashed=True)
    d.text(474, 228, "no")

    d.zone(528, 10, 222, 318, "Three verdicts")
    d.node(542, 90, "Failed", ["exit 1", "a claim is disproven"])
    d.node(542, 180, "Incomplete", ["exit 2", "none disproven, some not proven"])
    d.accent_box(536, 242, 206, 56)
    d.text(542, 270, "Verified", 'acc')
    d.text(542, 282, "exit 0")
    d.text(542, 293, "every claim in scope proven")

    d.arrow([(240, 169), (284, 169)])
    for y in (86, 176):
        d.arrow([(484, y), (528, y)])
        d.text(506, y - 6, "yes", anchor='middle')
    d.arrow([(484, 266), (528, 266)])

    d.zone(10, 340, 740, 54, "Sandbox")
    d.text(24, 372, "Sandbox evidence that verifies exits 3. Sandbox is a label on the result, never a verdict or a claim.")
    return d

if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    build().save(f"{here}/claims-to-verdict.svg")
    build(True).save(f"{here}/claims-to-verdict-dark.svg")
