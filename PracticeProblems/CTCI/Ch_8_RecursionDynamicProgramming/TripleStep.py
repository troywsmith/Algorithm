# def countWays(n):
#     """
#     Time Complexity: O(n)
#     """
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1

#     memo = [0 for x in range(n+1)]
#     memo[0] = 1
#     memo[1] = 1
#     memo[2] = 2

#     for x in range(3, n+1):

#         memo[x] = memo[x-1] + memo[x-2] + memo[x-3]

#     return memo[n]


def countWays(n):
    """
    Time Complexity: O(n)
    """
    if n < 0:
        return 0
    if n == 0:
        return 1

    a, b, c = 1, 1, 2
    for _ in range(3, n):
        d = a + b + c
        a, b, c = b, c, d

    return a + b + c


if __name__ == '__main__':
    print(countWays(5))


else:
    print('Importing: Triple Step Algorithm')
