package org.tankistckz.my_project;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import com.fasterxml.jackson.databind.ObjectMapper;

public class JsonProcessor {
    private static final Logger logger = LogManager.getLogger(JsonProcessor.class);
    private final ObjectMapper objectMapper;
    
    public JsonProcessor() {
        this.objectMapper = new ObjectMapper();
    }
    
    public String toJson(Object obj) {
        try {
            return objectMapper.writeValueAsString(obj);
        } catch (Exception e) {
            logger.error("Ошибка сериализации в JSON", e);
            return null;
        }
    }
    
    public <T> T fromJson(String json, Class<T> clazz) {
        try {
            return objectMapper.readValue(json, clazz);
        } catch (Exception e) {
            logger.error("Ошибка десериализации из JSON", e);
            return null;
        }
    }
}