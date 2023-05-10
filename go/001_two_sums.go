package main

import "fmt"

func twoSum(nums []int, target int) []int {
	for x := 0; x < len(nums); x++ {
		for y := 1; y < len(nums); y++ {
			if x == y {
				continue
			} else if nums[x]+nums[y] == target {
				return []int{x, y}
			}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(twoSum([]int{1, 2, 5, 3, 5}, 3))
	fmt.Println(twoSum([]int{3, 2, 3}, 6))
	fmt.Println(twoSum([]int{2, 5, 5, 11}, 10))
}
