package main

import "fmt"

func main() {
    slice := make([]string, 0, 3)
    
    fmt.Println("Начальное состояние:")
    fmt.Printf("Длина: %d, Емкость: %d, Содержимое: %v\n", len(slice), cap(slice), slice)
    
    slice = append(slice, "Как же я")
    slice = append(slice, "люблю")
    slice = append(slice, "убивать")
    
    fmt.Println("\nПосле добавления 3 элементов:")
    fmt.Printf("Длина: %d, Емкость: %d, Содержимое: %v\n", len(slice), cap(slice), slice)
    
    slice = append(slice, "время")
    slice = append(slice, "за танками")
    
    fmt.Println("\nПосле добавления 5 элементов:")
    fmt.Printf("Длина: %d, Емкость: %d, Содержимое: %v\n", len(slice), cap(slice), slice)
    
    fmt.Println("\nВсе элементы среза:")
    for i, value := range slice {
        fmt.Printf("Индекс: %d, Значение: %s\n", i, value)
    }
}