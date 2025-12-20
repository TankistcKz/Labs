import java.util.Scanner;

public class SecondLargest {
    
    public static int secondLargest(int[] arr) {
        int first = Integer.MIN_VALUE;
        int second = Integer.MIN_VALUE;
        
        for (int num : arr) {
            if (num > first) {
                second = first;
                first = num;
            } else if (num > second && num != first) {
                second = num;
            }
        }
        return second;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        input = input.replace("[", "").replace("]", "").replace(" ", "");
        String[] parts = input.split(",");
        
        int[] arr = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i]);
        }
        
        int result = secondLargest(arr);
        System.out.println(result);
        scanner.close();
    }
}