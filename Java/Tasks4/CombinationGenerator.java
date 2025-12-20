import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class CombinationGenerator {
    
    public static List<String> bruteForce(int n, int k) {
        List<String> result = new ArrayList<>();
        
        if (n > k) {
            return result;
        }
        
        boolean[] used = new boolean[k];
        generate("", n, k, used, result);
        
        return result;
    }
    
    private static void generate(String current, int remaining, int k, boolean[] used, List<String> result) {
        if (remaining == 0) {
            result.add(current);
            return;
        }
        
        for (int i = 0; i < k; i++) {
            if (!used[i]) {
                used[i] = true;
                generate(current + i, remaining - 1, k, used, result);
                used[i] = false;
            }
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] parts = input.split(",");
        
        int n = Integer.parseInt(parts[0]);
        int k = Integer.parseInt(parts[1]);
        
        List<String> result = bruteForce(n, k);
        
        System.out.print("[");
        for (int i = 0; i < result.size(); i++) {
            System.out.print("\"" + result.get(i) + "\"");
            if (i < result.size() - 1) {
                System.out.print(",");
            }
        }
        System.out.println("]");
        
        scanner.close();
    }
}