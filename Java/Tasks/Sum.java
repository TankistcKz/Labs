import java.util.Scanner;

public class Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int number = scanner.nextInt();

        int sum = digitSum(number);
        System.out.println(sum);
        scanner.close();
    }

    public static int digitSum(int number) {
        int sum = 0;
        int n = Math.abs(number);
        
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
}