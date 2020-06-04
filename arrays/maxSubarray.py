def maxSubarray(arr):
    maxSum = arr[0]
    curSum = arr[0]
    for i in range(1, len(arr)):
        curSum = max(arr[i], curSum + arr[i])
        maxSum = max(curSum, maxSum)

    return maxSum


if __name__ == '__main__':
    print(maxSubarray([3, -3, -2, 4, -2, 4, -5, 8]))
