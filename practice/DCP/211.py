"""
This problem was asked by Microsoft.
Given a string and a pattern, find the starting indices of all occurrences of the pattern in the string. For example, given the string "abracadabra" and the pattern "abr", you should return [0, 7].
"""


def findOccurenceIdx(string, pattern):
    occurences = []

    for i in range(len(string) - len(pattern) + 1):

        if string[i] == pattern[0]:

            windowStr = ''
            for j in range(i, i+len(pattern)):
                windowStr += string[j]

            if windowStr == pattern:
                occurences.append(i)

    return occurences


print("Occurences at: {}".format(findOccurenceIdx('abracadabra', 'abr')))
