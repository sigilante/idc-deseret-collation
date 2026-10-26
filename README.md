# Deseret Alphabet collation (Speller order)

A citable, machine-readable statement of the alphabetical order of the
Deseret Alphabet, with a minimal CLDR tailoring, sorted test data, and
reference implementations.  Published by the Illinois Deseret Consortium.

**Status:** draft 0.1 (2026-10-27).  Not yet submitted to CLDR; see
[`docs/cldr.md`](docs/cldr.md).

## The problem

When the Deseret Alphabet was encoded in Unicode (1996–2001), the proposal
stated that there was *no evidence* about how the letters were meant to be
alphabetized, and assumed the order in which the letters were commonly
presented in nineteenth-century alphabet tables.  That presentation order
became the Unicode code-point order, hence the order in the Unicode Collation
Algorithm's default table (DUCET) and the CLDR root collation, and therefore
the order used by ICU and everything built on it.  The CLDR locale `en_Dsrt`
exists (display names, dates, numbers) but has no collation tailoring.

Evidence has since emerged.  The *Deseret Phonetic Speller*, an unpublished
manuscript prepared for the Deseret Alphabet programme around March 1859 and
rediscovered in 1967, is organized by initial letter in a deliberate order,
and the index to the Deseret *Doctrine and Covenants* manuscript (ca. 1869)
follows the same first-letter order.  That order differs from the presentation
order in two places.  This repository documents the order, states the
difference as a CLDR tailoring, and provides tests and example code.  The
full argument is in Shosted & Davis, *The Deseret Alphabet: "A Fixed and
Unalterable Sound"* (University of Illinois Press, 2026), "Alphabetical
order"; a summary with archival references is in
[`docs/evidence.md`](docs/evidence.md).

## The order

Forty letters in five groups.  Lowercase sorts before uppercase at the
tertiary level, as in CLDR root.

| Group | Letters (capital / small) |
|---|---|
| Long vowels | 𐐀𐐨 𐐁𐐩 𐐂𐐪 𐐃𐐫 𐐄𐐬 𐐅𐐭 |
| Diphthongs | 𐐌𐐴 𐐦𐑎 𐐍𐐵 𐐧𐑏 |
| Short vowels | 𐐆𐐮 𐐇𐐯 𐐈𐐰 𐐉𐐱 𐐊𐐲 𐐋𐐳 |
| Consonants | 𐐑𐐹 𐐒𐐺 𐐓𐐻 𐐔𐐼 𐐕𐐽 𐐖𐐾 𐐗𐐿 𐐘𐑀 𐐙𐑁 𐐚𐑂 𐐛𐑃 𐐜𐑄 𐐝𐑅 𐐞𐑆 𐐟𐑇 𐐠𐑈 𐐡𐑉 𐐢𐑊 𐐣𐑋 𐐤𐑌 𐐥𐑍 |
| Glides | 𐐏𐐷 𐐎𐐶 𐐐𐐸 |

In Unicode letter names:

> LONG I, LONG E, LONG A, LONG AH, LONG O, LONG OO; AY, OI, OW, EW;
> SHORT I, SHORT E, SHORT A, SHORT AH, SHORT O, SHORT OO;
> PEE, BEE, TEE, DEE, CHEE, JEE, KAY, GAY, EF, VEE, ETH, THEE, ES, ZEE, ESH,
> ZHEE, ER, EL, EM, EN, ENG; YEE, WU, H.

The full table with code points, ALA-LC romanization, and lexical sets is in
[`data/order.tsv`](data/order.tsv).

### What changes relative to the Unicode / DUCET order

| | Root (DUCET) | Speller order |
|---|---|---|
| Diphthongs AY, OW | after the short vowels | after the long vowels, before the short vowels |
| Diphthongs OI, EW | last of all (encoded later, in Unicode 4.0) | with AY and OW: AY, OI, OW, EW |
| YEE, WU, H | before PEE, in the order WU, YEE, H | after ENG at the very end, in the order YEE, WU, H |

Everything else is identical: the long vowels, the short vowels, and the
consonant series PEE through ENG keep their root order, and so does the
position of Deseret relative to other scripts.  The tailoring is therefore
two lines:

```
&𐐭<𐐴<<<𐐌<𐑎<<<𐐦<𐐵<<<𐐍<𐑏<<<𐐧
&𐑍<𐐷<<<𐐏<𐐶<<<𐐎<𐐸<<<𐐐
```

Side by side, small letters only:

```
root:     𐐨𐐩𐐪𐐫𐐬𐐭 𐐮𐐯𐐰𐐱𐐲𐐳 𐐴𐐵 𐐶𐐷𐐸 𐐹𐐺𐐻𐐼𐐽𐐾𐐿𐑀𐑁𐑂𐑃𐑄𐑅𐑆𐑇𐑈𐑉𐑊𐑋𐑌𐑍 𐑎𐑏
speller:  𐐨𐐩𐐪𐐫𐐬𐐭 𐐴𐑎𐐵𐑏 𐐮𐐯𐐰𐐱𐐲𐐳 𐐹𐐺𐐻𐐼𐐽𐐾𐐿𐑀𐑁𐑂𐑃𐑄𐑅𐑆𐑇𐑈𐑉𐑊𐑋𐑌𐑍 𐐷𐐶𐐸
```

