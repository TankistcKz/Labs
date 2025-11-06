package main

import (
	"fmt"
	"os"
)

func main() {
	var a, b float64
	var operator string

	fmt.Println("Введите первое число:")
	fmt.Scanln(&a)

	fmt.Println("Введите оператор (+, -, *, /):")
	fmt.Scanln(&operator)

	fmt.Println("Введите второе число:")
	fmt.Scanln(&b)

	result := 0.0
	errorMsg := ""

	switch operator {
	case "+":
		result = a + b
	case "-":
		result = a - b
	case "*":
		result = a * b
	case "/":
		if b == 0 {
			errorMsg = "Ошибка: деление на ноль"
		} else {
			result = a / b
		}
	default:
		errorMsg = "Ошибка: неизвестный оператор"
	}

	if errorMsg != "" {
		fmt.Println(errorMsg)
		os.Exit(1)
	}

	fmt.Printf("Результат: %.2f %s %.2f = %.2f\n", a, operator, b, result)
}