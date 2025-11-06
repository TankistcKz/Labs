package main

import (
	"fmt"
	"strings"
	"unicode"
)

func countWords(text string) map[string]int {
    frequency := make(map[string]int)
    
    words := strings.FieldsFunc(text, func(r rune) bool {
        return !unicode.IsLetter(r) && !unicode.IsNumber(r)
    })
    
    for _, word := range words {
        lowerWord := strings.ToLower(word)
        frequency[lowerWord]++
    }
    return frequency
}

func main() {
    text := `Т-64 (индекс ГБТУ «Объект 432») — советский средний танк, принятый на вооружение в 1966 году Армией СССР. 
	Разработан в 1960—1967 годах в Харьковском конструкторском бюро машиностроения Харьковского завода транспортного машиностроения имени Малышева на базе Объекта 430А. 
	Серийно производился в 1963—1969 годах, за это время было построено 1192 машины.`
    
    wordFrequency := countWords(text)
    
    fmt.Println("Частота слов в тексте:")
    for word, count := range wordFrequency {
        fmt.Printf("%s: %d\n", word, count)
    }
}