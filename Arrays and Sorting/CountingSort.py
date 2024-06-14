import random



def CountingSort(arr):

    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr




def main():
    arrList = [[],[],[],[],[],[],[],[],[],[]]
    print("Unsorted Arr")
    for i in range(0,10):
        for i in range(0,10):
            arrList[i].append(random.randrange(0,100))
        #print(arrList[i])
    for i in arrList:
        print(i)

    sortedArr = []
    for i in arrList:
        sortedArr.append(CountingSort(i))
    print("Sorted Arr")
    for i in sortedArr:
        print(i)
    


    return




if __name__ == '__main__':
    main()