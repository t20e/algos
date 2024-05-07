# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 10]
# # sequence = [1]
# array = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [22, 25, 6]
array = [5, 1, 22, 25, 6, -1, 8, 10],
sequence = [5, 1, 22, 25, 6, -1, 8, 10, 10]


def isValidSubSequence(array, sequence):
    if len(sequence) == 1 and sequence[0] in array:
        return True
    checkNum = 0
    for i in array:
        # print('sequence:',sequence[checkNum], 'array int:', i)
        # print(i)
        if i == sequence[checkNum]:
            checkNum += 1
            # print('equal to sequence')
        if checkNum == len(sequence):
            return True
        elif checkNum > len(sequence):
            return False
    return False


print(isValidSubSequence(array, sequence))
