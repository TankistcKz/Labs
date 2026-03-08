import java.util.regex.*;
import java.util.Scanner;

public class IPAddressValidator {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String ipAddress = scanner.nextLine();
        
        if (isValidIP(ipAddress)) {
            System.out.println("✓");
        } else {
            System.out.println("✗");
            System.out.println("- Правильный формат: xxx.xxx.xxx.xxx");
            System.out.println("- где xxx - число от 0 до 255");
        }
        scanner.close();
    }
    
    public static boolean isValidIP(String ip) {
        String intPattern = "(25[0-5]|2[0-4]\\d|1\\d{2}|[1-9]?\\d)";
        String ipPattern = "^" + intPattern + "\\." + intPattern + "\\." + 
                          intPattern + "\\." + intPattern + "$";
        
        Pattern pattern = Pattern.compile(ipPattern);
        Matcher matcher = pattern.matcher(ip);
        return matcher.matches();
    }
}