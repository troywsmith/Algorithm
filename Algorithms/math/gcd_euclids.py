"""
Name: Euclid's Algorithm
Description: find the greatest common divisor of two nonnegative integers
Input: two nonnegative integers
Output: greatest common divisor of the input
Time Complexity: O(lg b) if a>b>0
Space Complexity: O(1)
Algorithm Technique: Recursion
"""


def euclid(a, b):
    if b == 0:
        return a
    else:
        return euclid(b, a % b)


def euclid_extended(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        d, x, y = euclid_extended(b, a % b)
        d, x, y = d, y, x - int(a/b) * y
        return d, x, y


print(euclid(15, 20))
print(euclid_extended(15, 20))
print(euclid_extended(100, 56))