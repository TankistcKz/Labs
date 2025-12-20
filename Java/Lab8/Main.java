import java.lang.annotation.*;
import java.lang.reflect.Method;
import java.util.*;
import java.util.stream.Collectors;
import java.util.concurrent.*;
import java.io.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
@interface DataProcessor {
}

class DataManager {
    private List<String> data = new ArrayList<>();
    private List<Method> processors = new ArrayList<>();
    private Object processorObj;
    
    public void registerDataProcessor(Object processor) {
        this.processorObj = processor;
        for (Method m : processor.getClass().getMethods()) {
            if (m.isAnnotationPresent(DataProcessor.class)) {
                processors.add(m);
            }
        }
    }
    
    public void loadData(String source) {
        try (BufferedReader br = new BufferedReader(new FileReader(source))) {
            data = br.lines().collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public void processData() {
        ExecutorService executor = Executors.newFixedThreadPool(2);
        
        try {
            List<String> result = executor.submit(() -> {
                return data.stream()
                    .map(item -> {
                        for (Method m : processors) {
                            try {
                                item = (String) m.invoke(processorObj, item);
                            } catch (Exception e) {}
                        }
                        return item;
                    })
                    .distinct()
                    .sorted()
                    .collect(Collectors.toList());
            }).get();
            
            data = result;
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            executor.shutdown();
        }
    }
    
    public void saveData(String destination) {
        try (PrintWriter pw = new PrintWriter(destination)) {
            data.forEach(pw::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

class MyProcessor {
    @DataProcessor
    public String process1(String s) {
        return s.trim();
    }
    
    @DataProcessor
    public String process2(String s) {
        return s.toUpperCase();
    }
}

public class Main {
    public static void main(String[] args) throws Exception {
        PrintWriter pw = new PrintWriter("input.txt");
        pw.println("apple");
        pw.println("  banana  ");
        pw.println("sliva");
        pw.println("apple");
        pw.close();
        
        DataManager manager = new DataManager();

        manager.registerDataProcessor(new MyProcessor());

        manager.loadData("input.txt");

        manager.processData();

        manager.saveData("output.txt");
    }
}