import java.util.Scanner;

public class CountWords {
    
    public static int countWords(String str) {
        str = str.trim();

        if (str.isEmpty()) {
            return 0;
        }

        String[] words = str.split("\\s+");
        return words.length;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        int result = countWords(input);
        System.out.println(result);
        scanner.close();
    }
}