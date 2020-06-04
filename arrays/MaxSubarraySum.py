"""
Name: Kadane's Algorithm
Description: find the maximum subarray sum of a list of numbers
Input: list of numbers
Output: max subarray sum
Time Complexity: O(n)
Space Complexity: O(1)
Algorithm Technique: Dynamic Programming
"""


def MSS(nums):

    maxSum = nums[0]

    for x in range(1, len(nums)):

        currSum = maxSum + nums[x]
        maxSum = max(maxSum, currSum)

    return maxSum


print('Max Subarray Sum: ' + str(MSS([1, -2, 3, -3, 4, -4, -5, 3, 2, 4])))