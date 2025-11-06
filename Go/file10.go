package main

import "fmt"

func main() {
    var num1, num2 int

    fmt.Print("Введите первое число: ")
    fmt.Scan(&num1)

    fmt.Print("Введите второе число: ")
    fmt.Scan(&num2)

    sum := num1 + num2
    fmt.Printf("%d + %d = %d\n", num1, num2, sum)

    difference := num1 - num2
    fmt.Printf("%d - %d = %d\n", num1, num2, difference)

    product := num1 * num2
    fmt.Printf("%d * %d = %d\n", num1, num2, product)

    if num2 != 0 {
        quotient := num1 / num2
        fmt.Printf("%d / %d = %d\n", num1, num2, quotient)
    } else {
        fmt.Println("Деление на ноль невозможно")
    }

    if num2 != 0 {
        remainder := num1 % num2
        fmt.Printf("%d %% %d = %d\n", num1, num2, remainder)
    } else {
        fmt.Println("Остаток от деления на ноль невозможен")
    }
}