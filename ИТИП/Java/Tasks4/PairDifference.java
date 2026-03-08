import java.util.Scanner;

public class PairDifference {
    
    public static int pairDifference(int[] arr, int k) {
        int count = 0;
        
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (Math.abs(arr[i] - arr[j]) == k) {
                    count++;
                }
            }
        }
        
        return count;
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
        
        String kPart = input.substring(closeBracket + 1).trim();
        int k = Integer.parseInt(kPart.substring(1).trim());
        
        System.out.println(pairDifference(arr, k));
        
        scanner.close();
    }
}