public class MatrixMaxThreads {
    private static int[][] matrix = {
        {12, 45, 23, 67, 89},
        {34, 78, 91, 15, 42},
        {56, 29, 73, 88, 11},
        {98, 62, 37, 51, 24}
    };
    
    private static int[] threadMaxValues;
    private static int globalMax;
    
    static class RowMaxThread extends Thread {
        private int rowIndex;
        private int threadId;
        
        public RowMaxThread(int rowIndex, int threadId) {
            this.rowIndex = rowIndex;
            this.threadId = threadId;
        }
        
        @Override
        public void run() {  
            int maxInRow = matrix[rowIndex][0];
            
            for (int j = 1; j < matrix[rowIndex].length; j++) {
                if (matrix[rowIndex][j] > maxInRow) {
                    maxInRow = matrix[rowIndex][j];
                }
            }
            
            threadMaxValues[threadId] = maxInRow;
        }
    }
    
    public static void main(String[] args) {
        int rows = matrix.length;
        threadMaxValues = new int[rows];

        RowMaxThread[] threads = new RowMaxThread[rows];

        for (int i = 0; i < rows; i++) {
            threads[i] = new RowMaxThread(i, i);
            threads[i].start();
        }

        try {
            for (int i = 0; i < rows; i++) {
                threads[i].join();
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        globalMax = threadMaxValues[0];
        for (int i = 0; i < threadMaxValues.length; i++) {
            if (threadMaxValues[i] > globalMax) {
                globalMax = threadMaxValues[i];
            }
        }
        System.out.println(globalMax);
    }
}