class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                print('inserted here left: ', self.value, self.left.value)
                return
            BST.insert(self.left, value)
        else:
            if self.right is None:
                self.right = BST(value)
                print('inserted here right: ', self.value, self.right.value)
                return
            BST.insert(self.right, value)
        return self  # Do not edit the return statement of this method.

    def contains(self, value):
        stack = [self]
        while len(stack) > 0:
            current = stack.pop()
            if current.value == value:
                return True
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
        return False

    def remove(self, value):
        stack = [self]
        while len(stack) > 0:
            current = stack.pop()
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                stack.append(current.left)
            if current.left.value == value:
                print('found and removed: ', self.value, self.left.value)
                current.left = None
                break
            if current.right.value == value:
                print('found and removed: ', self.value, self.right.value)
                current.right = None
                break
        return self  # Do not edit the return statement of this method.


a = BST(20)  # |                       20
b = BST(14)  # |                    14       23
c = BST(23)  # |                 7  17        30
d = BST(7)  # |
e = BST(17)  # |
f = BST(30)  # |
a.left = b  # |                        a
a.right = c  # |                    b     c
b.left = d  # |                   d   e       f
b.right = e
c.right = f

###########################################################################
# write a bst constructor functions for insert, contains and remove nodes
# insert :
# print(BST.insert(a, 12))
# contains :
# print(BST.contains(a, 7))
# remove :
print(BST.remove(a, 17))
