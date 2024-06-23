/*
Notes
	1. Var vs :=. := can only be used inside functions
	2. %d for Decimal, %x for Hex, %o for Octal, %b = Binary
	3. Printing strings is as simple as fmt.println(string)
	4. Printing array is as simple as fmt.Println(Array)
	5. Datatypes = int,string,float64,bool
	6. 2d array, with row and col, matrix:=make([][]int,rows), the iterate over and make the col using m

*/

package main

import (
	"fmt"
	"math/rand"
	"time"
)

var DEBUG bool = true
var SIZE int = 10000000
var BBS bool = false
var BS bool = true
var QS bool = true

func main() {
	// Generates random array
	arr := generateRandomArray()

	fmt.Println("Array = ", arr, "\n")

	if BBS {
		BubbleSort(arr)
	}

	if QS {
		QuickSort(arr, 0, len(arr)-1)
	}
	if BS {
		BinarySearch(arr, arr[rand.Intn(SIZE-1)])
	}
}

// Generates random array
func generateRandomArray() []int {
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
