import java.util.Scanner;

public class VowelCounter {
    public static int countVowels(String str) {
        if (str == null) {
            return 0;
        }
        
        String lowerStr = str.toLowerCase();
        int count = 0;

        for (int i = 0; i < lowerStr.length(); i++) {
            char ch = lowerStr.charAt(i);

            if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') {
                count++;
            }
        }
        return count;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        int result = countVowels(input);
        System.out.println(result);
        scanner.close();
    }
}