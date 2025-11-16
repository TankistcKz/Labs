import java.util.regex.*;

public class NumberFinder {
    public static void main(String[] args) {
        String text = "БПС Challenger имел пробитие 230 мм" +
                      "Swererpanzer spahwagen 7.5 cm sondercraftfarzeug 234/4" +
                      "shdfklhsklfh s;ljdfpojsof sdjfoji;sdifj";
        
        Pattern pattern = Pattern.compile("\\d+\\.?\\d*");
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            System.out.println(matcher.group());
        }
    }
}