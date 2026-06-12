package org.example;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

public class AssertionsTest {
    @Test
    void shouldCheckAssertions() {
        String value = "Spring";
        
        assertEquals("Spring", value);
        assertNotNull(value);
        assertTrue(value.startsWith("Sp"));
        assertFalse(value.isEmpty());
    }

    @Test
    void shouldThrowException() {
        assertThrows(ArithmeticException.class, () -> {
            int result = 10 / 0;
        });
    }

    @BeforeEach
    void setUp() {
        System.out.println("Подготовка перед каждым тестом");
    }

    @AfterEach
    void tearDown() {
        System.out.println("Завершение после каждого теста");
    }

    @BeforeAll
    static void beforeAll() {
        System.out.println("Один раз перед всеми тестами");
    }

    @AfterAll
    static void afterAll() {
        System.out.println("Один раз после всех тестов");
    }

    @Test
    void firstTest() {
        System.out.println("Первый тест");
    }

    @Test
    void secondTest() {
        System.out.println("Второй тест");
    }
}