### Scope and caveats

- This is a **sorting** order.  It does not propose changing the order in
  which the letters are presented in charts, keyboards, or fonts, and it does
  not affect code points.
- The placement of OI and EW relies on the specimens that include them
  (Phelps 1855, Rémy 1860, following Pitman 1846), which put the four
  diphthongs in the order PRICE, CHOICE, MOUTH, MULE; the Speller is
  consistent with this.  Whether the Speller manuscript itself contains
  sections for OI and EW should be confirmed against the page images before
  CLDR submission (see the checklist in `docs/cldr.md`).
- ENG (𐐥) does not begin a word phonologically, so the Speller has no
  section for it; its position after EN is inferred from word-final position
  and from every presentation order.  Orthographically it can be
  word-initial, because some writers spell syllabically with letter names
  (𐐥𐑀𐑊𐐰𐑌𐐼 "England", 𐐜 "the", 𐐒 "be"); such words sort by the same rule, so
  𐐥𐑀𐑊𐐰𐑌𐐼 follows every EN-initial word and precedes the glides.
- The 1860 English–Hopi vocabulary alphabetizes differently (long and short
  vowels interleaved, W before Y).  It is a field document by a single
  missionary; the Speller and the D&C index are institutional products of the
  Deseret Alphabet programme and are taken as authoritative.

## Repository layout

```
collation/en_Dsrt.xml            LDML collation tailoring, ready for CLDR common/collation/
collation/deseret-speller.rules  The same rules as an ICU rule string (comments allowed)
data/order.tsv                   The 40 letters in order: code points, names, romanization
data/specimen-orders.tsv         Letter order in ten historical specimens, side by side
docs/evidence.md                 Sources and archival references
docs/cldr.md                     Submission plan, draft ticket text, checklist
tests/letters.txt                Sorted letters (conformance target)
tests/words.txt                  Sorted words (conformance target)
tests/words.root-order.txt       Same words in root order, for comparison only
tests/run_tests.py               Checks the files with the reference implementation and with ICU
examples/python/                 Pure-Python reference implementation + PyICU helper
examples/javascript/             Pure-JS comparator (Intl.Collator cannot take custom rules)
examples/icu4c/                  C++ program using icu::RuleBasedCollator
examples/icu4j/                  Java program using com.ibm.icu.text.RuleBasedCollator
```

## Using it

**ICU (any binding).**  Build a `RuleBasedCollator` from
`collation/deseret-speller.rules` with comment lines removed.  With PyICU:

```python
import icu
rules = "\n".join(l for l in open("collation/deseret-speller.rules", encoding="utf-8")
                  if l.strip() and not l.startswith("#"))
coll = icu.RuleBasedCollator(rules)
words.sort(key=coll.getSortKey)
```

**Python, no dependencies.**

```python
from deseret_collation import sort, sort_key   # examples/python/
sort(["𐐺𐐳𐐿", "𐐺𐐮𐑌", "𐐺𐐴", "𐐺𐐨"])  # -> ["𐐺𐐨", "𐐺𐐴", "𐐺𐐮𐑌", "𐐺𐐳𐐿"]  (root order would give 𐐺𐐨 𐐺𐐮𐑌 𐐺𐐳𐐿 𐐺𐐴)
```

**JavaScript.**

```js
import { compare } from "./examples/javascript/deseretCollation.mjs";
words.sort(compare);
```

**C++ / Java.**  See `examples/icu4c/example.cpp` and
`examples/icu4j/Example.java`; both read the rules file and sort stdin.

Once the tailoring is in CLDR and ICU, none of this is needed: requesting a
collator for the locale `en-Dsrt` will give this order.

## Tests

```sh
python3 tests/run_tests.py          # reference implementation, plus ICU if PyICU is installed
node examples/javascript/test.mjs
```

The expected orders in `tests/` were generated by the reference
implementation and confirmed by ICU 73 (PyICU) and ICU 77 (ICU4C) running the
rules file.  See [`tests/README.md`](tests/README.md).

## Related resources

- Shosted, Ryan K. and N. E. Davis. *The Deseret Alphabet: "A Fixed and
  Unalterable Sound."* University of Illinois Press, 2026.
- Illinois Deseret Consortium: <https://go.illinois.edu/deseret>
- CLDR `en_Dsrt` locale data: <https://github.com/unicode-org/cldr/blob/main/common/main/en_Dsrt.xml>
- Unicode Deseret block chart: <https://www.unicode.org/charts/PDF/U10400.pdf>
- Jenkins, John H. *Proposal for encoding the Deseret Alphabet in ISO/IEC 10646* (1996):
  <http://web.archive.org/web/19980126170101/http://www.unicode.org/pending/deseret/Proposal.html>
- ALA-LC romanization table for Deseret (2016): <https://www.loc.gov/catdir/cpso/romanization/deseret.pdf>
- Noto Sans Deseret: <https://fonts.google.com/noto/specimen/Noto+Sans+Deseret>
- Beesley, Kenneth R. and Dirk Elzinga. *An 1860 English–Hopi Vocabulary
  Written in the Deseret Alphabet.* University of Utah Press, 2015.

## Citing

See [`CITATION.cff`](CITATION.cff).  Data and documentation are CC BY 4.0;
code is MIT.  See [`LICENSE.md`](LICENSE.md).
