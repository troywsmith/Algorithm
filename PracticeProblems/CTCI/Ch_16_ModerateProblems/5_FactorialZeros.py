"""
Write an algorithm which computes the number of trailing zeros in n factorial
"""


# def count_zeros(n):

#     count = 0
#     for x in range(2, n+1):
#         while x % 5 == 0:
#             count += 1
#             x /= 5
#     return count

def count_zeros(n):
    count = 0
    x = 5
    while n / x > 0:
        print(n, x)
        count += n / x
        x *= 5
    return count

n = 100
zeros = count_zeros(n)
print('{} has {} trailing zero(s)'.format(n, zeros))
