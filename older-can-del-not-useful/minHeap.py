#  a min heap is like a BST but has to have all of its levels filled up except for the first level
# !!! HOWEVER WE NEVER MAKE AN ACTUAL TREE ITS ONLY FOR VISUAL REPRESENTATION!!!
# from left to right
# EXAMPLE
#                              8
#                        12            23
#                    17     31     30      44
#                102   18
# a min heap states that every node values is going to be smaller than or equal
# to its children's node values
# vs a max heap is when a nodes children values are smaller than or equal to its value
# a heap is not sorted
# in a min heap the root node is the smallest in the heap


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
"""


# !!! THIS IS EXTRA FOR THE MAIN HEAP PY OUTSIDE THIS FOLDER IS MAIN !!!!
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
        i is the index of the child counting from 0 in the array
        (i - 2)/2 round it down
        index of 30 = 5
        print(math.floor((5-1)/2))
"""


class MinHeap:
    def __init__(self, arr):
        self.heap = arr
        self.buildHeap()

    def buildHeap(self):
        # t: O(N) n is the number of elements in the array, because we are calling shiftDown() or shiftUp() on N nodes in array to make it meet min heap standards
        # s: O(1) space because we are not allocating more space the array is already made
        for currIdx in reversed(range(0, len(self.heap))):
            # parentIdx = (currIdx - 1)//2
            leftChildIdx = 2 * currIdx + 1
            if leftChildIdx < len(self.heap):
                self.siftDown(currIdx)
        print(self.heap)
        return self.heap

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # this is made to only remove the root node
    def siftDown(self, parentIdx):
        # t: O(log(N)) n is the number of values in the array because we see the less of the array through every iteration
        # s: O(1)
        startIdx = parentIdx
        leftChildIdx = 2*startIdx + 1
        while leftChildIdx < len(self.heap) - 1:
            # then if statement is to make sure the right child index is in array
            rightChildIdx = 2*startIdx + 2 if startIdx * \
                2 + 2 <= len(self.heap) - 1 else -1
            if rightChildIdx != -1 and self.heap[rightChildIdx] < self.heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if self.heap[idxToSwap] < self.heap[startIdx]:
                self.swap(startIdx, idxToSwap)
                startIdx = idxToSwap
                leftChildIdx = startIdx * 2 + 1
            else:
                break  # meaning we are done shifting

    def siftUp(self, currIdx):
        # t: O(log(N)) n is the number of values in the array because we see the less of the array through every iteration
        # s: O(1)
        parentIdx = (currIdx - 2) // 2
        while self.heap[currIdx] < self.heap[parentIdx] and parentIdx >= 0:
            self.swap(currIdx, parentIdx)
            currIdx = parentIdx
            parentIdx = currIdx//2

    def peek(self):
        return self.heap[0]

    def remove(self):
        item_to_remove = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.siftDown(0)
        return item_to_remove

    # parentIdx = (len(self.heap) - 2)//2

    def insert(self, value):
        self.heap.append(value)
        currIdx = len(self.heap) - 1
        self.siftUp(currIdx)
        return self.heap

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


array = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
sortedArray = [2, 4, 6, 34, 6, 87, 10, 56]
"""
                    543
            4557         878
        32      56    78     45
        
                    32
            56              45
        4557      543    78     878


    """
# print(MinHeap(array))
arrHeap = MinHeap(array)
# [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41]
print('\ninsert',arrHeap.insert(76))
# [-5, 2, 6, 7, 8, 8, 24, 391, 24, 56, 12, 24, 48, 41, 76]
print('\npeek', arrHeap.peek())
#  -5
print('\nremove', arrHeap.remove())
# -5
print('\npeek', arrHeap.peek())
#  2
print('\nremove', arrHeap.remove())
# 2
print('\npeek', arrHeap.peek())
#  6
print('\ninsert',arrHeap.insert(87))
# [6, 7, 8, 24, 8, 24, 24, 391, 76, 56, 12, 41, 48, 87]
###
# arrHeap = MinHeap(sortedArray)
# print(arrHeap.insert(7))
# print(arrHeap.remove())

# !!! EXTRA !!!
""""
        build the heap as a tree out of an unsorted array in place
            arr = [30, 102, 23, 17, 18, 9, 44, 12, 31]
            we start by looking at the very last parent node which is 17 which we get by
            getting the last index of array 31 and calculated its parent node by math.floor((8-1)/2) 8 is the index of 31
            then we check to see if its less than both its children nodes 31 and 12
            since 17 > 12 we swap them
            arr = [30, 102, 23, 12, 18, 9, 44, 17, 31]
            then we go to second to last parent which is now 23 which is the index of 12 - 1 = 23
            then we compare 23 with its 2 child nodes
             left child:  2 *2+ 1 = arr[5] = 9
             right child: 2 *2+ 2 = arr[6] = 44
            then we take the smaller value of the 2: 9 < 44 | compare 9 and 23 then swap them because 9 < 23
            arr = [30, 102, 9, 12, 18, 23, 44, 17, 31]
            then we move to the next parent node which is current index of check which is 9 - 1 get 102
            compare 102 with its 2 child nodes
             left child:  2 *1+ 1 = arr[3] = 12
             right child: 2 *1+ 2 = arr[3] = 18
            12 < 18 | compare 12 < 102 | so we swap them
            arr = [30, 12, 9, 102, 18, 23, 44, 17, 31]
            then compare 102 with its child nodes
            17 < 31 | compare 17 < 102 | so we swap them
            arr = [30, 12, 9, 17, 18, 23, 44, 102, 31]
            then we call the shiftDown() on the last parent node which is the root and move 30 down
            arr = [9, 12, 30, 17, 18, 23, 44, 102, 31]
            then
            arr = [9, 12, 23, 17, 18, 30, 44, 102, 31]
            and we are done
    """

"""
        to remove a node for example 8
            arr = [8, 9, 23, 17, 12, 30, 44, 102, 18, 31]
            we swap 8 with the final value in the tree
            arr = [31, 9, 23, 17, 12, 30, 44, 102, 18, 8]
            remove the 8
            arr = [31, 9, 23, 17, 12, 30, 44, 102, 18]
            not we need to satisfy the min heap standards
            using the shiftDown() method which is the opposite of the shiftUp()
            take the value:31 that we swap with the value we remove:8 and shift it down to it correct position
            !!! when dealing with a min heap we always compare the its left child node first and move it in that direction!!!
            arr = [9, 31, 23, 17, 12, 30, 44, 102, 18]
            now 31 has child nodes of 17 and 12
            we compare 17 and 12 then compare 12 to 31 because 12 is less than 17
            arr = [9, 12, 23, 17, 31, 30, 44, 102, 18]
            then we compute the child nodes of 31 which returns an index that doesn't exist in the array and get
            no more child nodes so we are complete
    """

"""
        when we insert a new value, we add that new value at a leaf node,
            then we move it up to its correct position fo example if we had 9 then we make
            9 the child node of 31, then we correct the min heap by moving the 9 up using shiftUp()
            in array example
                arr = [8, 12, 23, 17, 31, 30, 44, 102, 18, 9]
                parent node of 9: math.floor((9(this is the index of 9 in the arr not the number) - 1)/2) = 4 index so 31 is 9's parent
                since 31 is > 9 we swap them
                arr = [8, 12, 23, 17, 9, 30, 44, 102, 18, 31]
            and we do the same thing again
                new parent node of 9: math.floor((4 - 1)/2) = 1 index so 12 is 9's new parent
                since 12 is > 9 we swap them
                arr = [8, 9, 23, 17, 12, 30, 44, 102, 18, 31]
    """
