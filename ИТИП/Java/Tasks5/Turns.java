import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Turns {
    public static int turns(int num) {
        List<Integer> digits = new ArrayList<>();
        int temp = num;
        
        while (temp > 0) {
            digits.add(0, temp % 10);
            temp /= 10;
        }
        
        if (digits.size() < 2) return 0;
        
        int direction = 0;
        int turnCount = 0;
        
        for (int i = 1; i < digits.size(); i++) {
            if (digits.get(i) > digits.get(i - 1)) {
                if (direction == -1) {
                    turnCount++;
                }
                direction = 1;
            } else if (digits.get(i) < digits.get(i - 1)) {
                if (direction == 1) {
                    turnCount++;
                }
                direction = -1;
            }
        }
        
        return turnCount;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        System.out.println(turns(n));
        scanner.close();
    }
}