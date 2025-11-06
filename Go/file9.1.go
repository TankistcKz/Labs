package main

import "fmt"

func main() {
	var dayNumber int

	fmt.Println("Введите номер дня недели (1-7):")
	fmt.Scanln(&dayNumber)

	dayName := ""

	switch dayNumber {
	case 1:
		dayName = "Понедельник"
	case 2:
		dayName = "Вторник"
	case 3:
		dayName = "Среда"
	case 4:
		dayName = "Четверг"
	case 5:
		dayName = "Пятница"
	case 6:
		dayName = "Суббота"
	case 7:
		dayName = "Воскресенье"
	default:
		dayName = "Неверный номер дня"
	}

	fmt.Println(dayName)
}