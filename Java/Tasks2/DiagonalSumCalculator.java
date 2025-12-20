import java.util.Scanner;

public class DiagonalSumCalculator {
    public static int diagonalSum(int[][] matrix) {
        int sum = 0;
        
        for (int i = 0; i < matrix.length; i++) {
            sum += matrix[i][i];
        }
        
        return sum;
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();

        input = input.trim();
        if (input.startsWith("[[") && input.endsWith("]]")) {
            input = input.substring(2, input.length() - 2);
        }

        String[] rows = input.split("\\],\\[");
        int n = rows.length;
        
        int[][] matrix = new int[n][n];

        for (int i = 0; i < n; i++) {
            String[] elements = rows[i].split(",");
            for (int j = 0; j < elements.length; j++) {
                matrix[i][j] = Integer.parseInt(elements[j].trim());
            }
        }
        
        int result = diagonalSum(matrix);
        System.out.println(result);
        scanner.close();
    }
}