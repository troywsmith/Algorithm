# # get amount of possible combos for n
# def getCombos(amt, coins):
#     combos = [0 for x in range(amt + 1)]
#     combos[0] = 1

#     for coin in coins:
#         for x in range(coin, len(combos)):
#             combos[x] += combos[x - coin]

#     return combos[amt]

# get min coins to make n
def getMinCoins(amt, coins):
    dp = [float('inf')]



# print(getCombos(12, [1, 2, 5]))
print(getMinCoins(12, [1, 2, 5]))
