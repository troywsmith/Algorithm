# Brute Force Solution O(n^2)
# def maxSubarray(prices):
#     if prices == []:
#         return 0
#     maxProfit = -float('inf')
#     for x in range(0, len(prices)):
#         for y in range(x+1, len(prices)):
#             if prices[x] < prices[y]:
#                 profit = prices[y] - prices[x]
#                 if profit > maxProfit:
#                     maxProfit = profit
#     return maxProfit
# print(maxSubarray(A))

# Solution 2: O(n)
# def maxSubarrayProfit(prices):
#     minPrice = float('inf')
#     maxProfit = 0

#     for i in range(len(prices)):
#         if prices[i] < minPrice:
#             minPrice = prices[i]
#         elif prices[i] - minPrice > maxProfit:
#             maxProfit = prices[i] - minPrice

#     return maxProfit


def maxCrossingSum(arr, l, m, h):

    # Get left sum
    sm = 0
    left_sm = -1000
    for i in range(m, l-1, -1):
        sm += arr[i]
        if sm > left_sm:
            left_sm = sm

    # Get right sm
    sm = 0
    right_sm = -1000
    for i in range(m+1, h+1):
        sm += arr[i]
        if sm > right_sm:
            right_sm = sm

    return left_sm + right_sm


def maxSubArraySum(arr, l, h):

    if h < 1:
        return 0

    # Base Case
    if (l == h):
        return arr[l]

    m = (l + h) // 2

    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))


arr = []
n = len(arr)

print(maxSubArraySum(arr, 0, n-1))
