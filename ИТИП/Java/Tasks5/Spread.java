import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Spread {
    public static double spread(List<Integer> arr) {
        if (arr.isEmpty()) return 0;
        
        int max = arr.get(0);
        int min = arr.get(0);
        int sum = 0;
        
        for (int num : arr) {
            if (num > max) max = num;
            if (num < min) min = num;
            sum += num;
        }
        
        double avg = (double) sum / arr.size();
        
        if (avg == 0) return 0;
        
        return (max - min) / avg;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        List<Integer> arr = new ArrayList<>();
        String[] parts = input.replace("[", "").replace("]", "").split(",");
        
        for (String part : parts) {
            arr.add(Integer.parseInt(part.trim()));
        }
        
        System.out.println(spread(arr));
        scanner.close();
    }
}