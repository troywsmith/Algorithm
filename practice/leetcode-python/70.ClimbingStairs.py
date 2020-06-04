def climbStairs(n):
    memo = [0, 1, 2]

    def climber(m):
        if m >= len(memo):
            memo.append(climber(m-1) + climber(m-2))
        return memo[m]
    return climber(n)

print(climbStairs(4))