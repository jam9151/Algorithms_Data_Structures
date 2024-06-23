import random
import QuickSort



'''
Very simple
O(nlogn)

1. let left = 0
2. let right = len(arr)-1
3. while left <= right
4. find middle index of array, if val is left of mid, let left = mid+1, if val right of mid, let right = mid-1, if val = mid. return val
5. if its not found return -1

'''

def BinarySearch(arr,val):
    left = 0
    right = len(arr)-1

    while left <= right:
        
        mid = (left + right) // 2

        if val == arr[mid]:
            return mid
        
        if val > arr[mid]:
            left = mid + 1
        
        else:
            right = mid - 1
    
    return -1






def main():
    arrList = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(10):
        for i in range(10):
            arrList[i].append(random.randrange(0,100))
        print(arrList[i])

    sortedArr = []
    for i in arrList:
        sortedArr.append(QuickSort.quickSort(i))
    
    for i in sortedArr:
        print(i)


    #testing Binary Search
    print("Testing Binary Search")
    for i in sortedArr:
        val = i[random.randrange(10)]
        print(f"{val} is in {i} at idx {BinarySearch(i,val)}")

if __name__ == '__main__':
    main()