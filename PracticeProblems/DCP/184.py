"""
This problem was asked by Amazon.
Given n numbers, find the greatest common denominator between them.
For example, given the numbers [42, 56, 14], return 14.
"""


def findGCD(n):
    for x in range(min(n), 0, -1):
        denoms = []

        for num in n:
            if num % x == 0:
                denoms.append(num)

        if len(denoms) == len(n):
            return x


print(findGCD([40, 56, 14]))