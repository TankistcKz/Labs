package main

import "fmt"

type Student struct {
    Name     string
    Age      int
    Course   int
    AvgGrade float64
}

func (s Student) GetStatus() string {
    switch {
    case s.AvgGrade >= 4.5:
        return "отличник"
    case s.AvgGrade >= 3.5:
        return "хорошист"
    default:
        return "троечник"
    }
}

func (s Student) PrintInfo() {
    fmt.Printf("Студент: %s\n", s.Name)
    fmt.Printf("Возраст: %d\n", s.Age)
    fmt.Printf("Курс: %d\n", s.Course)
    fmt.Printf("Средний балл: %.2f\n", s.AvgGrade)
    fmt.Printf("Статус: %s\n", s.GetStatus())
}

func main() {
    student := Student{
        Name:     "Иван Иванов",
        Age:      20,
        Course:   2,
        AvgGrade: 4.7,
    }

    student.PrintInfo()
}