import java.util.Scanner;

public class ReverseWords {
    public static String reverseWords(String str) {
        if (str == null || str.trim().isEmpty()) {
            return str;
        }
        
        String[] words = str.trim().split("\\s+");
        StringBuilder result = new StringBuilder();
        
        for (int i = words.length - 1; i >= 0; i--) {
            result.append(words[i]);
            if (i > 0) {
                result.append(" ");
            }
        }
        return result.toString();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        String result = reverseWords(input);
        System.out.println(result);
        scanner.close();
    }
}