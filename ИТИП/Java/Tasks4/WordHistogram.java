import java.util.Scanner;
import java.util.Map;
import java.util.LinkedHashMap;

public class WordHistogram {
    
    public static Map<String, Integer> wordHistogram(String text) {
        Map<String, Integer> histogram = new LinkedHashMap<>();
        
        String cleanText = text.toLowerCase().replaceAll("[^a-zA-Z0-9\\s]", "");
        String[] words = cleanText.split("\\s+");
        
        for (String word : words) {
            if (!word.isEmpty()) {
                histogram.put(word, histogram.getOrDefault(word, 0) + 1);
            }
        }
        
        return histogram;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        Map<String, Integer> result = wordHistogram(input);
        
        System.out.print("{");
        int count = 0;
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            System.out.print(entry.getKey() + ": " + entry.getValue());
            count++;
            if (count < result.size()) {
                System.out.print(", ");
            }
        }
        System.out.println("}");
        
        scanner.close();
    }
}