"""
Name: Euclid's Algorithm
Description: find the least common multiple of two nonnegative integers
Input: two nonnegative integers
Output: least common multiple of the input
Time Complexity: O(lg b) if a>b>0
Space Complexity: O(1)
Algorithm Technique: Recursion
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)