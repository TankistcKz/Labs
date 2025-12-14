import java.util.Scanner;
import java.util.LinkedHashMap;
import java.util.Map;

public class GradeEvaluator {
    
    public static Map<String, Integer> evaluateGrades(int[] grades) {
        Map<String, Integer> result = new LinkedHashMap<>();
        result.put("A", 0);
        result.put("B", 0);
        result.put("C", 0);
        result.put("D", 0);
        result.put("F", 0);
        
        for (int grade : grades) {
            if (grade >= 90 && grade <= 100) {
                result.put("A", result.get("A") + 1);
            } else if (grade >= 80 && grade <= 89) {
                result.put("B", result.get("B") + 1);
            } else if (grade >= 70 && grade <= 79) {
                result.put("C", result.get("C") + 1);
            } else if (grade >= 60 && grade <= 69) {
                result.put("D", result.get("D") + 1);
            } else {
                result.put("F", result.get("F") + 1);
            }
        }
        
        Map<String, Integer> filteredResult = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : result.entrySet()) {
            if (entry.getValue() > 0) {
                filteredResult.put(entry.getKey(), entry.getValue());
            }
        }
        
        return filteredResult;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        int openBracket = input.indexOf('[');
        int closeBracket = input.indexOf(']');
        String arrayPart = input.substring(openBracket + 1, closeBracket);
        String[] elements = arrayPart.split(",");
        
        int[] grades = new int[elements.length];
        for (int i = 0; i < elements.length; i++) {
            grades[i] = Integer.parseInt(elements[i].trim());
        }
        
        Map<String, Integer> result = evaluateGrades(grades);
        
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