import java.util.Scanner;

public class PositiveSumCalculator {
    public static int sumOfPositives(int[] arr) {
        int sum = 0;
        
        for (int num : arr) {
            if (num > 0) {
                sum += num;
            }
        }
        return sum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        input = input.replace("[", "").replace("]", "");
        String[] parts = input.split(",");
        int[] arr = new int[parts.length];
        
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i].trim());
        }
        
        int result = sumOfPositives(arr);
        System.out.println(result);
        scanner.close();
    }
}