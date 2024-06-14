

'''
    TC = O(n^2)
    SC = O(1)
    Note Do not use .pop or .insert
    if you used it would be O(n^3)

    
    
    1. iterate over list from 0 to length of array-1 using i to index
    2.  set minimum index to i
    3.  iterate over the aray from i+1 to len(arr)
    4.      if arr[minimum index] > arr[j]
    5.          set minimum index to j
    6.  swap arr[min index] with arr[i]
        
'''     




def selectionSort(arr):
    
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<NEW ARRAY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print(f"Working with arr = {arr}")
    
    #1
    for i in range(len(arr)-1):
        
        #2
        minIndex = i
        print(f"min idx = {minIndex}")
    
        #3
        for j in range(i+1,len(arr)):
            
            #4
            if arr[minIndex] > arr[j]:
                print(f"{arr[minIndex]} < {arr[j]}")
    
                #5
                minIndex = j
                print(f"minIdx = {j} now")
    
        #6
        minVal = arr[minIndex]
        print(f"swaping {arr[i]} with {arr[minIndex]}")

        x = arr[i]
        arr[i] = minVal
        arr[minIndex] = x
    
    return arr




def main():
    
    listArr = [
        [9,8,7,6,5,4,3,2,1],
        [9,283,5,1,2,5,78,12,3,142,12424],
        [],
        [10,9,8,7,6,5,4,3,2,1,0],
        [193,2,-1,33,1,6,123,23,15],
        [0,1,2,3,4,5,7,6,8,7,9],
        [100,9,99,2,33,124,61,1626,0],
    ]


    sortedList = []
    for i in listArr:
        sortedList.append(selectionSort(i))
    
    print("Sorted List")
    for i in sortedList:
        print(i)
if __name__ == '__main__':
    main()

'''
ITERATION TEST
    [9,8,7,6,5,4,3,2,1,0]
    Working with arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    min idx = 0
    9 < 8
    minIdx = 1 now
    8 < 7
    minIdx = 2 now
    7 < 6
    minIdx = 3 now
    6 < 5
    minIdx = 4 now
    5 < 4
    minIdx = 5 now
    4 < 3
    minIdx = 6 now
    3 < 2
    minIdx = 7 now
    2 < 1
    minIdx = 8 now
    swaping 9 with 1
    min idx = 1
    8 < 7
    minIdx = 2 now
    7 < 6
    minIdx = 3 now
    6 < 5
    minIdx = 4 now
    5 < 4
    minIdx = 5 now
    4 < 3
    minIdx = 6 now
    3 < 2
    minIdx = 7 now
    swaping 8 with 2
    min idx = 2
    7 < 6
    minIdx = 3 now
    6 < 5
    minIdx = 4 now
    5 < 4
    minIdx = 5 now
    4 < 3
    minIdx = 6 now
    swaping 7 with 3
    min idx = 3
    6 < 5
    minIdx = 4 now
    5 < 4
    minIdx = 5 now
    swaping 6 with 4
    min idx = 4
    swaping 5 with 5
    min idx = 5
    swaping 6 with 6
    min idx = 6
    swaping 7 with 7
    min idx = 7
    swaping 8 with 8
    [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''