import java.util.Scanner;

public class StringProcessor {
    
    public static String nonRepeat(String str) {
        int[] freq = new int[256];
        countFrequency(str.toLowerCase(), 0, freq);
        return buildResult(str, 0, freq);
    }
    
    private static void countFrequency(String str, int index, int[] freq) {
        if (index >= str.length()) {
            return;
        }
        freq[str.charAt(index)]++;
        countFrequency(str, index + 1, freq);
    }
    
    private static String buildResult(String str, int index, int[] freq) {
        if (index >= str.length()) {
            return "";
        }
        
        char currentChar = str.charAt(index);
        char lowerChar = Character.toLowerCase(currentChar);
        String rest = buildResult(str, index + 1, freq);
        
        if (freq[lowerChar] > 3) {
            return rest;
        } else {
            return currentChar + rest;
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println(nonRepeat(input));
        scanner.close();
    }
}