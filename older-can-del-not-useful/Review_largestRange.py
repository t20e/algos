# //  Write a function that takes in an array of integers and returns an array of
# //  length 2 representing the largest range of integers contained in that array.
# //   The first number in the output array should be the first number in the range,
# //   while the second number should be the last number in the range.
# //   A range of numbers is defined as a set of numbers that come right after each
# //   other in the set of real integers. For instance, the output array
# //   <span>[2, 6]</span> represents the range <span>{2, 3, 4, 5, 6}</span>, which
# //   is a range of length 5. Note that numbers don't need to be sorted or adjacent
# //   in the input array in order to form a range.
# // let array = [1,11,3,0,15,5,2,4,10,7,12,6]
# // const getLongestRange= (array)=>{
# //     let possibleRanges = []
# //     let checkRange = []
# //     for(var i = 0; i < array.length; i++){
# //     }
# // }
# // getLongestRange(array)
#     // sort array
#     // for(var i = 0; i < array.length; i++){
#     //     for(let runner = 0; runner< array.length; runner++){
#     //         if(array[runner] > array[i]){
#     //             let holder = array[i];
#     //             array[i] = array[runner]
#     //             array[runner] = holder
#     //         }
#     //     }
#     // }
# array = [1,11,3,0,15,5,2,4,10,7,12,6]
array = [8, 4, 2, 10, 3, 6, 7, 9, 1]

def largestRange(array):
    bestRange = []
    longestLen = 0
    nums = {}
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            # if the value is false in our hash table then continue
            continue
        nums[num] = False
        currentLen = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLen += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLen += 1
            right += 1
        if currentLen > longestLen:
            longestLen = currentLen
            bestRange = [left+1, right -1]
    return bestRange

print(largestRange(array))