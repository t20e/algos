# 0(nlog) time | 0(1) space 

def nonConstructibleChange(coins):
    coins.sort()
    currCHangeCreated = 0
    for coin in coins:
        if coin > currCHangeCreated + 1:
            return currCHangeCreated + 1
        currCHangeCreated += coin
    return currCHangeCreated + 1

coins = [5,7,1,1,2,3,22]
nonConstructibleChange(coins)

# return the smallest amount of change that you can NOT create
# with the available coins 