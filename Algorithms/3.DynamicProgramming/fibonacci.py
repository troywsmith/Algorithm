# # Recursion
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


# DP
# def fib(n):
#     dp = [x for x in range(n+1)]

#     for x in range(2, n+1):
#         dp[x] = dp[x-1] + dp[x-2]

#     return dp[n]

# DP (Optimized)
def fib(n):
    if n <= 1:
        return n

    a = 0
    b = 1
    for _ in range(2, n):
        c = a + b
        a = b
        b = c

    return a + b


print(fib(8))