package main

import "fmt"

func main() {
    var year int

    fmt.Print("Введите год: ")
    fmt.Scan(&year)

    isLeap := (year%400 == 0) || (year%100 != 0 && year%4 == 0)

    if isLeap {
        fmt.Printf("високосный")
    } else {
        fmt.Printf("не високосный")
    }
}