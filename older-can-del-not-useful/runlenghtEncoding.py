str = 'AAAAAAAAAAAAABBCCCCDD'

# 9A4A2B4C2D
def runLengthEncoding(str):
    l = 0
    res = ""
    while l < len(str):
        print(l)
        r = l + 1
        count = 1
        while count < 9 and r < len(str) and  str[r] == str[l] :
            count += 1
            r += 1
        res += f'{count}{str[l]}'
        l = r
    return res


print(runLengthEncoding(str))
