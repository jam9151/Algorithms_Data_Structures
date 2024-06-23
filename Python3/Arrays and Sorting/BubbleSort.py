"""
    TC = O(n^2)
    SC = O(1)
    Bubble passes through the array switching minimum and maximum values

    1. Iterate over array using i to index the length of array 
    2.      iterate from length of array - i - 1 to make sure you dont over index
    3.          if arr[j] > arr[j+1]
    4.              swap arr[j] and arr[j+1]

"""

def bubbleSort(arr):
    #1
    for i in range(len(arr)-1):
        #2
        for j in range(len(arr)-i-1):
            #3
            if arr[j] > arr[j+1]:
                #4
                x = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = x
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

    sortedArr = []
    
    for i in listArr:
        sortedArr.append(bubbleSort(i))
    
    for i in listArr:
        print(i)
    

if __name__ == '__main__':
    main()


