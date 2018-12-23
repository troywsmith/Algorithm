# def uglyNums(n):

#     uglyNums = [1]

#     i = 2
#     while len(uglyNums) < n:
#         if isUgly(i):
#             uglyNums.append(i)
#         i += 1

#     print(uglyNums)
#     return uglyNums[n-1]


# def isUgly(n):
#     for num in [2, 3, 5]:
#         while n % num == 0:
#             n = n / num
#     if n == 1:
#         return True
#     else:
#         return False

def getNthUglyNo(n):
    dp = [0] * n
    dp[0] = 1

    i2, i3, i5 = 0, 0, 0
    next2, next3, next5 = 2, 3, 5

    for i in range(1,n):
      dp[i] = min(next2, next3, next5)

      if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2

      if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3

      if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

    return dp[n-1]


print(getNthUglyNo(150))
