package main

import (
	"fmt"
	"strings"
)

func main() {
	sentence := "Schwerer Panzerspähwagen Sieben Komma FÜNF Zentimeter Sonderkraftfahrzeug Zweihundertvierunddreissig / VIER Panzerabwehrkanonenwagen"

	words := strings.Split(sentence, " ")
	fmt.Println("Разбиение предложения на слова:")
	for i, word := range words {
		fmt.Printf("%d: %s\n", i+1, word)
	}
}