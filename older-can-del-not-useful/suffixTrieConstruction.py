# A trie is a data structure that is a tree its often used to store characters, and we can check for words
#  the symbol * indicates that it is a complete word

#  this tree is used for things like spell checking, words look up, etc... its very useful!


class Trie:
    def __init__(self, string):
        self.root = {}  # points to dictionary/ hash-table/ hashmap
        self.endSymbol = "*"
        self.insert(string)

    def insert(self, string):
        # creation
        #   time:  O(n^2) n is the length of the input string
        #   space: O(n^2)  n is the length of the input string
        for i in range(len(string)):
            self.insertAt(i, string)

    def insertAt(self, idx, string):
        node = self.root
        for j in range(idx, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    def contains(self, string):
        # searching:
        #     time: O(M) m is the length of the input string
        #     space:0(1)
        node = self.root
        for char in string:
            if char not in node:
                return False
            print(node)
            node = node[char]
        return self.endSymbol in node


print(Trie.contains(Trie('here'), 'htere'))
