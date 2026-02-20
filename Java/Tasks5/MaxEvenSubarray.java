import java.util.Scanner;

public class MaxEvenSubarray {
    
    public static int maxEvenSubarray(int[] arr) {
        int maxEvenSum = 0;
        
        for (int i = 0; i < arr.length; i++) {
            int sum = 0;
            for (int j = i; j < arr.length; j++) {
                sum += arr[j];
                if (sum % 2 == 0 && sum > maxEvenSum && (j - i + 1) < arr.length) {
                    maxEvenSum = sum;
                }
            }
        }
        
        return maxEvenSum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        int openBracket = input.indexOf('[');
        int closeBracket = input.indexOf(']');
        String arrayPart = input.substring(openBracket + 1, closeBracket);
        String[] elements = arrayPart.split(",");
        
        int[] arr = new int[elements.length];
        for (int i = 0; i < elements.length; i++) {
            arr[i] = Integer.parseInt(elements[i].trim());
        }
        
        System.out.println(maxEvenSubarray(arr));
        
        scanner.close();
    }
}