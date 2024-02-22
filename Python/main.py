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

# @param list: the list to be sorted
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

# Ask user for list
list = []
type = int(input("Type (1: element/line, 2: line): "))
if type == 1:
    while True:
        x = input("#: ")
        if x == "done" or x == "exit":
            break
        else:
            try:
                list.append(int(x))
            except:
                print("Invalid input, try again")
else: 
    while True:
        x = input("line: ")
        try:
            if "," in x:
                list = [int(y) for y in x.split(", ")]
            else:
                list = [int(y) for y in x.split(" ")]
            break
        except:
            print("Invalid input, try again")

print("")
print("start sorting...")
print(BOGOsort(list))
