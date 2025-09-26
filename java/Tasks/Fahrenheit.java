import java.util.Scanner;

public class Fahrenheit {
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("");
        double celsius = scanner.nextDouble();
        
        double fahrenheit = toFahrenheit(celsius);
        System.out.println(fahrenheit);
        scanner.close();
        }
        
    public static double toFahrenheit(double celsius) {
        return celsius * 9.0 / 5.0 + 32;
    }
    
}
