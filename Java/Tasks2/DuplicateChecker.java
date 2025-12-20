import java.util.Scanner;
import java.util.HashSet;

public class DuplicateChecker {
    public static boolean hasDuplicates(int[] arr) {
        HashSet<Integer> seen = new HashSet<>();
        
        for (int num : arr) {
            if (seen.contains(num)) {
                return true;
            }
            seen.add(num);
        }
        
        return false;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        input = input.replace("[", "").replace("]", "").trim();

        if (input.isEmpty()) {
            System.out.println(false);
            scanner.close();
            return;
        }
        
        String[] parts = input.split(",");
        int[] arr = new int[parts.length];
        
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i].trim());
        }
        
        boolean result = hasDuplicates(arr);
        System.out.println(result);
        scanner.close();
    }
}