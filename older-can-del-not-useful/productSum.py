# given a special array find the product sum
# special arrays can contain numbers and other nested arrays
# for nested arrays we sum up the numbers inside that multiple that total
# by the depth which that array is inside the other array example below


array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]  # should return 12
# the outer array gets multiplied by 1
#  the array of [7,-1]
# does this 7 - 1 = 6 then we multiply by 2 because thats its depth in the original
#  array is
# 12 is the value of the array

# recursive
# time = O(n) n is the total number of elements(integers) including all
# the integers inside nested for loops
# space = 0(d) d is the depth of all the sub (nested) arrays in the input array
# space here is mostly because we are using recursion to make call stacks for
# each nested array


def productSum(array, multiplier=1):
    sum = 0
    for item in array:
        if type(item) is list:
            sum += productSum(item, multiplier + 1)
        else:
            sum += item
    return sum * multiplier


print(productSum(array))
