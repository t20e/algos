array = [34, 234, 45, 2, 345, 65, 78, 78, 23, 45]


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# print(insertion_sort(array))

# time : n^2
# space : 0(1)
def insertion_sort_two(arr):
    for i in range(1, len(arr)):
        value_to_sort = arr[i]
        while arr[i - 1] > value_to_sort and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    return arr


print(insertion_sort_two(array))
