def coinChangeGreedy(denoms, value):
    coins = sorted(denoms)
    result = []
    for i in range(len(coins) - 1, -1, -1):

        while value >= coins[i]:
          result.append(coins[i])
          value -= coins[i]

    print(result)
    return len(result)


print(coinChangeGreedy([1, 2, 5, 10, 20, 50, 100, 500, 1000], 121))
print(coinChangeGreedy([9, 6, 5, 1], 11))