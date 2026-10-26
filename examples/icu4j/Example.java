// Sort Deseret words with ICU4J using the Speller-order tailoring.
//
// Build and run (ICU4J jar on the classpath, e.g. com.ibm.icu:icu4j from Maven Central):
//   javac -cp icu4j.jar Example.java
//   java  -cp icu4j.jar:. Example ../../collation/deseret-speller.rules < ../../tests/words.txt
import com.ibm.icu.text.Collator;
import com.ibm.icu.text.RuleBasedCollator;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Example {
    public static void main(String[] args) throws Exception {
        if (args.length < 1) { System.err.println("usage: Example RULES_FILE < words"); System.exit(2); }
        String rules = Files.readAllLines(Paths.get(args[0]), StandardCharsets.UTF_8).stream()
                .filter(l -> !l.isBlank() && !l.startsWith("#"))
                .collect(Collectors.joining("\n"));
        Collator coll = new RuleBasedCollator(rules);

        List<String> words = new ArrayList<>();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in, StandardCharsets.UTF_8));
        for (String line; (line = in.readLine()) != null; )
            if (!line.isEmpty() && !line.startsWith("#")) words.add(line);
        words.sort(coll);
        words.forEach(System.out::println);
    }
}
