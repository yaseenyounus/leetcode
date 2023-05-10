package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	strX := strconv.Itoa(x)

	for i := 0; i < len(strX)/2; i++ {
		if strX[i] != strX[len(strX)-1-i] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}
