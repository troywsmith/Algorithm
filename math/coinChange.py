def coinChangeAllCombos(coins, amount):
    dp = [[] for _ in range(amount+1)]
    dp[0] = []
    dp[1] = [[1]]

    for x in range(2, amount+1):
        currentWays = []
        for combo in dp[x-1]:
            for denom in coins:
                if sum(combo) + denom == x:
                    combo.append(denom)
                    currentWays.append(combo)
        for denom in coins[:-1]:
            if x % denom == 0:
                repeats = x // denom
                combo = [denom for _ in range(repeats)]
                currentWays.append(combo)
        dp[x] = currentWays

    return dp[amount]


def coinChangeNumCombos(coins, amount):
    combos = [0 for _ in range(amount+1)]
    combos[0] = 1
    for coin in coins:
        for x in range(1, len(combos)):
            if x >= coin:
                combos[x] += combos[x - coin]
        #         print(combos)
        # print()
    return combos[amount]


if __name__ == '__main__':
    coins = [1, 5, 10, 25]
    amount = 10
    allCombos = coinChangeAllCombos(coins, amount)
    numWays = coinChangeNumCombos(coins, amount)
    print('Combos:')
    for combo in allCombos:
        print(combo)
    print('Result: {} ways to make {}'.format(numWays, amount))
