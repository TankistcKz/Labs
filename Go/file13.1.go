package main

import "fmt"

func incrementByValue(num int) {
    num++
    fmt.Println("Внутри incrementByValue:", num)
}

func incrementByPointer(num *int) {
    *num++
    fmt.Println("Внутри incrementByPointer:", *num)
}

func main() {
    value := 10
    pointerValue := 10

    fmt.Println("Исходные значения:", value, pointerValue)
    incrementByValue(value)
    fmt.Println("После incrementByValue:", value)
    incrementByPointer(&pointerValue)
    fmt.Println("После incrementByPointer:", pointerValue)
}