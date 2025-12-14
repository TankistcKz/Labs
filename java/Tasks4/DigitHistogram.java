import java.util.Scanner;

public class DigitHistogram {
    
    public static int[] digitHistogram(long num) {
        int[] histogram = new int[10];
        
        String numStr = String.valueOf(num);
        for (int i = 0; i < numStr.length(); i++) {
            int digit = numStr.charAt(i) - '0';
            histogram[digit]++;
        }
        
        return histogram;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long num = scanner.nextLong();
        
        int[] result = digitHistogram(num);
        
        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) {
                System.out.print(",");
            }
        }
        System.out.println("]");
        
        scanner.close();
    }
}