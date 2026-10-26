#!/usr/bin/env python3
"""Verify the test files against the reference implementation and, when PyICU
is available, against ICU running collation/deseret-speller.rules.

    python3 tests/run_tests.py

Exit status is non-zero on any failure.  ICU checks are skipped (with a
notice) if PyICU is not installed.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "examples" / "python"))
import deseret_collation as dc  # noqa: E402

TEST_FILES = ["letters.txt", "words.txt"]


def read_lines(path: Path) -> list[str]:
    return [l for l in path.read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]


def check(name: str, expected: list[str], sorter) -> bool:
    shuffled = expected[:]
    random.Random(2026).shuffle(shuffled)
    actual = sorter(shuffled)
    if actual == expected:
        print(f"PASS {name} ({len(expected)} lines)")
        return True
    print(f"FAIL {name}")
    for i, (a, e) in enumerate(zip(actual, expected), 1):
        if a != e:
            print(f"  first difference at line {i}: got {a!r}, expected {e!r}")
            break
    return False


def main() -> int:
    ok = True
    try:
        import icu  # type: ignore
        coll = dc.icu_collator()
        icu_sorter = lambda ws: sorted(ws, key=coll.getSortKey)
        print(f"ICU {icu.ICU_VERSION} available; rules parsed OK")
    except ImportError:
        icu_sorter = None
        print("PyICU not installed; skipping ICU checks")

    for name in TEST_FILES:
        expected = read_lines(ROOT / "tests" / name)
        ok &= check(f"reference  tests/{name}", expected, dc.sort)
        if icu_sorter:
            ok &= check(f"ICU rules  tests/{name}", expected, icu_sorter)

    # The ORDER string and data/order.tsv must agree.
    tsv = read_lines(ROOT / "data" / "order.tsv")[1:]
    smalls = "".join(row.split("\t")[3] for row in tsv)
    caps = "".join(row.split("\t")[2] for row in tsv)
    if smalls == dc.ORDER and all(ord(c) - ord(s) == -0x28 for c, s in zip(caps, smalls)):
        print("PASS data/order.tsv matches examples/python ORDER")
    else:
        print("FAIL data/order.tsv does not match examples/python ORDER")
        ok = False

    # Sanity check: the Speller order must actually differ from CLDR root on
    # the word list (otherwise the tailoring is a no-op).
    if icu_sorter:
        words = read_lines(ROOT / "tests" / "words.txt")
        root = icu.Collator.createInstance(icu.Locale.getRoot())
        root_sorted = sorted(words, key=root.getSortKey)
        if root_sorted != words:
            print("PASS CLDR root order differs from Speller order on tests/words.txt")
        else:
            print("FAIL CLDR root order equals Speller order on tests/words.txt")
            ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
