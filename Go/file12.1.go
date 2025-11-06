package main

import "fmt"

func FindLongestString(strings ...string) string {
	if len(strings) == 0 {
		return ""
	}

	longest := strings[0]
	for _, str := range strings {
		if len(str) > len(longest) {
			longest = str
		}
	}
	return longest
}

func main() {
	result := FindLongestString("T-64", "swehrer panzerspähwagen sieben komma fünf zentimeter sonderkraftfahrzeug zweihundertvierunddreissig vier panzerwerhkanonenwagen",
	 "APFSDS", "m4a2e3", "Mark V")
	fmt.Println("Самая длинная строка:", result)
}