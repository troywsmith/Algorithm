def LCS(s1, s2):
  m = len(s1)
  n = len(s2)
  dp = [[0 for x in range(n+1)] for x in range(m+1)]

  for i in range(1, m+1):
    for j in range(1, n+1):

      if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1
      
      else:
        dp[i][j] = max(dp[i][j-1], dp[i-1][j])

  return dp[m][n]

# print('LCS: ' + str(LCS('ABCBDAB', 'BDCABA')))
print('LCS: ' + str(LCS('AGGTAB', 'GXTXAYB')))