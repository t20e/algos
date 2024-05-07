arrays = [
    [1, 5, 9, 21],
    [-1, 0],
    [-124, 81, 121],
    [3, 6, 12, 20, 150],
    [-9, -6, 2, 5, 10]
]

# A FASTER SOLUTION WOULD BE TO USE A MIN HEAP LIKE EXAMPLE UNDER THIS BUT THAT ANSWER DOESN'T FULLY WORK


def mergeSortedArrays(arrays):
    # time: O(NK) | space: O(N+K)
    sortedList = []
    # sort the position for each array as we iterate
    indexes = [0] * len(arrays)
    #    this can also be written as indexes = [0 for array in arrays]
    while True:
        smallestItems = []
        for arrayIdx in range(len(arrays)):  # O(N)
            relevantArray = arrays[arrayIdx]
            index = indexes[arrayIdx]
            if index == len(relevantArray):
                # if the index in the indexes array thats tracking that particular sub array take your sub array
                # is == to the length of the sub array then we know that we have already seen
                # all elements of the sub array
                continue
            smallestItems.append(
                {"array_index": arrayIdx, "num": relevantArray[index]})
        if len(smallestItems) == 0:
            # meaning we have already went through all sub arrays
            break
        nextItem = getMinValue(smallestItems)
        sortedList.append(nextItem['num'])
        indexes[nextItem['array_index']] += 1  # move by one in the array
    return sortedList


def getMinValue(smallestItems):
    minValueIdx = 0
    for i in range(1, len(smallestItems)):
        if smallestItems[i]['num'] < smallestItems[minValueIdx]['num']:
            minValueIdx = i
    return smallestItems[minValueIdx]


print(mergeSortedArrays(arrays))

# class MinHeap():
#     def __init__(self, arr):
#         self.heap = arr
#         self.build_heap()

#     # O(N) time | O(1) space
#     def build_heap(self):
#         firstParentIdx = (len(self.heap) - 1)//2
#         for currIdx in reversed(range(firstParentIdx + 1)):
#             self.shiftDown(currIdx)

#     # O(log(N)) time | O(1) space
#     def shiftDown(self, currIdx):
#         leftChildIdx = currIdx * 2 + 1
#         while leftChildIdx <= len(self.heap) - 1:
#             rightChildIdx = currIdx * 2 + 2 if currIdx * \
#                 2 + 2 <= len(self.heap) - 1 else -1
#             if rightChildIdx != -1 and self.heap[rightChildIdx]['num'] < self.heap[rightChildIdx]['num']:
#                 idxToSwap = rightChildIdx
#             else:
#                 idxToSwap = leftChildIdx
#             if self.heap[idxToSwap]['num'] < self.heap[currIdx]['num']:
#                 self.swap(currIdx, idxToSwap)
#                 currIdx = idxToSwap
#                 leftChildIdx = currIdx * 2 + 1
#             else:
#                 # we are done sorting
#                 return

#     # O(log(N)) time | O(1) space
#     def shiftUp(self, currIdx):
#         parentIdx = (currIdx - 1)//2
#         while currIdx > 0 and self.heap[currIdx]['num'] < self.heap[parentIdx]['num']:
#             self.swap(currIdx, parentIdx)
#             currIdx = parentIdx
#             parentIdx = (currIdx - 1)//2

#     # O(1) time | O(1) space
#     def peek(self):
#         return self.heap[0]
#     # O(log(N)) time | O(1) space

#     def remove(self):
#         self.swap(0, len(self.heap) - 1)
#         value_to_remove = self.heap.pop()
#         self.shiftDown(0, len(self.heap) - 1)
#         return value_to_remove

#     def insert(self, value):
#         self.heap.append(value)
#         currIdx = len(self.heap) - 1
#         self.siftUp(currIdx)
#         # return self.heap

#     def swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def isEmpty(self):
#         # returns True is the heap is empty or False if not
#         return len(self.heap) == 0


# def mergeSortedArrays(arrays):
#     sortedList = []
#     smallestItems = []  # this is the heap
#     for arrIdx in range(len(arrays)):
#         smallestItems.append({
#             "arrIdx": arrIdx,
#             "elementIdx": 0,
#             "num": arrays[arrIdx][0]
#         })
#     heap = MinHeap(smallestItems)
#     while not heap.isEmpty():
#         smallestItem = MinHeap.remove()
#         arrIdx, elemIdx, num = smallestItem["arrIdx"], smallestItem["elementIdx"], smallestItem["num"]
#         sortedList.append(num)
#         if elemIdx == len(arrays[arrIdx]) - 1:
#             continue
#         heap.insert(
#             {'arrIdx': arrIdx, "elementIdx": elemIdx +
#              1, "num": arrays[arrIdx][elemIdx + 1]})
#     return sortedList


"""__best way to solve for best complexity__
        use a min heap to sort the array
        to get O(N log(K) + K) the puls k is for building the heap
        space:  O(N+K)
    """


"""__another way to solve it__
        all input arrays are sorted we need to combine them to create a single sorted array
        one way of doing this is comparing the first values of all arrays and keeps iterating comparing
        first come values
            time: O(N*K) k is the number of the 4 elements of each array we are comparing
            for every N'th iteration
            space:  O(N+K)
"""
