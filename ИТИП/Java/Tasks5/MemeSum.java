import java.util.Scanner;

public class MemeSum {
    public static int memeSum(int a, int b) {
        StringBuilder result = new StringBuilder();
        
        String s1 = String.valueOf(a);
        String s2 = String.valueOf(b);
        
        int i = s1.length() - 1;
        int j = s2.length() - 1;
        
        while (i >= 0 || j >= 0) {
            int d1 = i >= 0 ? s1.charAt(i) - '0' : 0;
            int d2 = j >= 0 ? s2.charAt(j) - '0' : 0;
            
            result.insert(0, d1 + d2);
            i--;
            j--;
        }
        
        return Integer.parseInt(result.toString());
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] parts = input.split(",");
        
        int a = Integer.parseInt(parts[0].trim());
        int b = Integer.parseInt(parts[1].trim());
        
        System.out.println(memeSum(a, b));
        scanner.close();
    }
}