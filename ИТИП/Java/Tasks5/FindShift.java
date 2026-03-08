import java.util.Scanner;

public class FindShift {
    public static int findShift(String s1, String s2) {
        if (s1.length() != s2.length() || s1.length() == 0) return -1;
        
        int shift = (s2.charAt(0) - s1.charAt(0) + 26) % 26;
        
        for (int i = 0; i < s1.length(); i++) {
            int expectedShift = (s2.charAt(i) - s1.charAt(i) + 26) % 26;
            if (expectedShift != shift) {
                return -1;
            }
        }
        
        return shift;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] parts = input.split(",");
        
        String s1 = parts[0].trim();
        String s2 = parts[1].trim();
        
        System.out.println(findShift(s1, s2));
        scanner.close();
    }
}