words = ["dog", "hello", "god"]
# time O(N^2)
# space = O(N^2)


def semordnilap(words):
    wordSet = set(words)
    pairs = []
    for word in words:
        reverse = word[::-1] #O(N)
        if reverse in wordSet and reverse != word:
            pairs.append([word, reverse])
            wordSet.remove(word)
            wordSet.remove(reverse)
    return pairs


print(semordnilap(words))
