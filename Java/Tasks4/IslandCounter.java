import java.util.Scanner;

public class IslandCounter {
    
    public static int countIslands(int[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int count = 0;
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == 1 && !visited[i][j]) {
                    dfs(grid, visited, i, j);
                    count++;
                }
            }
        }
        
        return count;
    }
    
    private static void dfs(int[][] grid, boolean[][] visited, int i, int j) {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || 
            visited[i][j] || grid[i][j] == 0) {
            return;
        }
        
        visited[i][j] = true;
        
        dfs(grid, visited, i + 1, j);
        dfs(grid, visited, i - 1, j);
        dfs(grid, visited, i, j + 1);
        dfs(grid, visited, i, j - 1);
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        
        input = input.replace("[[", "").replace("]]", "");
        String[] rows = input.split("\\],\\[");
        
        int[][] grid = new int[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            String[] elements = rows[i].split(",");
            grid[i] = new int[elements.length];
            for (int j = 0; j < elements.length; j++) {
                grid[i][j] = Integer.parseInt(elements[j].trim());
            }
        }
        
        System.out.println(countIslands(grid));
        
        scanner.close();
    }
}