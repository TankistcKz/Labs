package main

import "fmt"

func addGrade(grades map[string]int, name string, grade int) {
    grades[name] = grade
}

func findGrade(grades map[string]int, name string) int {
    if grade, exists := grades[name]; exists {
        return grade
    }
    return 0
}

func removeGrade(grades map[string]int, name string) {
    delete(grades, name)
}

func main() {
    grades := make(map[string]int)
    
    addGrade(grades, "Владимир", 5)
    addGrade(grades, "Мария", 4)
    addGrade(grades, "Иван", 3)
    

    fmt.Println("Оценка Владимира:", findGrade(grades, "Владимир"))
    fmt.Println("Оценка Сани:", findGrade(grades, "Саня"))
    
    removeGrade(grades, "Иван")
    fmt.Println("Оценка Ивана после удаления:", findGrade(grades, "Иван"))
    
    fmt.Println("Все оценки:", grades)
}