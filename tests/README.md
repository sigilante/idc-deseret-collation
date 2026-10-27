# Test data

Each `.txt` file here is a list of strings, one per line, **already in the
correct order**.  A conformant collator must reproduce the file exactly when
given its lines in any other order.  Lines beginning with `#` are comments.

| File | Contents |
|---|---|
| `letters.txt` | The 40 Deseret letters, each small (lowercase) form immediately followed by its capital. Exercises the primary order and the lowercase-first tertiary order. |
| `words.txt` | 259 words. Most are taken from the 1869 Deseret Alphabet *Book of Mormon* (the largest printed Deseret text): the six most frequent words under each initial letter, some capitalized forms, and hand-picked words that differ only in the second letter (e.g. 𐐺𐐨 / 𐐺𐐴 / 𐐺𐐮𐑌 / 𐐺𐐳𐐿). The 1869 text does not use the OI (𐐦 𐑎) and EW (𐐧 𐑏) letters, so fourteen words containing them are constructed: 𐑎𐑊, 𐐦𐑊, 𐐺𐑎, 𐑂𐑎𐑅, 𐐾𐑎, 𐐽𐑎𐑅, 𐑏, 𐐧, 𐑁𐑏, 𐑌𐑏, 𐑋𐑏𐑊, 𐑏𐑆, 𐐧𐑆, 𐐸𐑏. One syllabic spelling with word-initial ENG, 𐐥𐑀𐑊𐐰𐑌𐐼 "England", checks that ENG sorts after EN and before 𐐏 𐐎 𐐐 even in initial position. |
| `words.root-order.txt` | The same words sorted by the **untailored** CLDR root collation (code-point order of the Deseret block). Not a conformance target; it is here so the effect of the tailoring can be seen with `diff`. |

The expected orders were produced by the reference implementation in
`examples/python/deseret_collation.py` and independently confirmed by ICU
(ICU4C 73.1 via PyICU, and the ICU4C example program compiled against ICU 77)
running `collation/deseret-speller.rules`.

Run the checks:

```sh
python3 tests/run_tests.py          # reference implementation; ICU too if PyICU is installed
node examples/javascript/test.mjs   # JavaScript comparator
```
