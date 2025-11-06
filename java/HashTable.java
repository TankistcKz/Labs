import java.util.LinkedList;


public class HashTable<K, V> {
    private LinkedList<Entry<K, V>>[] table;
    private int size;
    private static final int DEFAULT_CAPACITY = 16;
    
    @SuppressWarnings("unchecked")
    public HashTable() {
        table = new LinkedList[DEFAULT_CAPACITY];
        size = 0;
    }
    
    private int hash(K key) {
        return Math.abs(key.hashCode()) % table.length;
    }
    
    public void put(K key, V value) {
        int index = hash(key);
        if (table[index] == null) {
            table[index] = new LinkedList<Entry<K, V>>();
        }
        
        for (Entry<K, V> entry : table[index]) {
            if (entry.getKey().equals(key)) {
                entry.setValue(value);
                return;
            }
        }
        
        table[index].add(new Entry<K, V>(key, value));
        size++;
    }
    
    public V get(K key) {
        int index = hash(key);
        if (table[index] == null) {
            return null;
        }
        
        for (Entry<K, V> entry : table[index]) {
            if (entry.getKey().equals(key)) {
                return entry.getValue();
            }
        }
        
        return null;
    }
    
    public V remove(K key) {
        int index = hash(key);
        if (table[index] == null) {
            return null;
        }
        
        for (Entry<K, V> entry : table[index]) {
            if (entry.getKey().equals(key)) {
                V value = entry.getValue();
                table[index].remove(entry);
                size--;
                return value;
            }
        }
        
        return null; 
    }
    
    public int size() {
        return size;
    }
    
    public boolean isEmpty() {
        return size == 0;
    }
    
    public void display() {
        for (int i = 0; i < table.length; i++) {
            if (table[i] != null) {
                System.out.print("Индекс " + i + ": ");
                for (Entry<K, V> entry : table[i]) {
                    System.out.print("[" + entry.getKey() + " -> " + entry.getValue() + "] ");
                }
                System.out.println();
            }
        }
    }
    
    public static void main(String[] args) {
        HashTable<Integer, Order> orderTable = new HashTable<>();
        
        String[] dishes1 = {"Стейк", "Картофель", "Салат"};
        Order order1 = new Order(dishes1, 2500.0, "18:30");
        
        String[] dishes2 = {"Паста", "Суп", "Вино"};
        Order order2 = new Order(dishes2, 1800.0, "19:15");
        
        String[] dishes3 = {"Рыба", "Рис", "Овощи"};
        Order order3 = new Order(dishes3, 2200.0, "20:00");
        
        orderTable.put(5, order1);
        orderTable.put(12, order2);
        orderTable.put(8, order3);
        
        orderTable.display();
        
        Order foundOrder = orderTable.get(12);
        if (foundOrder != null) {
            System.out.println("Заказ для столика 12: " + foundOrder);
        } else {
            System.out.println("Заказ для столика 12 не найден");
        }
        
        Order removedOrder = orderTable.remove(5);
        if (removedOrder != null) {
            System.out.println("Удален заказ: " + removedOrder);
        }
        
        orderTable.display();
        
        System.out.println("Количество заказов: " + orderTable.size());
        System.out.println("Таблица пуста: " + orderTable.isEmpty());
        
        String[] updatedDishes = {"Паста", "Суп", "Вино", "Десерт"};
        Order updatedOrder = new Order(updatedDishes, 2100.0, "19:15");
        orderTable.put(12, updatedOrder);
        
        System.out.println("Обновленный заказ для столика 12: " + orderTable.get(12));
    }
}

class Entry<K, V> {
    private K key;
    private V value;
    
    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }
    
    public K getKey() {
        return key;
    }
    
    public V getValue() {
        return value;
    }
    
    public void setValue(V value) {
        this.value = value;
    }
}

class Order {
    private String[] dishes;
    private double totalCost;
    private String orderTime;
    
    public Order(String[] dishes, double totalCost, String orderTime) {
        this.dishes = dishes;
        this.totalCost = totalCost;
        this.orderTime = orderTime;
    }
    
    public String[] getDishes() {
        return dishes;
    }
    
    public void setDishes(String[] dishes) {
        this.dishes = dishes;
    }
    
    public double getTotalCost() {
        return totalCost;
    }
    
    public void setTotalCost(double totalCost) {
        this.totalCost = totalCost;
    }
    
    public String getOrderTime() {
        return orderTime;
    }
    
    public void setOrderTime(String orderTime) {
        this.orderTime = orderTime;
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Заказ {");
        sb.append("Блюда: ");
        for (String dish : dishes) {
            sb.append(dish).append(", ");
        }
        sb.append(" | Стоимость: ").append(totalCost);
        sb.append(" | Время: ").append(orderTime);
        sb.append("}");
        return sb.toString();
    }
}
