#!/usr/bin/env python3
"""Deseret Alphabet collation in the "Speller" order.

Two implementations are provided:

* ``sort_key`` / ``sort`` -- a dependency-free reference implementation that
  handles Deseret letters (U+10400..U+1044F).  Non-Deseret characters are
  ordered by code point ahead of all Deseret letters, which is good enough
  for word lists but is *not* a substitute for a full UCA implementation on
  mixed-script text.
* ``icu_collator`` -- builds an ICU ``RuleBasedCollator`` from the rules in
  ``collation/deseret-speller.rules`` (requires PyICU).  This is the
  authoritative behaviour: it is exactly what CLDR/ICU will do once the
  tailoring is adopted.

Usage::

    python3 deseret_collation.py < words.txt          # reference sort
    python3 deseret_collation.py --icu < words.txt    # ICU sort
"""
from __future__ import annotations

import sys
from pathlib import Path

# Small (lowercase) letters in canonical order.  Capitals are at small - 0x28.
ORDER = (
    "𐐨𐐩𐐪𐐫𐐬𐐭"      # long vowels   LONG I, LONG E, LONG A, LONG AH, LONG O, LONG OO
    "𐐴𐑎𐐵𐑏"        # diphthongs    AY, OI, OW, EW
    "𐐮𐐯𐐰𐐱𐐲𐐳"      # short vowels  SHORT I, SHORT E, SHORT A, SHORT AH, SHORT O, SHORT OO
    "𐐹𐐺𐐻𐐼𐐽𐐾𐐿𐑀"    # PEE BEE TEE DEE CHEE JEE KAY GAY
    "𐑁𐑂𐑃𐑄𐑅𐑆𐑇𐑈"    # EF VEE ETH THEE ES ZEE ESH ZHEE
    "𐑉𐑊𐑋𐑌𐑍"       # ER EL EM EN ENG
    "𐐷𐐶𐐸"         # coalescents + aspirate  YEE, WU, H
)
assert len(ORDER) == 40

_SMALL_FIRST, _SMALL_LAST = 0x10428, 0x1044F
_CAP_FIRST, _CAP_LAST = 0x10400, 0x10427
_CASE_DELTA = _SMALL_FIRST - _CAP_FIRST  # 0x28

_PRIMARY = {c: i for i, c in enumerate(ORDER)}
_PRIMARY.update({chr(ord(c) - _CASE_DELTA): i for i, c in enumerate(ORDER)})

RULES_PATH = Path(__file__).resolve().parents[2] / "collation" / "deseret-speller.rules"


def sort_key(text: str) -> tuple:
    """Return a key such that ``sorted(words, key=sort_key)`` gives Speller order.

    Primary level: Deseret letters by canonical position (all other characters
    sort before any Deseret letter, by code point).  Tertiary level: lowercase
    before uppercase, decided only after the whole string ties at primary
    level, as in UCA.
    """
    primary = []
    tertiary = []
    for ch in text:
        p = _PRIMARY.get(ch)
        if p is None:
            primary.append((0, ord(ch)))
            tertiary.append(0)
        else:
            primary.append((1, p))
            tertiary.append(1 if _CAP_FIRST <= ord(ch) <= _CAP_LAST else 0)
    return (tuple(primary), tuple(tertiary))


def sort(words):
    """Sort an iterable of strings into Speller order."""
    return sorted(words, key=sort_key)


def load_rules(path: Path = RULES_PATH) -> str:
    """Read the ICU rule file, dropping comment lines."""
    lines = path.read_text(encoding="utf-8").splitlines()
    return "\n".join(l for l in lines if l.strip() and not l.lstrip().startswith("#"))


def icu_collator(path: Path = RULES_PATH):
    """Build an ICU RuleBasedCollator for the Speller order (needs PyICU)."""
    import icu  # type: ignore

    return icu.RuleBasedCollator(load_rules(path))


def main(argv: list[str]) -> int:
    use_icu = "--icu" in argv
    words = [line.rstrip("\n") for line in sys.stdin if line.strip()]
    if use_icu:
        coll = icu_collator()
        words.sort(key=coll.getSortKey)
    else:
        words = sort(words)
    sys.stdout.write("\n".join(words) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
