import random

#For Terminal Display
debug   = 0
reverse = 0
display = 0
delete  = 0
insert  = 0
destroy = 0

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


#takes array and generates linked list, returns head
def generateListFromArr(arr):
    if not arr:
        return None

    head = Node(arr[0])
    temp = head

    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

#Turning Linked list to array
def linkedListToArr(head):
    arr = []
    temp = head
    while(temp != None):
        arr.append(temp.val)
        temp = temp.next
    print(arr)
    return arr

#displays linked list like so val1 -> val2 -> val3 ->
def traverseLinkedList(head):
    temp = head
    returnStr = ''
    while(temp != None):
        returnStr += f' {temp.val} ->'
        temp = temp.next
    return returnStr

    
#reverse linked list
def reverseLinkedList(head):
    '''
    Visual example of what its doing.
    p   c    n  
        1 -> 2 -> 3 -> 4 ->
    p   c    n     
     <- 1 -> 2 -> 3 -> 4 ->
        p    c    n
     <- 1 <- 2 -> 3 -> 4 ->
             
     <- 1 <- 2 <- 3 -> 4 ->
                  
     <- 1 <- 2 <- 3 <- 4
    '''

    current = head
    prev = None

    while(current != None):
        next = current.next
    
        current.next = prev
        
        prev = current
        
        current = next
    head = prev  
    return head

#deletes node by finding val
def deleteNode(head, val):
    '''
    p   c   
        1 -> 2 -> 3 -> 4 ->
        p    c
        1 -> 2 -> 3 -> 4 ->
             p    c
        1 -> 2 -> 3 -> 4 ->

        1 -> 2  3  4 -> 
        
        remove 3
        1 -> 2 -> 4
             3
    '''

    # Edge case: empty list
    if head is None:
        return None
    
    # Case where the head node is the one to be deleted
    if head.val == val:
        return head.next
    
    # Initialize pointers
    prev = None
    current = head
    
    # Traverse the list
    while current is not None:
        if current.val == val:
            # Delete the current node
            prev.next = current.next
            return head
        prev = current
        current = current.next
    
    # Return the head if the val was not found
    return head

#inserts new node at idx with node.val = val
def insertNode(head,val,idx):

    #if the head does not exist return new Node
    if not head:
        return Node(val)
    
    #if idx is at the front
    if idx == 0:
        newNode = Node(val)
        newNode.next = head
        return newNode
    
    i = 0
    current = head
    prev = None
    
    #find insert position
    while(i != idx and current):
        prev = current
        current = current.next
        i = i+1
    
    #insert Node
    newNode = Node(val)
    if prev:
        prev.next = newNode
    newNode.next = current

    return head

#destroy entire linked list
def destroyList(head):
    
    while head != None:
        prev = head
        head = head.next
        del(prev)
    del(head)
    
    return None


def main():
    linkedLists = []
    arrList = [[],[],[],[],[],[],[],[],[],[]]

    #populate arrList with random arrays
    for i in range(0,10):
        for j in range(random.randrange(10)):
            arrList[i].append(random.randrange(0,100))
    
    print("<<<<<<<<<<ArrayList>>>>>>>>>>")
    #populate linkedLists
    for i in arrList:
        print(i)
        linkedLists.append(generateListFromArr(i))
    
    if debug:

        print("<<<<<<<<<<Array to Linked List>>>>>>>>>>")
        #print linked List vals
        for i in linkedLists:
            linkedListToArr(i)
    
    if display:

        print("<<<<<<<<<<Display Nodes>>>>>>>>>>")
        #print linked List vals
        for i in linkedLists:
            print(traverseLinkedList(i))
    
    if reverse:

        print("<<<<<<<<<<Reverse Linked List>>>>>>>>>>>")
        #reverse the linked list
        for i in range(len(linkedLists)-1):
            linkedLists[i] = reverseLinkedList(linkedLists[i])
        
        if display:
            print("<<<<<<<<<<Display Nodes>>>>>>>>>>")
            #print linked List vals
            for i in linkedLists:
                print(traverseLinkedList(i))
    
    if debug:
        #print linkedLists again
        for i in linkedLists:
            linkedListToArr(i)
    
    if delete:
        
        print("<<<<<<<<<<Deleting Nodes>>>>>>>>>>")
        for i in range(len(arrList)):
            for j in range(len(arrList[i])):
                linkedLists[i] = deleteNode(linkedLists[i], arrList[i][j])
        
        if display:
            print("<<<<<<<<<<Display Nodes>>>>>>>>>>")
            #print linked List vals
            for i in linkedLists:
                print(traverseLinkedList(i))

    if insert:
        print("<<<<<<<<<<Inserting Value Into List>>>>>>>>>>")
        

        for i in range(len(arrList)):
            val = random.randrange(100)
            linkedLists[i] = insertNode(linkedLists[i],val,random.randrange(len(arrList)))
        
        if display:
            print("<<<<<<<<<<Display Nodes>>>>>>>>>>")
            #print linked List vals
            for i in linkedLists:
                print(traverseLinkedList(i))

    if destroy:
        print("<<<<<<<<<<Destroying Linked Lists>>>>>>>>>>>")
        for i in range(len(linkedLists)):
            linkedLists[i] = destroyList(linkedLists[i])
        \
        if display:
            print("<<<<<<<<<<Display Nodes>>>>>>>>>>")
            #print linked List vals
            for i in linkedLists:
                print(traverseLinkedList(i))
        
            

if __name__ == '__main__':
    main()


