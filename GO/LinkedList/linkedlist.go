package main

import "fmt"

type Node struct {
	val  int
	next *Node
}

type LinkedList struct {
	Head *Node
}

func LinkedListFromArr(arr []int) *Node {
	if len(arr) == 0 {
		return nil
	}

	head := &Node{val: arr[0], next: nil}
	temp := head

	for i := 1; i < len(arr); i++ {
		temp.next = &Node{val: arr[i], next: nil}
		temp = temp.next
	}

	return head
}

func traverseLinkedList(head *Node) {

	temp := head

	for temp != nil {
		fmt.Println("Val = ", temp.val)
		temp = temp.next

	}

}
