# a stack is a list of things stacked on each other
# u can only pick from the top first
# we can also access the min and max values of the stack at any given time time:O(1)

# Feel free to add new properties and methods to the class.
# time: O(1)
# space: O(1)
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minMax = []  # {min:,max:}

    def peek(self):  # the top value
        return self.stack[len(self.stack) - 1]

    def pop(self):  # remove the top value
        self.minMax.pop()
        return self.stack.pop()

    def push(self, number):  # push to the top
        newMinMax = {'min': number, 'max': number}
        if len(self.minMax):
            # means its not empty
            lastMinMax = self.minMax[len(self.minMax)-1]
            newMinMax['min'] = min(lastMinMax['min'], number)
            newMinMax['max'] = max(lastMinMax['max'], number)
        self.minMax.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMax[len(self.minMax) - 1]['min']

    def getMax(self):
        return self.minMax[len(self.minMax) - 1]['max']


arr = [3, 5, -2, 3, 5, 7, 8]
instance = MinMaxStack()
for num in arr:
    instance.push(num)
print(instance.getMax())
print(instance.getMin())
print(instance.peek())
print(instance.pop())
print(instance.peek())
