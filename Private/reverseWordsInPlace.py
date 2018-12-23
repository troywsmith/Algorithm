# inp = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'h', 'i']
# inp = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']
inp = ['p', 'e', 'r', 'f', 'e', 'c', 't', ' ', 'm', 'a', 'k',
       'e', 's', ' ', 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e']


def reverseWordsString(wordList):
    reverseWholeString(wordList)
    reverseWords(wordList)
    print(wordList)


def reverseWholeString(wordList):
    left = 0
    right = len(wordList) - 1
    while left < right:
        wordList[left], wordList[right] = wordList[right], wordList[left]
        left += 1
        right -= 1


def reverseWords(words):

    left = 0
    for x in range(len(words) - 1):

        # for all words except last
        if words[x + 1] == ' ':
            right = x
            while left < right:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1
            left = x + 2

        # For last word
        if x + 2 == len(words):
            right = x + 1
            while left < right:
                words[left], words[right] = words[right], words[left]
                left += 1
                right -= 1
            left = x + 2


reverseWordsString(inp)
