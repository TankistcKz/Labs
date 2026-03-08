import java.util.Scanner;

public class SkipSevenSum {
    public static boolean containsSeven(int num) {
        if (num == 0) return false;
        while (num > 0) {
            if (num % 10 == 7) {
                return true;
            }
            num /= 10;
        }
        return false;
    }
    
    public static int skipSevenSum(int n) {
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            if (!containsSeven(i)) {
                sum += i;
            }
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(skipSevenSum(n));
        scanner.close();
    }
}