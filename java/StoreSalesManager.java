import java.util.*;
import java.util.concurrent.CopyOnWriteArrayList;

class Product {
    private String name;
    private double price;
    private int quantitySold;
    
    public Product(String name, double price, int quantitySold) {
        this.name = name;
        this.price = price;
        this.quantitySold = quantitySold;
    }
    
    public String getName() {
        return name;
    }
    
    public double getPrice() {
        return price;
    }
    
    public int getQuantitySold() {
        return quantitySold;
    }
    
    public double getTotalRevenue() {
        return price * quantitySold;
    }
    
    @Override
    public String toString() {
        return String.format("%-20s | Цена: %8.2f руб | Продано: %4d шт | Выручка: %10.2f руб", 
                           name, price, quantitySold, getTotalRevenue());
    }
}

public class StoreSalesManager {
    public static void main(String[] args) {
        CopyOnWriteArrayList<Product> products = new CopyOnWriteArrayList<>();

        products.add(new Product("Молоко", 85.50, 150));
        products.add(new Product("Хлеб", 25.00, 200));
        products.add(new Product("Масло сливочное", 320.00, 80));
        products.add(new Product("Сыр", 450.00, 60));
        products.add(new Product("Яйца куриные", 120.00, 95));
        products.add(new Product("Йогурт", 75.00, 110));
        products.add(new Product("Кефир", 68.00, 130));
        products.add(new Product("Творог", 180.00, 70));
        
        displayProducts(products);
        calculateStatistics(products);
        demonstrateConcurrentSafety(products);
    }

    private static void displayProducts(CopyOnWriteArrayList<Product> products) {
        int counter = 1;
        for (Product p : products) {
            System.out.printf("%2d. %s%n", counter++, p);
        }
    }

    private static void calculateStatistics(CopyOnWriteArrayList<Product> products) {
        double totalRevenue = 0;
        int totalQuantity = 0;
        Product mostPopular = null;
        double maxRevenue = 0;
        Product bestRevenue = null;
        
        for (Product p : products) {
            double revenue = p.getTotalRevenue();
            totalRevenue += revenue;
            totalQuantity += p.getQuantitySold();
            
            if (mostPopular == null || p.getQuantitySold() > mostPopular.getQuantitySold()) {
                mostPopular = p;
            }

            if (revenue > maxRevenue) {
                maxRevenue = revenue;
                bestRevenue = p;
            }
        }
        
        System.out.println("Общая сумма продаж:" + String.format("%,15.2f", totalRevenue) + " руб");
        System.out.println("Всего продано единиц:" + String.format("%,15d", totalQuantity) + " шт");
        System.out.println("Количество наименований:" + String.format("%,15d", products.size()));
        System.out.println("Средняя выручка на товар:" + 
                         String.format("%,15.2f", totalRevenue / products.size()) + " руб");
        
        if (mostPopular != null) {
            System.out.println("Самый популярный товар (по количеству):");
            System.out.println("    " + mostPopular.getName() + " - " + 
                             mostPopular.getQuantitySold() + " шт");
        }
        
        if (bestRevenue != null) {
            System.out.println("Лидер по выручке:");
            System.out.println("    " + bestRevenue.getName() + " - " + 
                             String.format("%.2f", bestRevenue.getTotalRevenue()) + " руб");
        }
    }
    
    private static void demonstrateConcurrentSafety(CopyOnWriteArrayList<Product> products) {
        int count = 0;
        for (Product p : products) {
            count++;
            if (count == 3) {
                products.add(new Product("Сметана", 95.00, 85));
            }
            if (count <= 4) {
                System.out.println("    " + count + ". " + p.getName());
            }
        }
        System.out.println("\nТекущее количество товаров:" + products.size());
    }
}