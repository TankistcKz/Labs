import java.util.Scanner;
import java.util.Arrays;

public class ArrayRotator {
    public static int[] rotateRight(int[] arr, int k) {
        if (arr.length == 0 || arr.length == 1) {
            return arr;
        }
        
        k = k % arr.length;
        
        if (k == 0) {
            return arr;
        }
        
        int[] result = new int[arr.length];
        
        for (int i = 0; i < arr.length; i++) {
            result[(i + k) % arr.length] = arr[i];
        }
        
        return result;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);        
        String input = scanner.nextLine();
        
        int lastComma = input.lastIndexOf(',');
        String arrayInput = input.substring(0, lastComma).trim();
        int k = Integer.parseInt(input.substring(lastComma + 1).trim());
        
        arrayInput = arrayInput.replace("[", "").replace("]", "").trim();
        
        if (arrayInput.isEmpty()) {
            System.out.println("[]");
            scanner.close();
            return;
        }
        
        String[] parts = arrayInput.split(",");
        int[] arr = new int[parts.length];
        
        for (int i = 0; i < parts.length; i++) {
            arr[i] = Integer.parseInt(parts[i].trim());
        }
        
        int[] result = rotateRight(arr, k);
        System.out.println(Arrays.toString(result));
        scanner.close();
    }
}