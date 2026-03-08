import java.util.Scanner;
import java.util.Arrays;

public class EvenOddDigitCounter {
    public static int[] countEvenOddDigits(int n) {
        n = Math.abs(n);
        
        int evenCount = 0;
        int oddCount = 0;
        
        if (n == 0) {
            return new int[]{1, 0};
        }
        
        while (n > 0) {
            int digit = n % 10;
            
            if (digit % 2 == 0) {
                evenCount++;
            } else {
                oddCount++;
            }
            
            n /= 10;
        }
        
        return new int[]{evenCount, oddCount};
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        
        int[] result = countEvenOddDigits(n);
        System.out.println(result[0] + ", " + result[1]);
        scanner.close();
    }
}