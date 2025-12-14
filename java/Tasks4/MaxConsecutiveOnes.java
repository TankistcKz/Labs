import java.util.Scanner;

public class MaxConsecutiveOnes {
    
    public static int maxConsecutiveOnes(int[] arr) {
        int maxCount = 0;
        int currentCount = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1) {
                currentCount++;
                if (currentCount > maxCount) {
                    maxCount = currentCount;
                }
            } else {
                currentCount = 0;
            }
        }
        
        return maxCount;
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
        
        System.out.println(maxConsecutiveOnes(arr));
        
        scanner.close();
    }
}