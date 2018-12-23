def maxSum(arr):
    max_sm = 0
    curr_sm = 0

    for x in range(len(arr)):
        curr_sm += arr[x]

        if curr_sm < 0:
            curr_sm = 0

        if curr_sm > max_sm:
            max_sm = curr_sm

    return max_sm


print(maxSum([-2, -3, 4, -1, -2, 1, 5, -3]))
