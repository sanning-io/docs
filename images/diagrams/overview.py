"""Writes overview.svg and overview-dark.svg. Run: python3 overview.py"""
import os
from lib import D

ARIA = ("How Sanning works. Your agent captures each step and signs it in your process. Sanning "
        "seals new records every few minutes and puts a stamp on a public record. You give an "
        "evidence pack to a reviewer. The reviewer verifies it offline and checks the stamp on the "
        "public record, without asking Sanning.")


def build(dark=False):
    d = D(760, 250, ARIA, dark)
    d.zone(10, 10, 230, 96, "Your systems")
    d.node(24, 58, "Your agent", ["captures each step, and signs it", "with a key that only you hold"])
    d.zone(280, 10, 200, 96, "Sanning")
    d.node(294, 58, "Anchors", ["seals new records every", "few minutes"])
    d.zone(520, 10, 230, 96, "Public record")
    d.accent_box(534, 36, 202, 52)
    d.text(546, 58, "The stamp", 'acc')
    d.text(546, 70, "shows when the records existed")

    d.arrow([(240, 58), (280, 58)])
    d.text(260, 50, "records", anchor='middle')
    d.arrow([(480, 58), (520, 58)])
    d.text(500, 50, "stamp", anchor='middle')

    d.zone(10, 144, 230, 96, "You")
    d.node(24, 192, "Evidence pack", ["the records, their stamps and", "the content you disclose"])
    d.zone(280, 144, 200, 96, "The reviewer")
    d.node(294, 192, "Verifies offline", ["open-source code, no account"])

    d.arrow([(240, 192), (280, 192)])
    d.text(260, 184, "gives", anchor='middle')
    d.arrow([(480, 192), (635, 192), (635, 106)], dashed=True)
    d.text(560, 184, "checks the stamp", anchor='middle')
    return d


if __name__ == '__main__':
    here = os.path.dirname(os.path.abspath(__file__))
    build().save(f"{here}/overview.svg")
    build(True).save(f"{here}/overview-dark.svg")
