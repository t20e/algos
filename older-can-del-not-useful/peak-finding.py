arr = [100, 132, 4, 3,  6, 5, 78, 45, 32, 7, 6,  89]
# peaks are it is >= the index to its left and <= the index to its right


def peak(idx=1, len=len(arr) - 1):
    # for idx, i in enumerate(arr):
    #     # if i >= arr[idx - 1] and i <= arr[idx + 1]:
    #     #     return i
    #     # return -1
    #     print('here', arr[idx - 1], 'idx', idx)
    if idx == len:
        return - 1
    if arr[idx] >= arr[idx - 1] and arr[idx] <= arr[idx + 1]:
        print('left',  arr[idx - 1], 'right', arr[idx + 1])
        return arr[idx]
    return peak(idx + 1, len)

print(peak())
