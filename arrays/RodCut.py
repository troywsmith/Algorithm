def cutRod(prices, n):

    dp = [0 for x in range(n+1)]

    for x in range(1, n+1):
        currMax = 0

        for y in range(x):
            currMax = max(currMax, prices[y] + dp[x-y-1])

        dp[x] = currMax

    return dp[n]



#########################################################
prices = [1, 5, 8, 9, 10]
n = len(prices)
print('Max Revenue: ' + str(cutRod(prices, n)))


#########################################################
# Time Complexity: O(n^2)
