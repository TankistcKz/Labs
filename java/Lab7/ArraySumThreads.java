public class ArraySumThreads {
    private static int[] array = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    private static int sum1 = 0;
    private static int sum2 = 0;
    private static int totalSum = 0;
    
    static class FirstHalfThread extends Thread {
        @Override
        public void run() {
            int localSum = 0;
            int halfLength = array.length / 2;
            
            for (int i = 0; i < halfLength; i++) {
                localSum += array[i];
            }
            sum1 = localSum;
        }
    }
    
    static class SecondHalfThread extends Thread {
        @Override
        public void run() {
            int localSum = 0;
            int halfLength = array.length / 2;
            
            for (int i = halfLength; i < array.length; i++) {
                localSum += array[i];
            }
            sum2 = localSum;
        }
    }
    
    public static void main(String[] args) {
        FirstHalfThread thread1 = new FirstHalfThread();
        SecondHalfThread thread2 = new SecondHalfThread();
        
        thread1.start();
        thread2.start();
        
        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        
        totalSum = sum1 + sum2;
        System.out.println(totalSum);
    }
}