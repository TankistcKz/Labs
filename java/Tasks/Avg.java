import java.util.Scanner;
public class Avg {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("");
        int num1 = scanner.nextInt();
        
        System.out.print("");
        int num2 = scanner.nextInt();
        
        System.out.print("");
        int num3 = scanner.nextInt();
        
        double result = average(num1, num2, num3);
        System.out.println(result);
        
        scanner.close();
    }

    public static double average(int a, int b, int c) {
        return (a + b + c) / 3.0;
    }
}