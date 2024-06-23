import random


'''
    Understand what partition is doing.
    It takes as input and arr, low, and high     



'''
#swaps highest and lowest values in a sub array then returns the idx of the lowest value
def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    print(f"Swapping {array[i+1]} and {array[high]}")
    array[i+1], array[high] = array[high], array[i+1]

    print(f'Swapping {array[i+1]} with {array[low]}')
    return i+1


#uses recursion to split the array into shorter and shorter sub arrays, based on the pivot which is determined by partition.
def quickSort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quickSort(array, low, pivot_index-1)
        quickSort(array, pivot_index+1, high)
    return array

'''
iteration trial run.
arr = [5,4,3,2,1]
1.quicksort(arr,0,None)
    high = 4

    low < high
        pivot_idx = arr,0,4 -> 1
            pivot = 1
            from 0 to 4
                if 5 <= 1 no
                if 4 <= 1 no
                if 3 <= 1 no
                if 2 <= 1 no
            [5,4,3,2,1] = [1, |4,3,2,5]
            return 0

        


'''



def main():
    listArr = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(len(listArr)-1):
        for i in range(10):
            listArr[i].append(random.randrange(0,100))
    
    print("<<<<<<<<UNSORTED>>>>>>>")
    for i in listArr:
        print(i)
    print("<<<<<<<<SORTED>>>>>>>")
    sortedList = []
    for i in listArr:
        sortedList.append(quickSort(i))
    
    print("Sorted List")
    for i in sortedList:
        print(i)
    return




if __name__ == '__main__':
    main()