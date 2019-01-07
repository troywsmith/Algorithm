"""
This problem was asked by Amazon.
Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
Do this in O(N) time.
"""


def findSmallestInteger(arr):

    if arr[0] > 1:
        return 1

    sm = 1

    for i in range(len(arr)):

        if arr[i] <= sm:
            sm += arr[i]
        else:
            break

    return sm


arr = [1, 2, 3, 10]
ans = findSmallestInteger(arr)
print(ans)
