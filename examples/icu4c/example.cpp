// Sort Deseret words with ICU4C using the Speller-order tailoring.
//
// Build (macOS/Homebrew, adjust for your platform):
//   c++ -std=c++17 example.cpp $(pkg-config --cflags --libs icu-i18n icu-uc icu-io) -o example
// Run:
//   ./example ../../collation/deseret-speller.rules < ../../tests/words.txt
#include <unicode/coll.h>
#include <unicode/tblcoll.h>
#include <unicode/unistr.h>
#include <unicode/ustream.h>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

static icu::UnicodeString loadRules(const char* path) {
    std::ifstream in(path);
    std::string line, rules;
    while (std::getline(in, line)) {
        if (line.empty() || line[0] == '#') continue;   // drop comments
        rules += line + "\n";
    }
    return icu::UnicodeString::fromUTF8(rules);
}

int main(int argc, char** argv) {
    if (argc < 2) { std::cerr << "usage: example RULES_FILE < words\n"; return 2; }
    UErrorCode status = U_ZERO_ERROR;
    std::unique_ptr<icu::RuleBasedCollator> coll(
        new icu::RuleBasedCollator(loadRules(argv[1]), status));
    if (U_FAILURE(status)) {
        std::cerr << "collator error: " << u_errorName(status) << "\n";
        return 1;
    }
    std::vector<icu::UnicodeString> words;
    std::string line;
    while (std::getline(std::cin, line))
        if (!line.empty() && line[0] != '#') words.push_back(icu::UnicodeString::fromUTF8(line));
    std::sort(words.begin(), words.end(),
              [&](const icu::UnicodeString& a, const icu::UnicodeString& b) {
                  return coll->compare(a, b) < 0;
              });
    for (const auto& w : words) std::cout << w << "\n";
    return 0;
}
