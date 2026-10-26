# CLDR submission

## Current state in CLDR and ICU

- `common/main/en_Dsrt.xml` exists: display names, date/time and number
  formats for English in Deseret.  Nothing in `common/collation/` mentions
  Deseret, so `en_Dsrt` collates with the root order (DUCET, i.e. code-point
  order for the Deseret block).
- ICU builds its collation data from CLDR, so the fix belongs in CLDR, not in
  ICU, Windows, macOS, Android, Java or browsers individually.  Those all
  consume ICU (or ICU4X) data and pick the change up in due course.

## What to submit

The single file `collation/en_Dsrt.xml` from this repository, placed at
`common/collation/en_Dsrt.xml` in the CLDR repository.  It contains only the
two reset-and-tailor lines; see UTS #35 Part 5 (Collation) for the syntax.
No change to `common/main/en_Dsrt.xml` is needed.

If reviewers would like conformance data, `tests/letters.txt` and
`tests/words.txt` can be offered as test cases.

## Process

1. File a ticket in the CLDR Jira: <https://unicode-org.atlassian.net/browse/CLDR>
   (project CLDR, component *collation*).  Use the draft text below.  Link
   this repository and the book.
2. Open a pull request against <https://github.com/unicode-org/cldr> with
   the ticket number in the title (`CLDR-NNNNN Add en_Dsrt collation
   tailoring`).  The CLDR bot will ask for the Unicode contributor license
   agreement if it is not already on file.
3. Reply to review.  Typical questions: evidence for the order (point to
   `docs/evidence.md`), whether the order should apply to Deseret text in
   locales other than `en_Dsrt` (it is the only locale that uses the script),
   and whether `search` collation also needs it (no; `search` tailorings are
   for matching, and the primary order is irrelevant there).
4. CLDR releases roughly twice a year; the following ICU release carries the
   data.

## Draft ticket text

> **Title:** Add collation tailoring for en_Dsrt (Deseret Alphabet)
>
> The locale en_Dsrt currently inherits the root collation, which orders the
> Deseret letters by code point. The code-point order follows the
> presentation order in 19th-century alphabet charts; the 1996 encoding
> proposal noted explicitly that there was then no evidence about intended
> alphabetical order.
>
> Archival evidence now establishes the order used within the Deseret
> Alphabet programme itself: the unpublished *Deseret Phonetic Speller* (ca.
> 1859, Church History Library CR 244 415) and the index to the Deseret
> *Doctrine and Covenants* manuscript (ca. 1869, same collection). Both order
> initial letters as: long vowels; diphthongs (AY, OI, OW, EW); short vowels;
> consonants PEE through ENG; then YEE, WU, H. This differs from root in two
> respects only: (1) the diphthongs move from after the short vowels (and, for
> OI and EW, from the end of the block) to between the long and short vowels;
> (2) YEE, WU, H move from before PEE to after ENG, with YEE before WU.
>
> Proposed tailoring (common/collation/en_Dsrt.xml):
>
>     &𐐭<𐐴<<<𐐌<𐑎<<<𐐦<𐐵<<<𐐍<𐑏<<<𐐧
>     &𐑍<𐐷<<<𐐏<𐐶<<<𐐎<𐐸<<<𐐐
>
> Documentation, the evidence with archival references, sorted test data
> (verified with ICU 73 and 77), and example code are at
> https://github.com/sigilante/idc-deseret-collation. The underlying analysis
> is published in Shosted & Davis, *The Deseret Alphabet: "A Fixed and
> Unalterable Sound"* (University of Illinois Press, 2026).

## Checklist before filing

- [ ] Confirm against the Speller page images that the manuscript has
      sections headed by OI and EW, or document that their position is taken
      from Phelps 1855 / Rémy 1860.
- [ ] Add page images or a transcription of the Speller headings to this
      repository if CHL permits.
- [ ] Both authors agree on the proposed order and the wording of the ticket.
- [ ] Link this repository from the Consortium site.
- [ ] Unicode contributor license agreement on file for whoever opens the PR.
