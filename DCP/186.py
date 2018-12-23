"""
This problem was asked by Microsoft.
Given an array of positive integers, divide the array into two subsets such that the difference between the sum of the subsets is as small as possible.
For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20}, which has a difference of 5, which is the smallest possible difference.
"""


def findMin(arr, n):
    return findMinRec(arr, n, 0, sum(arr))


def findMinRec(arr, i, sumCalculated, sumTotal):
    if i == 0:
        return abs((sumTotal-sumCalculated) - sumCalculated)

    return min(findMinRec(arr, i-1, sumCalculated+arr[i-1], sumTotal), findMinRec(arr, i-1, sumCalculated, sumTotal))


print(findMin([5, 10, 15, 20, 25], 5))
