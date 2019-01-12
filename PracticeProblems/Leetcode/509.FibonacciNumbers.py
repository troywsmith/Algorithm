def fib(N):
    """
    :type N: int
    :rtype: int
    """
    dp = [None for _ in range(N+1)]
    dp[0] = 0
    dp[1] = 1

    for x in range(2, N+1):
        dp[x] = dp[x-1] + dp[x-2]
    return dp[N]


print(fib(3))
