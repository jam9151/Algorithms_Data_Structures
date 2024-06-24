package main

import (
	"fmt"
)

var SIZE int = 100
var DEBUG bool = true

func main() {

	fmt.Println()
	arr := generateRandomArray(SIZE)
	fmt.Print(arr)

	linkedList := LinkedListFromArr(arr)
	traverseLinkedList((linkedList))

}
