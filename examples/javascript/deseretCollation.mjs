// Deseret Alphabet collation in the "Speller" order.
//
// Intl.Collator cannot be given custom rules, so this module provides a
// comparator directly.  It handles Deseret letters (U+10400..U+1044F); any
// other character sorts before all Deseret letters by code point.  For
// mixed-script text use ICU (ICU4C/ICU4J/ICU4X) with
// collation/deseret-speller.rules instead.
//
//   import { compare, sort, ORDER } from "./deseretCollation.mjs";
//   words.sort(compare);

// Small (lowercase) letters in canonical order.  Capitals are at small - 0x28.
export const ORDER = [
  ..."𐐨𐐩𐐪𐐫𐐬𐐭",     // long vowels   LONG I, LONG E, LONG A, LONG AH, LONG O, LONG OO
  ..."𐐴𐑎𐐵𐑏",       // diphthongs    AY, OI, OW, EW
  ..."𐐮𐐯𐐰𐐱𐐲𐐳",     // short vowels  SHORT I, SHORT E, SHORT A, SHORT AH, SHORT O, SHORT OO
  ..."𐐹𐐺𐐻𐐼𐐽𐐾𐐿𐑀",   // PEE BEE TEE DEE CHEE JEE KAY GAY
  ..."𐑁𐑂𐑃𐑄𐑅𐑆𐑇𐑈",   // EF VEE ETH THEE ES ZEE ESH ZHEE
  ..."𐑉𐑊𐑋𐑌𐑍",      // ER EL EM EN ENG
  ..."𐐷𐐶𐐸",        // coalescents + aspirate  YEE, WU, H
];
if (ORDER.length !== 40) throw new Error("ORDER must contain 40 letters");

const CAP_FIRST = 0x10400, CAP_LAST = 0x10427, CASE_DELTA = 0x28;
const PRIMARY = new Map();
ORDER.forEach((ch, i) => {
  const cp = ch.codePointAt(0);
  PRIMARY.set(cp, i);                // small letter
  PRIMARY.set(cp - CASE_DELTA, i);   // capital letter
});

/** Primary weight (>= 1) for a code point; 0 means "not Deseret". */
function primary(cp) {
  const p = PRIMARY.get(cp);
  return p === undefined ? 0 : p + 1;
}

/** Returns a comparable key: [primaryWeights[], tertiaryWeights[]]. */
export function sortKey(text) {
  const prim = [], tert = [];
  for (const ch of text) {
    const cp = ch.codePointAt(0);
    const p = primary(cp);
    if (p === 0) {
      prim.push([0, cp]);
      tert.push(0);
    } else {
      prim.push([1, p]);
      tert.push(cp >= CAP_FIRST && cp <= CAP_LAST ? 1 : 0);
    }
  }
  return [prim, tert];
}

function cmpArrays(a, b, cmp) {
  const n = Math.min(a.length, b.length);
  for (let i = 0; i < n; i++) {
    const c = cmp(a[i], b[i]);
    if (c !== 0) return c;
  }
  return a.length - b.length;
}

const cmpPair = ([a0, a1], [b0, b1]) => (a0 - b0) || (a1 - b1);
const cmpNum = (a, b) => a - b;

/** Comparator for Array.prototype.sort: whole-string primary, then tertiary. */
export function compare(a, b) {
  const [pa, ta] = sortKey(a);
  const [pb, tb] = sortKey(b);
  return cmpArrays(pa, pb, cmpPair) || cmpArrays(ta, tb, cmpNum);
}

/** Return a new array sorted into Speller order. */
export function sort(words) {
  return [...words].sort(compare);
}
