"""
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
"""


def checkPossibility(nums):
    p = None
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            if p is not None:
                return False
            p = i

    result = (p is None or p == 0 or p == len(nums)-2 or nums[p-1] <= nums[p+1] or nums[p] <= nums[p+2])
    return result


print(checkPossibility([1, 1, 1]))
