# ineffective algo
# create a sub list in the arr that represent sorted items
# and create a sub list in the arr that represent unsorted items
arr = [8, 5, 2, 9, 5, 6, 3]
# first find the smallest item by iterating over all items and comparing the smallest value

# space =  O(1)
# time  =  O(n^2) n is the length of input array


def selectionSort(array):
    for i in range(len(array) - 1):
        #  while i < length of array - 1
        min = i
        #  min set what ever i is in outer loop
        for runner in range(i + 1, len(array)):
            #  while runner is between i + 1, len(array)
            if array[min] > array[runner]:
                min = runner
        array[min], array[i] = array[i], array[min]
    return array
    # or
    # currIndex = 0  # the index of the first num in the sorted sub list array
    # while currIndex < len(array) - 1:  # while idx less than array length
    #     smallestIdx = currIndex
    #     # the loop will always start at the first index of the unsorted array
    #     for i in range(currIndex+1, len(array)):
    #         if array[i] < array[smallestIdx]:
    #             smallestIdx = i
    #     array[currIndex], array[smallestIdx] = array[smallestIdx], array[currIndex]
    #     currIndex += 1
    # return array

# print(selectionSort(arr))


def newSelectionSort(arr):
    i = 0
    while i < len(arr) - 1:
        min = i
        for runner in range(i + 1, len(arr)):
            if arr[min] > arr[runner]:
                min = runner
        arr[min], arr[i] = arr[i], arr[min]
        i += 1
    print(arr)


newSelectionSort(arr)
