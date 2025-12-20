import java.util.regex.*;
import java.util.Scanner;

public class PasswordValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String password = scanner.nextLine();
        
        Pattern pattern = Pattern.compile("^(?=.*[A-Z])(?=.*\\d)[A-Za-z\\d]{8,16}$");
        Matcher matcher = pattern.matcher(password);
        
        if (matcher.matches()) {
            System.out.println("✓");
        } else {
            if (password.length() < 8 || password.length() > 16) {
                System.out.println("- Длина должна быть от 8 до 16 символов");
            }
            if (!password.matches(".*[A-Z].*")) {
                System.out.println("- Должна быть хотя бы одна заглавная буква");
            }
            if (!password.matches(".*\\d.*")) {
                System.out.println("- Должна быть хотя бы одна цифра");
            }
            if (!password.matches("[A-Za-z\\d]*")) {
                System.out.println("- Допустимы только латинские буквы и цифры");
            }
        }
        scanner.close();
    }
}