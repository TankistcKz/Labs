package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Sonderkraftfarzeug"

	runeCount := len([]rune(str))
	fmt.Printf("Количество символов: %d\n", runeCount)

	substr := "zeug"
	index := strings.Index(str, substr)
	if index != -1 {
		fmt.Printf("Подстрока '%s' найдена на позиции %d\n", substr, index)
	} else {
		fmt.Printf("Подстрока '%s' не найдена\n", substr)
	}

	lower := strings.ToLower(str)
	upper := strings.ToUpper(str)
	title := strings.Title(lower)
	titleCase := strings.ToTitle(lower)

	fmt.Println("\nИзменение регистра:")
	fmt.Println("В нижнем регистре:", lower)
	fmt.Println("В верхнем регистре:", upper)
	fmt.Println("Title case:", title)
	fmt.Println("Title case:", titleCase)
}