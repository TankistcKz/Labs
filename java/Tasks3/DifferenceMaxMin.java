import java.util.Scanner;

public class DifferenceMaxMin {
    
    public static int differenceMaxMin(int[] arr) {
        int max = arr[0];
        int min = arr[0];

        for (int num : arr) {
            if (num > max) {
                max = num;
            }
            if (num < min) {
                min = num;
            }
        }
        
        return max - min;
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

        int result = differenceMaxMin(arr);
        System.out.println(result);
        scanner.close();
    }
}