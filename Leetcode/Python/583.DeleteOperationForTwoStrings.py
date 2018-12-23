def minDistance(word1, word2):
    # subwords = []

    # for x in range(len(word1)):
    #     if word1[x] in word2:
    #         subword = word1[x]
    #         for y in range(x, len(word1)):
    #             if subword + word1[y] in word2:
    #                 subword += word1[y]
    #         subwords.append(subword)

    # goal_word = ''

    # for word in subwords:
    #     if len(word) > len(goal_word):
    #         goal_word = word
    # print(goal_word)

    # reword1 = word1.replace(goal_word, '')
    # reword2 = word2.replace(goal_word, '')

    # return len(reword1) + len(reword2)
    m = len(word1)
    n = len(word2)

    dp = [[0] * (n + 1) for i in range(m + 1)]
    print(dp)
    
    for i in range(m):
        for j in range(n):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))

    return m + n - 2 * dp[m][n]


# print(minDistance('sea', 'eat'))
# print(minDistance('mart', 'karma'))
print(minDistance('park', 'spake'))
