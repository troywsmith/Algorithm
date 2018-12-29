"""
Name: Longest Increasing Subsequence
Description: find the length of the longest subsequence of a given sequence such that all elements of the subsequence are sorted in increasing order
Input: list of numbers
Output: length of the longest subsequence
Time Complexity: 
Space Complexity: 
Algorithm Technique: Dynamic Programming
"""


def LIS(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(n):
        for j in range(i):

            if arr[i] > arr[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
            
            print(dp)

    return dp[n-1]


# print('Longest Increasing Subsequence: ' + str(LIS([10, 22, 9, 33, 21, 50, 41, 60, 80])))
# print('Longest Increasing Subsequence: ' + str(LIS([3, 2])))
# print('Longest Increasing Subsequence: ' + str(LIS([50, 3, 10, 7])))
print('Longest Increasing Subsequence: ' + str(LIS([6, 2, 4, 3, 7, 4, 5])))