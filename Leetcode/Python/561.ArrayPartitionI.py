"""
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
"""


def arrayPairSum(nums):
    return sum(sorted(nums)[::2])


print(arrayPairSum([1, 2, 3, 4, 5, 6]))