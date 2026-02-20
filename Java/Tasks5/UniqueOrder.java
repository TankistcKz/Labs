import java.util.Scanner;
import java.util.HashSet;

public class UniqueOrder {
    public static String uniqueOrder(String str) {
        HashSet<Character> seen = new HashSet<>();
        StringBuilder result = new StringBuilder();
        
        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if (!seen.contains(c)) {
                seen.add(c);
                result.append(c);
            }
        }
        
        return result.toString();
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println(uniqueOrder(input));
        scanner.close();
    }
}