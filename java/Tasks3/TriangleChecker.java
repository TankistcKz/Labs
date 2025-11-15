import java.util.Scanner;

public class TriangleChecker {
    
    public static boolean isTriangle(int a, int b, int c) {
        return (a + b > c) && (a + c > b) && (b + c > a);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        input = input.replace(" ", "");
        String[] parts = input.split(",");

        int a = Integer.parseInt(parts[0]);
        int b = Integer.parseInt(parts[1]);
        int c = Integer.parseInt(parts[2]);

        boolean result = isTriangle(a, b, c);
        System.out.println(result);
        scanner.close();
    }
}