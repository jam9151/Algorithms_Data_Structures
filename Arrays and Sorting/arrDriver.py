import random


def main():
    arrList = []
    for i in range(10):
        for i in range(10):
            arrList[i].append(random.randrange(0,100))
        print(arrList[i])

    sortedArr = []
    for i in arrList:
        sortedArr.append(func(i))
    
    for i in sortedArr:
        print(i)
    


    return




if __name__ == '__main__':
    main()
