"""
GET CHILD NODES
    we start from root node
    i is the index of 23 in the array
    index of 23 = 2
    get the left child use: 2*i + 1
    get the right child use: 2*i + 2
    left child:  2 *2+ 1 = arr[5] = 30
    right child: 2 *2+ 2 = arr[6] = 44

GET THE PARENT NODE OF A CHILD:
    i is the index of the child
    (i - 1)/2 round it down
    index of 30 = 5
    print(math.floor((5-1)/2))
# a node has to have a left child if it has a right child
"""


class MaxHeap:
    def __init__(self, arr):
        self.heap = arr
        self.buildHeap()

    def buildHeap(self):
        # get parent of last node
        for i in reversed(range(0, len(self.heap))):
            leftChildIdx = 2 * i + 1
            # call for when they have a valid child
            if leftChildIdx < len(self.heap) or 2 * i + 2 < len(self.heap):
                self.shiftDown(i, leftChildIdx)
        print(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, value):  # √
        self.heap.append(value)
        childIdx = self.heap[len(self.heap)-1]

    def shiftUp(self, currIdx):
        # TODO this should only move items up the heap
        leftChildIdx = 2 * currIdx + 1
        while currIdx != len(self.heap):
            rightChildIdx = 2 * currIdx + 2 if 2 * \
                currIdx + 2 < len(self.heap) else None
            if rightChildIdx is not None and self.heap[rightChildIdx] > self.heap[leftChildIdx] and self.heap[rightChildIdx] < self.heap[leftChildIdx] > self.heap[currIdx]:
                self.swap(rightChildIdx, currIdx)
                currIdx = rightChildIdx
            elif self.heap[leftChildIdx] > self.heap[currIdx]:
                self.swap(leftChildIdx, currIdx)
                currIdx = leftChildIdx
            else:
                break

    def shiftDown(self, currIdx, leftChildIdx):
        # TODO this should only move items down the heap
        while leftChildIdx < len(self.heap):
            # then if statement is to make sure the right child index is in array
            rightChildIdx = 2*currIdx + 2 if currIdx * \
                2 + 2 <= len(self.heap) - 1 else -1
            if rightChildIdx != -1 and self.heap[rightChildIdx] > self.heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if self.heap[idxToSwap] > self.heap[currIdx]:
                self.swap(currIdx, idxToSwap)
                currIdx = idxToSwap
                leftChildIdx = currIdx * 2 + 1
            else:
                break  # meaning we are done shifting

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.heap[0] = self.heap.pop()
        self.shiftUp(0)
        return self.heap

#                   3
#         2                 67
#      3     50         10       8
#   16

# sorted
#                   67
#         50                 10
#      16     2         3       8
#   3

#                   50
#         16                 10
#     9     2         3       8
#   3


array = [3, 2, 67, 3, 50, 10, 8, 16]
arrHeap = MaxHeap(array)
# [67, 50, 10, 16, 2, 3, 8, 3]
print('\ninsert', arrHeap.insert(76))
# [76,67,10,50,2,3,8,3,16]
print('\npeek', arrHeap.peek())
# 76
print('\nremove', arrHeap.remove())
# [67,50,10,16,2,3,8,3]
print('\npeek', arrHeap.peek())
#  67
print('\nremove', arrHeap.remove())
# [50,16,10,3,2,3,8]
print('\npeek', arrHeap.peek())
#  50
print('\ninsert', arrHeap.insert(9))
# [50,16,10,9,2,3,8,3]
