"""
    sort a stack in place, you are only allowed to pop items from the end and
    append items to the end, the solution must be recursive
"""


def sortStack(stack):
    # time O(n^2)
    # space O(N)
    # return if empty
    if len(stack) == 0:
        return stack
    # then loop through the stack and remove the top element to sort it
    top = stack.pop()
    # call the function to remove tops which is the last value in stack
    sortStack(stack)
    # call function to insert the top this will run in last in first server order
    # so that the last call stack runs sorts first
    insert(stack, top)
    return stack


def insert(stack, value):
    # if we are at the base case or stack is fully empty then append
    if len(stack) == 0 or stack[len(stack)-1] <= value:
        stack.append(value)
        return
    # else if the new value is < the top value of the stack pop that element off
    top = stack.pop()
    # call insert with the top value removed and the same value to be added
    insert(stack, value)
    # then after thats done readd the top value
    stack.append(top)
    # this will loop until all call stacks are done and stack is sorted


stack = [-5, 2, 34, -2, -4, 56, 4, -23, 45, -3, 45, 1]
print(sortStack(stack))
