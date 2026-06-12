package org.example;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.apache.commons.lang3.StringUtils;
import java.util.Scanner;
import java.io.InputStream;
import java.util.Properties;

public class Main {
    private static final Logger logger = LoggerFactory.getLogger(Main.class);

    public static void main(String[] args) {
        logger.info("Приложение запущено");

        try (InputStream input = Main.class.getClassLoader().getResourceAsStream("build-passport.properties")) {
            if (input != null) {
                Properties prop = new Properties();
                prop.load(input);

                System.out.println("Пользователь: " + prop.getProperty("build.user"));
                System.out.println("ОС: " + prop.getProperty("build.os"));
                System.out.println("Java: " + prop.getProperty("build.java.version"));
                System.out.println("Время сборки: " + prop.getProperty("build.time"));
                System.out.println("Сообщение: " + prop.getProperty("build.message"));

                logger.info("Build passport загружен успешно");
            } else {
                logger.warn("Файл build-passport.properties не найден");
            }
        } catch (Exception e) {
            logger.error("Ошибка при чтении build-passport.properties", e);
        }

        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String input = scanner.nextLine();

        logger.info("Пользователь ввел: {}", input);

        String reversed = StringUtils.reverse(input);
        String capitalized = StringUtils.capitalize(input);

        logger.info("Перевернутая строка: {}", reversed);
        logger.info("С заглавной буквы: {}", capitalized);

        logger.info("Приложение завершено");
    }
}
