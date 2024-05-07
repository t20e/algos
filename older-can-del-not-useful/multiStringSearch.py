# multi string search
# find if the list of strings are in the bigStr
# return boolean value in the arrStr if they are in the bigStr or not

bigString = "this is a big string"
smallStrings = ["this", "yo", "i", "a", "bigger", "string", "kappa"]


class Trie:
    def __init__(self, char):
        self.children = {}
        self.endOfWord = False
        self.value = char

    def addBigStrToTree(self, bigString):
        words = bigString.split(" ")
        curr = None
        for word in words:
            curr = self  # set current to self
            for c in word:  # for each character in word
                if c not in curr.children:
                    curr.children[c] = Trie(c)
                curr = curr.children[c]
        curr.endOfWord = True

    def loop(self):  # testing if the children are correctly placed
        for c in self.children:
            # print(self.children[c].value)
            for i in self.children[c].children:
                # print(i)
                for t in self.children[c].children[i].children:
                    # print(t)
                    for k in self.children[c].children[i].children[t].children:
                        # print(k)
                        for l in self.children[c].children[i].children[t].children[k].children:
                            print(l)
                            for p in self.children[c].children[i].children[t].children[k].children[l].children:
                                print(p)


def multiStringSearch(bigString, smallStrings):
    root = Trie(' ')
    root.addBigStrToTree(bigString)
    count = 0
    for word in smallStrings:
        for c in word:
            if c not in root.children:
                smallStrings[count] = False
                break
            root = root.children[c]
            count += 1
    return smallStrings
    # for word in smallStrings:
    #     check = True
    #     for c in word:
    #         if c not in root.children:
    #             check = False
    #             break
    #         root = root.children[c]
    #         print(check)
    #     smallStrings[count] = check
    #     count += 1
    # return smallStrings


print(multiStringSearch(bigString, smallStrings))
