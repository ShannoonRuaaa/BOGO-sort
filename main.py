import random as rd

## BOGO sort
# BOGO sort is a sorting algorithm that shuffles the list until it is sorted.
# The average time complexity is O(n*n!)
# The worst case is O(∞)

# @param arr1: the array to be shuffled
def BOGO(arr1):
    arr2 = []
    for i in range(0, len(arr1)):
        arr2.append(arr1.pop(rd.randint(0, len(arr1) - 1)))
    return arr2


def BOGOsort(list):
    sorted = False
    while (not sorted):
        list = BOGO(list)
        for i in range(0, len(list) - 1):
            if (list[i] > list[i + 1]):
                sorted = False
                break
            else:
                sorted = True
    return list
list = [ 2 ,1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 ,14 ,15 ,16 ,17 ,18 ,19, 20 ,21, 22, 23, 24, 25]
print ("start sorting...")
print(BOGOsort(list))
