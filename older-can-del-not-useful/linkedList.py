# A LINKED LIST CONTAINS MANY NODES THAT ARE LINKED TOGETHER WITH POINTS
# LINKED LIST IS ORDERED AND ITS HAS INDEX FROM THE FIRST NODE IS 0 AND SO ON
# A NODE IS A CONTAINER FOR DATA
# LAST NODE POINTS TO NULL
# THE START NODE IS CALLED THE HEAD # THE LAST NODE IS CALLED THE TAIL
# TIP interactive solutions save more space and memory usage

# LINKED LIST VS ARRAY
# |   AN ARRAY MUST BE STORED CONTINUOUSLY IN MEMORY WHICH MAKES IT SLOWER
# |      ex: to insert into an array when need to find where we want to insert and push all the elements
#        after it by one index over o(n)
# |   WHILE A LINKED LIST CAN EXIST ANYWHERE IN THE COMPUTERS MEMORY NOT CONTINUOUSLY IN MEMORY
# |      ex to insert we just create a new node find where we want to insert and adjust the points so that
#        we wont have to move all the nodes like an array 0(1)

# current and current.next are current and the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def iterateList(head):
        # |   INTERACTIVELY ITERATE
        # current = self
        # while current is not None:
        #     print(current.value, ' => ')
        #     current = current.next
        # |   RECURSIVELY ITERATE
        if head is None:
            return
        print(head.value, ' => ')
        Node.iterateList(head.next)

    def linkedListValues(head):
        # interactive
        #     values = []
        #     current = head
        #     while current is not None:
        #         values.append(current.value)
        #         current = current.next
        #     return values
        # recursive
        # TIP: a recursive with a helper function like this one save space by not creating multiple array for every recursive call just one
        values = []
        Node.fillValues(head, values)
        return values

    def fillValues(head, values):
        if head is None:
            return
        values.append(head.value)
        Node.fillValues(head.next, values)

    def nodesSum(head):
        # interactive
        # sum = 0
        # current = head
        # while current is not None:
        #     sum += current.value
        #     current = current.next
        # return sum
        # RECURSIVE
        if head is None:
            return 0
        return head.value + Node.nodesSum(head.next)
        # vs other one which is more lines
        # sum = head.value
        # sum += Node.nodesSum(head.next)
        # return sum

    def findTarget(head, value):
        # interactive
        # current = head
        # while current is not None:
        #     if current.value == value:
        #         return True
        #     current = current.next
        # return False
        # RECURSIVE
        if head is None:
            return False
        if head.value == value:
            return True
        return Node.findTarget(head.next, value)

    def getNodeValueAtIndex(head, index):
        # interactive
        # count = 0
        # current = head
        # while current is not None:
        #     if count == index:
        #         return current.value
        #     count += 1
        #     current = current.next
        # return None
        # RECURSIVE
        if head is None:
            return None
        if index == 0:
            return head.value
        return Node.getNodeValueAtIndex(head.next, index - 1)

    def reverseList(head, prev=None):
        #
        # iterative remove above prev
        # current = head
        # prev = None
        # while current is not None:
        #     next = current.next
        #     current.next = prev
        #     prev = current
        #     current = next
        # return('new head', prev.value)  # prev contains the new head we
        # RECURSIVE
        if head is None:
            return 'new head:', prev.value
        next = head.next
        head.next = prev
        return Node.reverseList(next, head)

    def zipperLists(head1, head2):
        # time and space complexity
        # n = length of list 1
        # n = length of list 2
        # time = o(min(n,m))
        # space o(1)
        # interactive solution
        # tail = head1
        # current1 = head1.next
        # current2 = head2
        # count = 0
        # while current1 is not None and current2 is not None:
        #     # we take from one list or the other based on if the count is a negative or positive number
        #     if count % 2 == 0:
        #         tail.next = current2
        #         current2 = current2.next
        #     else:
        #         tail.next = current1
        #         current1 = current1.next
        #     tail = tail.next
        #     count += 1
        # if current1 is not None:
        #     tail.next = current1
        # if current2 is not None:
        #     tail.next = current2
        # return head1

        # recursive solution
        if head1 is None and head2 is None:
            # if both are empty
            return None
        if head1 is None:
            # if one of the lists is empty after looping through all its nodes tag the rest of
            # the nodes in the other list to the end of it
            # and vice versa for the below if statement
            return head2
        if head2 is None:
            return head1
        next1 = head1.next
        next2 = head2.next
        head1.next = head2
        head2.next = next1
        # because all the calls will return head1 we want to only return the head1 from the fist call
        # we dont want to replace it on the return so we set the value to head2 upon head1 return
        # from the inner call stacks
        head2 = Node.zipperLists(next1, next2)
        return head1.value

    def removeDuplicates(head):
        if head is None:
            return
        current = head
        prev = Node(None)
        while current is not None:
            next = current.next
            if current.value == prev.value:
                # we have duplicates values remove current
                prev.next = current.next
                current = None
            else:
                prev = current
            current = next


# a = Node('A')
# b = Node('B')
# c = Node('C')
# d = Node('D')
# e = Node('E')
# f = Node('F')
# g = Node('G')
# h = Node('H')
# numbers nodes
a = Node(2)
b = Node(3)
c = Node(5)
d = Node(5)
e = Node(6)
f = Node(9)
g = Node(12)
h = Node(12)
i = Node(7)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = None


# A => B => C => D => E => F => G => H => NULL

# LIST TWO ONLY NEEDED FOR ALGOS THAT NEED TWO LINKED LISTS
# q = Node('Q')
# r = Node('Q')
# q.next = r
# r.next = None

########################################################################
# iterate and print values
# a.iterateList()
# Node.iterateList(a)
########################################################################
# add node values to array
print(Node.linkedListValues(a))
########################################################################
# get the sum of all the values of all nodes
# print(Node.nodesSum(a))
#######################################################################
# find a value in the list
# print(Node.findTarget(a, 7))
#######################################################################
# find value at an index of the linked list
# ex index 2 above should return 5 because a index is 0 and b is 1 and c is 2
# print(Node.getNodeValueAtIndex(a, 2))
#######################################################################
# time : o(n)
# space : o(n)
# reverse the list and return the new head
# print('before', Node.iterateList(a))
# print(Node.reverseList(a))
# print('after', Node.iterateList(g))

#######################################################################
# zipper list
# list one : a -> b -> c
# list two : q -> r -> s
# equals : a -> q -> b -> r -> c -> s
# take two linked list and reassign (merge them)
# print(Node.zipperLists(a, q))

#######################################################################
# remove duplicates values from a ordered linked list, this needs the duplicates
#  values nodes from creating above
# Node.iterateList(a)
# print('before')
# Node.removeDuplicates(a)
# Node.iterateList(a)
# print('after')
