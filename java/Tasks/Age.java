import java.util.Scanner;

public class Age {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("");
        int age = scanner.nextInt();

        String result = checkAge(age);
        System.out.println(result);
        scanner.close();
    }

    public static String checkAge(int age) {
        if (age >= 18) {
            return "совершеннолетний";
        } else {
            return "несовершеннолетний";
        }
    }
}