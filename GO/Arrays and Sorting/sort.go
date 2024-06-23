package main

import (
	"fmt"
)

// Returns index of valye where the
func BinarySearch(arr []int, val int) int {

	if len(arr) == 0 {
		return -1
	}

	fmt.Println("Peforming Binary Search with arr ", arr, " and val", val, "\n")

	left := 0
	right := len(arr) - 1

	for left <= right {
		// Calculates Middle point
		mid := left + (right-left)/2

		//if mid is the idx looking for, return it. if its greater move left, if its less move right
		if arr[mid] == val {
			fmt.Println(val, " found at arr index ", mid, "\n")
			return mid
		}

		if val > arr[mid] {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	fmt.Println("Value not found, Returning -1")
	//if value is not found return -1
	return -1
}

// No Return Val, O(N^2) TC
func BubbleSort(arr []int) {

	fmt.Println("Sorting Array With Bubble Sort. Arr = ", arr, "\n")

	for i := 0; i < len(arr)-1; i++ {

		for j := 0; j < len(arr)-i-1; j++ {

			if arr[j] > arr[j+1] {
				temp := arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
			}
		}
	}
	fmt.Println("Sorted Array = ", arr, "\n")
}

func Partition(arr []int, low int, high int) int {
	pivot := arr[high]
	i := low - 1

	for j := low; j < high; j++ {
		if arr[j] < pivot {
			i++
			arr[i], arr[j] = arr[j], arr[i]
		}
	}
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return i + 1

}

func QuickSort(arr []int, low int, high int) {

	if low < high {
		p := Partition(arr, low, high)
		QuickSort(arr, low, p-1)
		QuickSort(arr, p+1, high)
	}

}
