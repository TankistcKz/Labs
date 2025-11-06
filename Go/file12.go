package main

import (
	"fmt"
	"sort"
)

func FindElement(slice []int, target int) (int, bool) {
	for index, value := range slice {
		if value == target {
			return index, true
		}
	}
	return -1, false
}

func SortSlice(slice []int) []int {
	sorted := make([]int, len(slice))
	copy(sorted, slice)
	sort.Ints(sorted)
	return sorted
}

func FilterSlice(slice []int) []int {
	var filtered []int
	for _, value := range slice {
		if value%2 == 0 {
			filtered = append(filtered, value)
		}
	}
	return filtered
}

func main() {
	numbers := []int{5, 3, 8, 1, 9, 4, 2, 7, 6}

	if index, found := FindElement(numbers, 8); found {
		fmt.Printf("Элемент 8 найден на позиции %d\n", index)
	} else {
		fmt.Println("Элемент не найден")
	}

	sorted := SortSlice(numbers)
	fmt.Println("Отсортированный срез:", sorted)

	filtered := FilterSlice(numbers)
	fmt.Println("Отфильтрованный срез (только чётные):", filtered)
}