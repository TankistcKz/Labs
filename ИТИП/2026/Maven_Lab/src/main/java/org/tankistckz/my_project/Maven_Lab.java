package org.tankistckz.my_project;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Maven_Lab {
    private static final Logger logger = LogManager.getLogger(Maven_Lab.class);
    
    public static void main(String[] args) {
        logger.info("Приложение запущено");
        
        Person person = new Person("Иван", "Иванов", 25);
        logger.info("Создан объект Person: {}", person);
        
        JsonProcessor processor = new JsonProcessor();
        String json = processor.toJson(person);
        logger.info("JSON: {}", json);
        
        Person deserializedPerson = processor.fromJson(json, Person.class);
        logger.info("Десериализованный объект: {}", deserializedPerson);
    }
}