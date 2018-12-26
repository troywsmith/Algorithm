# # Recursion
# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)


## DP
def fib(n):
  dp = [x for x in range(n+1)]

  for x in range(2, n+1):
    dp[x] = dp[x-1] + dp[x-2]

  return dp[n]

print(fib(35))