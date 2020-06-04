"""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
"""


def findWords(words):

    rows = ['qwertyuiopQWERTYUIOP', 'asdfghjklASDFGHJKL', 'zxcvbnmZXCVBNM']
    result = []
    for word in words:
        for row in rows:
            if set(word).issubset(row):
                result.append(word)

    return result


print(findWords(["Hello", "Alaska", "Dad", "Peace"]))
