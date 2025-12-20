import java.util.Scanner;
import java.util.Arrays;
import java.util.HashSet;

public class MergeUniqueSorted {
    public static int[] mergeUniqueSorted(int[] a, int[] b) {
        HashSet<Integer> set = new HashSet<>();

        for (int num : a) {
            set.add(num);
        }

        for (int num : b) {
            set.add(num);
        }

        int[] result = new int[set.size()];
        int index = 0;
        for (int num : set) {
            result[index++] = num;
        }

        Arrays.sort(result);
        return result;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);    
        String input = scanner.nextLine();
        
        String[] parts = input.split("\\],\\s*\\[");
        String firstArray = parts[0].replace("[", "").trim();
        String secondArray = parts[1].replace("]", "").trim();
        
        int[] a;
        if (firstArray.isEmpty()) {
            a = new int[0];
        } else {
            String[] firstElements = firstArray.split(",");
            a = new int[firstElements.length];
            for (int i = 0; i < firstElements.length; i++) {
                a[i] = Integer.parseInt(firstElements[i].trim());
            }
        }
        
        int[] b;
        if (secondArray.isEmpty()) {
            b = new int[0];
        } else {
            String[] secondElements = secondArray.split(",");
            b = new int[secondElements.length];
            for (int i = 0; i < secondElements.length; i++) {
                b[i] = Integer.parseInt(secondElements[i].trim());
            }
        }
        
        int[] result = mergeUniqueSorted(a, b);
        System.out.print("[");
        for (int i = 0; i < result.length; i++) {
            System.out.print(result[i]);
            if (i < result.length - 1) {
                System.out.print(",");
            }
        }
        System.out.println("]");
        scanner.close();
    }
}