import java.util.Scanner;

public class DivisorCounter {
    public static int countDivisors(int n) {
        int count = 0;
        
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                count++;

                if (i != n / i) {
                    count++;
                }
            }
        }
        
        return count;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int n = scanner.nextInt();
        int result = countDivisors(n);
        System.out.println(result);
        scanner.close();
        }
}
