"""
    get the sum of sub arrays of length k
    sub arrays sum
    example [1,2,3,4,5,6]
    k = 3
    1 + 2 + 3 = 6 
    2+3+4 = 9
    3+4+5 = 12
    4+5+6 = 15
"""


def slidingWindow(arr, k):  # k is the maximum number of ints i can collect
    curr_subArray = sum(arr[:k])
    result = [curr_subArray]
    for i in range(1, len(arr) - k+1):
        curr_subArray - curr_subArray - arr[i-1]
        curr_subArray - curr_subArray + arr[i+k-1]
        result.append(curr_subArray)
    return result


array = [34, 15, 19, 12, 27, 53, 23, 4, 1, 10, 43]
print(slidingWindow(array, 5))
