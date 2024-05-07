string = "abcdcaf"

# return the index of first non repeating character from the string
def firstNonRepeatingCharacter(string):
    # Write your code here.
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] = dic[i]+1
    for i in dic:
        if(dic[i] == 1):
            return string.index(i)
    return -1

print(firstNonRepeatingCharacter(string))