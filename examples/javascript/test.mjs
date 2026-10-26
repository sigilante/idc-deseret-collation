// Checks the JS comparator against the shared test files.
//   node examples/javascript/test.mjs
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";
import { sort } from "./deseretCollation.mjs";

const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
let failures = 0;
for (const name of ["letters.txt", "words.txt"]) {
  const expected = readFileSync(join(root, "tests", name), "utf8")
    .split("\n").filter((l) => l.length && !l.startsWith("#"));
  // Shuffle deterministically, then sort.
  const shuffled = [...expected].sort((a, b) => hash(a) - hash(b));
  const actual = sort(shuffled);
  const ok = actual.every((w, i) => w === expected[i]);
  console.log(`${ok ? "PASS" : "FAIL"} tests/${name} (${expected.length} lines)`);
  if (!ok) {
    failures++;
    for (let i = 0; i < expected.length; i++) {
      if (actual[i] !== expected[i]) { console.log(`  first difference at line ${i + 1}: got ${actual[i]}, expected ${expected[i]}`); break; }
    }
  }
}
function hash(s) { let h = 2166136261; for (const c of s) { h ^= c.codePointAt(0); h = Math.imul(h, 16777619) >>> 0; } return h; }
process.exit(failures ? 1 : 0);
