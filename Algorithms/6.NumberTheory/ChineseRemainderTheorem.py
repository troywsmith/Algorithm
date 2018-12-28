"""
Name: Chinese Remainder Theorem
Description: find the minimum positive number that produces given remainders
Input: numbers array and remainders array
Output: minimum positive number that produces given remainders
Time Complexity: 
Space Complexity: 
Algorithm Technique: 
"""

# # Naive Implementation
# def findMinX(nums, rem):
#     x = 1
#     while True:
#         match = True
#         for y in range(len(nums)):
#             if x % nums[y] != rem[y]:
#                 match = False
#                 break
#         if match:
#             return x
#         else:
#             x += 1


# Inverse Modulo Implementation
def inv(a, m):
    m0 = m
    x0 = 0
    x1 = 1

    if (m == 1):
        return 0

    # Apply extended Euclid Algorithm
    while (a > 1):
        # q is quotient
        q = a // m

        t = m

        # m is remainder now, process same as euclid's algo
        m = a % m
        a = t

        t = x0

        x0 = x1 - q * x0

        x1 = t

    # Make x1 positive
    if (x1 < 0):
        x1 = x1 + m0

    return x1

def findMinX(nums, rem):

    prod = 1
    for num in nums:
        prod *= num

    result = 0
    for i in range(len(nums)):
        pp = prod // nums[i]
        result = result + (rem[i] * pp * inv(pp, nums[i]))

    return result % prod


print('x is ' + str(findMinX([3, 4, 5], [2, 3, 1])))
print('x is ' + str(findMinX([9, 8, 7], [1, 2, 3])))