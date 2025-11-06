package main

import "fmt"

func removeElement(slice []string, index int) []string {
    if index < 0 || index >= len(slice) {
        return slice
    }
    return append(slice[:index], slice[index+1:]...)
}

func main() {
    fruits := []string{"Яблоко", "Банан", "Апельсин", "Груша", "Киви"}
    fmt.Println("Исходный срез:", fruits)
    
    fruits = removeElement(fruits, 2)
    fmt.Println(fruits)
}