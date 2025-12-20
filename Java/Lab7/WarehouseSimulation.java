import java.util.concurrent.*;
import java.util.ArrayList;
import java.util.List;

public class WarehouseSimulation {
    static class Product {
        private String name;
        private int weight;
        
        public Product(String name, int weight) {
            this.name = name;
            this.weight = weight;
        }
        
        public String getName() {
            return name;
        }
        
        public int getWeight() {
            return weight;
        }
        
        @Override
        public String toString() {
            return name + " (" + weight + " кг)";
        }
    }

    static class Warehouse {
        private List<Product> products;
        private int maxWeight = 150;
        
        public Warehouse() {
            products = new ArrayList<>();
            products.add(new Product("Телевизор", 45));
            products.add(new Product("Холодильник", 80));
            products.add(new Product("Стиральная машина", 70));
            products.add(new Product("Микроволновка", 25));
            products.add(new Product("Диван", 95));
            products.add(new Product("Шкаф", 120));
            products.add(new Product("Стол", 40));
            products.add(new Product("Кресло", 30));
            products.add(new Product("Пылесос", 15));
        }
        
        public List<Product> getProducts() {
            return products;
        }
        
        public int getMaxWeight() {
            return maxWeight;
        }
    }

    static class Loader implements Callable<LoaderResult> {
        private int loaderId;
        private List<Product> assignedProducts;
        private int maxWeight;
        
        public Loader(int loaderId, List<Product> assignedProducts, int maxWeight) {
            this.loaderId = loaderId;
            this.assignedProducts = assignedProducts;
            this.maxWeight = maxWeight;
        }
        
        @Override
        public LoaderResult call() throws Exception {
            int totalWeight = 0;
            List<Product> movedProducts = new ArrayList<>();
            
            for (Product product : assignedProducts) {
                if (totalWeight + product.getWeight() <= maxWeight) {;
                    totalWeight += product.getWeight();
                    movedProducts.add(product);
                    
                    System.out.println("Грузчик " + loaderId + " перенес " + product);
                } else {
                    System.out.println("Грузчик " + loaderId + " превышен лимит веса: " + (totalWeight + product.getWeight()) + " > " + maxWeight + " кг");
                }
            }
            return new LoaderResult(loaderId, movedProducts, totalWeight);
        }
    }

    static class LoaderResult {
        private int loaderId;
        private List<Product> movedProducts;
        private int totalWeight;
        
        public LoaderResult(int loaderId, List<Product> movedProducts, int totalWeight) {
            this.loaderId = loaderId;
            this.movedProducts = movedProducts;
            this.totalWeight = totalWeight;
        }
        
        public int getLoaderId() {
            return loaderId;
        }
        
        public List<Product> getMovedProducts() {
            return movedProducts;
        }
        
        public int getTotalWeight() {
            return totalWeight;
        }
    }
    
    public static void main(String[] args) {
        Warehouse warehouse = new Warehouse();
        List<Product> products = warehouse.getProducts();

        ExecutorService executor = Executors.newFixedThreadPool(3);
        CompletionService<LoaderResult> completionService = new ExecutorCompletionService<>(executor);

        int productsPerLoader = products.size() / 3;
        int remainder = products.size() % 3;
        
        int startIndex = 0;
        for (int i = 0; i < 3; i++) {
            int endIndex = startIndex + productsPerLoader + (i < remainder ? 1 : 0);
            List<Product> assignedProducts = products.subList(startIndex, endIndex);
            
            Loader loader = new Loader(i + 1, assignedProducts, warehouse.getMaxWeight());
            completionService.submit(loader);
            
            startIndex = endIndex;
        }
        
        List<LoaderResult> results = new ArrayList<>();
        try {
            for (int i = 0; i < 3; i++) {
                Future<LoaderResult> future = completionService.take();
                LoaderResult result = future.get();
                results.add(result);
            }
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }

        executor.shutdown();

        int totalMovedProducts = 0;
        int totalWeight = 0;
        
        for (LoaderResult result : results) {
            System.out.println("Грузчик " + result.getLoaderId() + ":");
            System.out.println("Перенесено товаров: " + result.getMovedProducts().size());
            System.out.println("Общий вес: " + result.getTotalWeight() + " кг");
            System.out.println("Список товаров:");
            for (Product product : result.getMovedProducts()) {
                System.out.println("    - " + product);
            }
            
            totalMovedProducts += result.getMovedProducts().size();
            totalWeight += result.getTotalWeight();
        }
    }
}