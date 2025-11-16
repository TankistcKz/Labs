import java.util.regex.*;
import java.util.ArrayList;
import java.util.List;

public class WordsStartingWithLetter {
    public static void main(String[] args) {
        String text = "Мам купи Abrams!" +
                        "У нас есть Abrams! дома" +
                        "Abrams! дома: 🚜 ";
        char letter = 'A';
        List<String> words = findWordsStartingWith(text, letter);

        System.out.println(words);
    }
    
    public static List<String> findWordsStartingWith(String text, char letter) {
        List<String> words = new ArrayList<>();

        String patternStr = "\\b" + Pattern.quote(String.valueOf(letter)) + "\\w*";
        Pattern pattern = Pattern.compile(patternStr, Pattern.CASE_INSENSITIVE);
        Matcher matcher = pattern.matcher(text);
        
        while (matcher.find()) {
            words.add(matcher.group());
        }
        return words;
    }
}