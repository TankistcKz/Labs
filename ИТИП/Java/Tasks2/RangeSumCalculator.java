import java.util.Scanner;

public class RangeSumCalculator {
    public static int sumRange(int a, int b) {
        int n = b - a + 1;
        int sum = n * (a + b) / 2;
        return sum;
    }
    
    public static int sumRangeLoop(int a, int b) {
        int sum = 0;
        for (int i = a; i <= b; i++) {
            sum += i;
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        String[] numbers = input.split(", ");
        int a = Integer.parseInt(numbers[0]);
        int b = Integer.parseInt(numbers[1]);
        
        int result = sumRange(a, b);
        System.out.println(result);
    }
}