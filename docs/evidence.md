# Evidence for the order

This is a summary of the section "Alphabetical order" in Shosted & Davis,
*The Deseret Alphabet: "A Fixed and Unalterable Sound"* (University of
Illinois Press, 2026), with the archival references needed to check it.
Archival sigla: **CHL** = Church History Library, Salt Lake City; **DAM** =
Deseret Alphabet manuscripts, CHL CR 244 415; **D1B** = *Deseret First Book*
(1868); **BoM69** = the 1869 Deseret Alphabet *Book of Mormon*.

## 1. The Unicode position

The 1996 encoding proposal (Jenkins) states:

> There is no evidence regarding collation of the Deseret. One assumes that
> the letters are intended to collate in the order in which they were
> commonly presented, but there is no proof of that at this time.

The 38 letters were encoded in that presentation order (Unicode 3.1, 2001);
OI and EW were added at the end of the block in Unicode 4.0 (2003).  DUCET and
the CLDR root collation assign primary weights in code-point order, with
lowercase before uppercase at the tertiary level (see `allkeys.txt`,
U+10400–U+1044F).  No CLDR collation tailoring exists for Deseret; the
`en_Dsrt` locale inherits root.

## 2. Presentation order in the specimens

`data/specimen-orders.tsv` lists the order of the letters in ten sources,
side by side.  (The Pitman column gives the *sound* order of his 1846
phonotypic alphabet, rendered with the Deseret letters of equivalent value.)

| Column | Source |
|---|---|
| Pitman-1846 | Isaac Pitman, *Paradise Lost* in phonotypy (London: Phonetic Institution, 1846), p. vi. |
| Palmer-c1854 | The "Palmer specimen," earliest known printed form of the alphabet, ca. 1854. |
| Phelps-1855 | W. W. Phelps's 1855 printed specimen (includes OI and EW). |
| Remy-1860 | Jules Rémy, *Voyage au pays des Mormons* (Paris: Dentu, 1860) (includes OI and EW). |
| DN-1860 | *Deseret News* alphabet table, 1860. |
| Burton-1861 | Richard F. Burton, *The City of the Saints* (London: Longman, 1861). |
| D1B-1868 | *Deseret First Book* (1868). |
| BoM-1869 | Alphabet key in BoM69 (1869). |
| Speller-c1859 | *Deseret Phonetic Speller* manuscript (see §3); order inferred from its section structure. |
| Unicode-1996 | Order of encoding in Jenkins's proposal (= code-point order). |

Observations:

- Across printed specimens the order is stable: six long vowels, six short
  vowels, the diphthongs (PRICE, [CHOICE,] MOUTH, [MULE]), then W, Y, H, then
  the consonants from PEE to ENG.  The only outlier is the *Missouri Daily
  Democrat* (22 August 1857), whose haphazard order suggests printing without
  Mormon supervision.
- The consonants are ordered by place and manner of articulation, following
  Pitman.
- The two specimens that include OI and EW (Phelps, Rémy) place the four
  diphthongs in the Pitman order PRICE, CHOICE, MOUTH, MULE.
- D1B (1868) prints Y before W, the only inversion within a block in any
  printed specimen; Orson Pratt restored W, Y in BoM69.  Jenkins's proposal
  follows D1B glyph shapes but encodes W before Y.

## 3. The Deseret Phonetic Speller (ca. March 1859)

DAM, images 1–114 (CHL CR 244 415).  Undated, unsigned manuscript, possibly
in Orson Pratt's hand; titled 𐑄 𐐼𐐯𐑅𐐨𐑉𐐯𐐻 𐑁𐐬𐑌𐐯𐐻𐐮𐐿 𐑅𐐹𐐯𐑊𐐲𐑉 "The Deseret
Phonetic Speller."  Fifty-seven one-sided pages of monosyllabic words built
up by systematic combination of letters, at most four characters per word,
arranged in three columns.  The date follows from the Board of Regents'
discussion of a speller and dictionary in March–April 1859 (Journal History
of the Church, 21 March and 18 April 1859).  The manuscript was among the
Deseret Alphabet manuscripts located in the Church Historian's Office in
May 1967.  It was never printed.

Reading order: short columns of three to five words, all beginning with the
same letter, are read top to bottom; the columns run left to right and top to
bottom across the page.  Read this way, the initial letters proceed:

1. long vowels 𐐀 𐐁 𐐂 𐐃 𐐄 𐐅;
2. the diphthongs, *immediately after the long vowels and before the short
   vowels*, which no presentation specimen does;
3. short vowels 𐐆 𐐇 𐐈 𐐉 𐐊 𐐋;
4. consonants 𐐑 … 𐐤 in the standard order (𐐥 heads no section, since no
   English syllable begins with /ŋ/; in final position it follows 𐐤.  Note
   that 𐐥 can still be orthographically word-initial in syllabic spellings
   that use letter names, e.g. 𐐥𐑀𐑊𐐰𐑌𐐼 "England"; the sort rule applies to
   these unchanged);
5. 𐐏 𐐎 𐐐, *after* the consonant series rather than before it, and with 𐐏
   before 𐐎 as in D1B.

## 4. The Doctrine and Covenants manuscript index (ca. 1869)

