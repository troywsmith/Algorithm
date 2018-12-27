"""
Name: Euclid's Algorithm
Description: find the greatest common divisor of two nonnegative integers
Input: two nonnegative integers
Output: greatest common divisor of the input
Time Complexity: O(lg b) if a>b>0
Space Complexity: O(1)
Algorithm Technique: Recursion
"""


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_extended(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = gcd_extended(b, a % b)
        d, x, y = d, y, x - int(a/b) * y
        return d, x, y
