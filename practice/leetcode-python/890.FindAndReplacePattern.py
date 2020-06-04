def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """

    def hash_function(pattern):
        n = len(pattern)
        d = dict()
        for i in range(n):
            if pattern[i] not in d:
                d[pattern[i]] = i+1

        res = 0
        for i in range(n):
            res += d[pattern[i]]*10**(n-1-i)
        return res

    result = []
    for word in words: 
      if hash_function(word) == hash_function(pattern):
        result.append(word)

    return result


words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

print(findAndReplacePattern(words, pattern))
