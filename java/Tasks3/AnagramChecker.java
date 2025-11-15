import java.util.Scanner;
import java.util.Arrays;

public class AnagramChecker {
    
    public static boolean isAnagram(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();

        if (str1.length() != str2.length()) {
            return false;
        }

        char[] arr1 = str1.toCharArray();
        char[] arr2 = str2.toCharArray();
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        String[] parts = input.split(",");
        String str1 = parts[0].trim();
        String str2 = parts[1].trim();
        
        boolean result = isAnagram(str1, str2);
        System.out.println(result);
        scanner.close();
    }
}