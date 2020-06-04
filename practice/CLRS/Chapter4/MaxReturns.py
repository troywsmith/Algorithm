def recurse(arr, l, r):
    if l == r:
        return (0, arr[l], arr[r])

    m = l + (r - l) // 2

    left = recurse(arr, l, m)
    right = recurse(arr, m+1, r)

    maxProfit = max(left[0], right[0], right[2] - left[1])
    return (maxProfit, min(left[1], right[1]), max(left[2], right[2]))


def maxSubArraySum(arr):
    if len(arr) <= 1:
        return 0

    result = recurse(arr, 0, len(arr) - 1)
    return result[0]


print(maxSubArraySum([7, 1, 5, -3, 6, 4]))
