import java.util.Scanner;

public class Season {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int month = scanner.nextInt();

        String result = season(month);
        System.out.println(result);
        
        scanner.close();
    }

    public static String season(int month) {
        if (month == 12 || month == 1 || month == 2) {
            return "зима";
        } else if (month >= 3 && month <= 5) {
            return "весна";
        } else if (month >= 6 && month <= 8) {
            return "лето";
        } else if (month >= 9 && month <= 11) {
            return "осень";
        } else {
            return "неверный месяц";
        }
    }
}