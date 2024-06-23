package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Generates random array
func generateRandomArray(SIZE int) []int {
	// Seed the random number generator to ensure different results each run
	rand.Seed(time.Now().UnixNano())

	fmt.Println("\nCreating Random Array with size -> ", SIZE, "\n")
	//Creates enough memory to hold integers
	arr := make([]int, SIZE)

	for i := 0; i < SIZE; i++ {
		arr[i] = rand.Intn(1000)
	}
	return arr
}
