import random as rd


def BOGO(arr1):
    # Use a breakpoint in the code line below to debug your script.
    arr2 = []
    for i in range(0, len(arr1)):
        arr2.append(arr1.pop(rd.randint(0, len(arr1) - 1)))
    return arr2


# Press the green button in the gutter to run the script.
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
sorted = False
while (not sorted):
    list = BOGO(list)
    for i in range(0, len(list) - 1):
        if (list[i] > list[i + 1]):
            sorted = False
            break
        else:
            sorted = True

print(list)
