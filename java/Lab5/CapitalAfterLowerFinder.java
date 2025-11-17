import java.util.regex.*;

public class CapitalAfterLowerFinder {
    public static void main(String[] args) {
        String text = "Зачем мНе брИтанский Дырокол если еСть совЕтский КаморниК?";

        Pattern pattern = Pattern.compile("[а-я][А-Я]");
        Matcher matcher = pattern.matcher(text);
        StringBuffer result = new StringBuffer();
        
        while (matcher.find()) {
            String found = matcher.group();
            matcher.appendReplacement(result, "!" + found + "!");
        }
        matcher.appendTail(result);
        System.out.println(result.toString());
    }
}