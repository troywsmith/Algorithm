import math


def minEatingSpeed(piles, H):
    bananas = sum(piles)
    K = math.ceil(bananas / H) - 1

    minHours = H + 1

    while minHours > H:
        minHours = 0
        K += 1
        for pile in piles:
            minHours += pile // K + math.ceil((pile % K) / K)

    return K


# print(minEatingSpeed([3,6,7,11], 8))
print(minEatingSpeed([30, 11, 23, 4, 20], 5))
# print(minEatingSpeed([30,11,23,4,20], 6))
# print(minEatingSpeed([332484035, 524908576, 855865114, 632922376, 222257295, 690155293, 112677673, 679580077, 337406589,
#                       290818316, 877337160, 901728858, 679284947, 688210097, 692137887, 718203285, 629455728, 941802184], 823855818))
