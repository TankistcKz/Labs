import java.util.Scanner;
import java.util.Arrays;

public class FilterEven {
    
    public static int[] filterEven(int[] arr) {
        int count = 0;
        for (int num : arr) {
            if (num % 2 == 0) {
                count++;
            }
        }

        int[] result = new int[count];
        int index = 0;

        for (int num : arr) {
            if (num % 2 == 0) {
                result[index++] = num;
            }
        }
        
        return result;
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

        int[] result = filterEven(arr);
        System.out.println(Arrays.toString(result));
        scanner.close();
    }
}