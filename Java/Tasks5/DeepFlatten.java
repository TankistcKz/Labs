import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class DeepFlatten {
    public static void flattenRecursive(Object obj, List<Integer> result) {
        if (obj instanceof List) {
            List<?> list = (List<?>) obj;
            for (Object item : list) {
                flattenRecursive(item, result);
            }
        } else if (obj instanceof Integer) {
            result.add((Integer) obj);
        }
    }
    
    public static List<Integer> deepFlatten(List<?> input) {
        List<Integer> result = new ArrayList<>();
        flattenRecursive(input, result);
        return result;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        List<Object> list = parseInput(input);
        List<Integer> result = deepFlatten(list);
        
        System.out.println(result);
        scanner.close();
    }
    
    public static List<Object> parseInput(String s) {
        List<Object> result = new ArrayList<>();
        List<List<Object>> stack = new ArrayList<>();
        stack.add(result);
        
        for (int i = 1; i < s.length() - 1; i++) {
            char c = s.charAt(i);
            if (c == '[') {
                List<Object> newList = new ArrayList<>();
                stack.get(stack.size() - 1).add(newList);
                stack.add(newList);
            } else if (c == ']') {
                stack.remove(stack.size() - 1);
            } else if (Character.isDigit(c) || c == '-') {
                int j = i;
                while (j < s.length() && (Character.isDigit(s.charAt(j)) || s.charAt(j) == '-')) {
                    j++;
                }
                stack.get(stack.size() - 1).add(Integer.parseInt(s.substring(i, j)));
                i = j - 1;
            }
        }
        return result;
    }
}