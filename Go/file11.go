package main

import "fmt"

type Student struct {
    Name      string
    Age       int
    Course    int
    AvgGrade  float64
}

func NewStudent(name string, age, course int, avgGrade float64) Student {
    return Student{
        Name:     name,
        Age:      age,
        Course:   course,
        AvgGrade: avgGrade,
    }
}

func (s Student) PrintInfo() {
    fmt.Printf("Студент: %s\n", s.Name)
    fmt.Printf("Возраст: %d\n", s.Age)
    fmt.Printf("Курс: %d\n", s.Course)
    fmt.Printf("Средний балл: %.2f\n", s.AvgGrade)
}

func (s *Student) Promote() {
    s.Course++
    fmt.Printf("%s переведен на %d курс\n", s.Name, s.Course)
}

func (s *Student) UpdateGrade(newGrade float64) {
    s.AvgGrade = newGrade
    fmt.Printf("Средний балл %s обновлен: %.2f\n", s.Name, s.AvgGrade)
}

func main() {
    student := NewStudent("Иван Петров", 20, 2, 4.5)
    student.PrintInfo()
    student.Promote()
    student.UpdateGrade(4.7)
    student.PrintInfo()
}