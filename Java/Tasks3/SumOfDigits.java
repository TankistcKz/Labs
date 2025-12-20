import java.util.Scanner;

public class SumOfDigits {
    public static int sumOfDigits(int number) {
        int sum = 0;
        number = Math.abs(number);
        
        while (number > 0) {
            sum += number % 10;
            number /= 10;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input = scanner.nextInt();
        
        int result = sumOfDigits(input);
        System.out.println(result);
        scanner.close();
    }
}