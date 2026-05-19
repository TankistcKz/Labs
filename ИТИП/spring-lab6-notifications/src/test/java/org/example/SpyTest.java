package org.example;

import org.junit.jupiter.api.Test;
import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.*;

public class SpyTest {

    @Test
    void shouldDemonstrateSpyOnList() {
        // 1. Создаём реальный список
        List<String> realList = new ArrayList<>();
        
        // 2. Оборачиваем его в spy
        List<String> spyList = spy(realList);
        
        // 3. Используем spy — вызывается реальный метод add()
        spyList.add("Spring");
        spyList.add("Boot");
        spyList.add("Test");
        
        // 4. Проверяем, что методы были вызваны
        verify(spyList).add("Spring");
        verify(spyList, times(1)).add("Boot");
        verify(spyList, atLeastOnce()).add("Test");
        
        // 5. Реальный список изменился
        assertEquals(3, spyList.size());
        assertEquals("Spring", spyList.get(0));
        
        // 6. Можно переопределить поведение метода
        when(spyList.size()).thenReturn(100);
        
        // 7. Теперь size() возвращает 100, а не реальный размер
        assertEquals(100, spyList.size());
        
        // 8. Остальные методы работают реально
        assertEquals("Spring", spyList.get(0));  // реальное значение
    }
    
    @Test
    void shouldDemonstrateSpyVsMock() {
        // Mock — полностью поддельный объект
        List<String> mockList = mock(List.class);
        mockList.add("Hello");
        
        // Проверка: метод add был вызван, но реального добавления НЕ произошло
        verify(mockList).add("Hello");
        assertEquals(0, mockList.size());  // size() возвращает 0 (значение по умолчанию)
        
        // Spy — реальный объект
        List<String> realList = new ArrayList<>();
        List<String> spyList = spy(realList);
        spyList.add("Hello");
        
        // Проверка: метод add был вызван И реальное добавление ПРОИЗОШЛО
        verify(spyList).add("Hello");
        assertEquals(1, spyList.size());  // реальный размер
    }
    
    @Test
    void shouldSpyOnUserService() {
        // Пример использования spy для частичного мокирования списка
        List<String> names = new ArrayList<>();
        List<String> spyNames = spy(names);
        
        // Реальное поведение
        spyNames.add("Иван");
        spyNames.add("Петр");
        spyNames.add("Сидор");
        
        // Проверяем размер
        assertEquals(3, spyNames.size());
        
        // Проверяем значения
        assertEquals("Иван", spyNames.get(0));
        assertEquals("Петр", spyNames.get(1));
        assertEquals("Сидор", spyNames.get(2));
        
        // Переопределяем метод get() для первого элемента
        when(spyNames.get(0)).thenReturn("Анна");
        
        // Теперь get(0) возвращает "Анна" (из stubbing)
        assertEquals("Анна", spyNames.get(0));
        
        // get(1) и get(2) работают реально
        assertEquals("Петр", spyNames.get(1));
        assertEquals("Сидор", spyNames.get(2));
        
        // Проверяем вызовы add
        verify(spyNames).add("Иван");
        verify(spyNames).add("Петр");
        verify(spyNames).add("Сидор");
    }
}
