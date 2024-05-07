words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]


def groupAnagrams(words):
    # empty dict this will contain key names of the sorted words
    anagrams = {}
    for word in words:
        # sort the word a-z and create a str from the sorted arr returned
        sortedWord = "".join(sorted(word))
        if sortedWord in anagrams:
            # if the word in anagrams then append the word to it
            anagrams[sortedWord].append(word)  # constant time
        else:
            # added the word as a list to the dict with key of sortedWord
            anagrams[sortedWord] = [word]
            # return a list of values from the dictionary
    return list(anagrams.values())


print(groupAnagrams(words))
