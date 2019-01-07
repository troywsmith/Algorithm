from collections import defaultdict


def changeMaker(n):

    # Coin denominations we will be using
    coins = [25, 10, 5, 1]

    # Create a nested dictionary
    ways_map = defaultdict(lambda: defaultdict(int))
    ways = getWays(n, coins, 0, ways_map)
    return ways


def getWays(amount, coins, coinIndex, ways_map):

    # If result has already been computed, return it
    if ways_map[amount][coinIndex] > 0:
        return ways_map[amount][coinIndex]

    # Base Case: if its the last coin (1)
    if coinIndex >= len(coins) - 1:
        return 1

    # Get Current Coin
    coin = coins[coinIndex]

    # Init ways to 0
    ways = 0

    # Way of adding coin until as many times as possible until it exceeds desired amount
    i = 0
    while i * coin <= amount:
        amount_remaining = amount - i * coin

        # Get ways for the amount remaining with the other coins
        ways += getWays(amount_remaining, coins, coinIndex + 1, ways_map)

        # Add coin again
        i += 1

    # Store current coin and amount results for future lookup
    ways_map[coinIndex][amount] = ways
    return ways


if __name__ == '__main__':
    n = 6
    ways = changeMaker(n)
    print('{} can be made {} different ways.'.format(n, ways))
    
else:
    print('Importing: Coin Change Algorithm')