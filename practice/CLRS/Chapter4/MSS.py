def maxCrossingSum(arr):
    mid = len(arr) // 2
    left = arr[:mid][::-1]
    right = arr[mid:]

    sum, left_sum = 0, float('-inf')
    for x in left:
        sum += x
        if sum > left_sum: left_sum = sum

    sum, right_sum = 0, float('-inf')
    for x in right:
        sum += x
        if sum > right_sum: right_sum = sum

    return left_sum + right_sum


def maxSubArraySum(arr):

    if len(arr) == 1: return arr[0]

    mid = len(arr) // 2
    return max(
        maxSubArraySum(arr[:mid]),
        maxSubArraySum(arr[mid:]),
        maxCrossingSum(arr)
    )


print(maxSubArraySum([1, 4, 2, -235, 6, 2, 5, 325]))