DAM (CHL CR 244 415), partial manuscript (a), pp. 7–47, images 13–95 of 388.
A topical index to the Deseret *Doctrine and Covenants* manuscript (scribe
probably Larinda Ross Pratt), arranged by first letter in the same order as
the Speller.  Second letters are not reliably ordered, apparently because the
entries were keyed from the English index.

## 5. The English–Hopi vocabulary (1860)

Marion J. Shelton's manuscript vocabulary (CHL MS 2977), edited in Beesley &
Elzinga 2015 (see p. 83).  English headwords are grouped by initial letter in
the traditional order, but long and short vowels are grouped together ("image"
directly after "evening"), the order W, Y, H obtains, and there are no groups
headed by diphthongs (the only such words, "our" and "ours," sit in an
unalphabetized list of pronouns).  This is the one source that diverges from
the Speller.  It is a single missionary's field document, whereas the Speller
and the D&C index were produced inside the Deseret Alphabet programme, so the
Speller order is preferred.

## 6. Comparison with Pitman's phonotypic orders

The Deseret letters were modelled on Pitman's English Phonotypic Alphabet
(EPA), and the Deseret presentation order on Pitman's.  Pitman's own order,
however, was not stable.  The Unicode proposal for the EPA observes that "the
different versions of EPA specify differing 'systematical' alphabet orders"
(L2/24-277, §2.5), and its figures reproduce the tables; `data/epa-orders.tsv`
summarizes eight of them, from 1844 to 1888, beside the two Deseret orders.
In brief:

| | 1844 No. 11 | 1844 No. 12 | 1846–48 | 1855 Cincinnati | 1856 | 1868 | 1888 |
|---|---|---|---|---|---|---|---|
| Vowels before consonants | yes | yes | yes | yes | no | no | no |
| Long and short vowels | paired by quality | paired by quality | long block, short block | long block, short block | interleaved, by place | interleaved, by place | interleaved, by place |
| Diphthongs | after Y, W | after short vowels | after short vowels | after short vowels | last (digraphs) | last | last (digraphs) |
| Y, W, H | Y W between vowels and diphthongs; H last of all | W Y H after diphthongs | Y W H after diphthongs | Y W H after diphthongs | dispersed by place (h y guttural, w labial) | W Y H after the consonants | W Y H after the consonants |
| L and R | l r | l r | r l | l r | l r | l r | l r |

Three things follow.

- **The Deseret presentation order is EPA 1846–48**, the version current
  when the regents began work (long block, short block, diphthongs, then the
  coalescents and aspirate, then the consonants by place and manner).  The
  Deseret specimens differ only in printing W before Y, which Pitman himself
  did in 1844 (No. 12) and in his 1852 recapitulation of the 1847 alphabet.
  The relative order of Y and W was unstable in Pitman and is the one point
  of instability in the Deseret specimens (D1B has Y, W).
- **The Speller's placement of the diphthongs**, between the long and short
  vowels, has no precedent in any EPA version.  Pitman always put them after
  the short vowels, or, from 1856, at the very end.
- **The Speller's placement of Y, W, H after the consonants** parallels what
  Pitman did from 1868 ("… m n ng; l r; w y; h"), and his 1844 No. 11 table
  already put the aspirate last of all.  Whether the regents knew the
  post-1856 revisions, or arrived at the arrangement independently, is not
  established; the Speller (ca. 1859) predates the 1868 table.

So Pitman's order is a useful control but not a source for the Speller order:
the Speller shares Pitman's vowel-first structure and his consonant sequence,
and departs from every Pitman version in the position of the diphthongs.

Sources for the tables: *Phonotypic Journal* 3 (1844), pp. 2 and 98 (Nos. 11
and 12); Pitman, *Paradise Lost* (1846), p. vi; *The Gospel according to
Matthew, in Phonotypy and Heterotypy* (1847), p. 4; *Phonetic Journal* 7
(1848), inner cover; *Phonetic Journal* 7 (1852), p. 5; *American Phonetic
Journal* (Cincinnati, 1855), p. 12; *An English Grammar, printed
phonetically* (London, 1856), p. 4; Pitman, *The Trial of William Rodger*
(1868), p. vi; *Phonetic Journal* 47 (1888), p. 1.  All but the first three
are reproduced as figures 1847a, 1848a, 1852a, 1855a, 1856b, 1868a and 1888a
in *Fifth Revised Proposal to encode characters for the English Phonotypic
Alphabet (EPA) in the UCS*, Unicode document L2/24-277 (2024),
<https://www.unicode.org/L2/L2024/24277-epa-proposal-fifth-edition.pdf>.

## 7. Assessment

Two independent institutional documents (the Speller and the D&C index) agree
on an order that differs from the presentation order in exactly two respects:
diphthongs between the long and short vowels, and Y, W, H after the
consonants.  Everything else matches the presentation order, DUCET, and
Pitman's 1846–48 alphabet.  That is the order proposed here.

## 8. Still to do

- Obtain and, if permitted, publish page images or a transcription of the
  Speller's section headings so the order can be checked without a visit to
  CHL.  Confirm in particular whether the Speller has sections for OI and EW.
- Add the D&C index page images or a transcription of its first-letter
  sequence.
