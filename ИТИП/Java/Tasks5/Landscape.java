import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;

public class Landscape {
    public static boolean isLandscape(List<Integer> arr) {
        if (arr.size() < 3) return false;
        
        int peakIndex = -1;
        
        for (int i = 1; i < arr.size(); i++) {
            if (arr.get(i) <= arr.get(i - 1)) {
                peakIndex = i - 1;
                break;
            }
        }
        
        if (peakIndex <= 0 || peakIndex >= arr.size() - 1) return false;
        
        for (int i = peakIndex + 1; i < arr.size(); i++) {
            if (arr.get(i) >= arr.get(i - 1)) {
                return false;
            }
        }
        
        return true;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        List<Integer> arr = new ArrayList<>();
        String[] parts = input.replace("[", "").replace("]", "").split(",");
        
        for (String part : parts) {
            arr.add(Integer.parseInt(part.trim()));
        }
        
        System.out.println(isLandscape(arr));
        scanner.close();
    }
}