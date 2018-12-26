class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sRev = s[::-1]

        dp = [[0 for x in range(len(s)+1)] for x in range(len(s)+1)]
        endIndex = 0

        for x in range(1, len(s)+1):
            for y in range(1, len(s)+1):

                if s[x-1] == sRev[y-1]:
                    dp[x][y] = dp[x-1][y-1] + 1
                    endIndex = x - 1

                else:
                    dp[x][y] = max(dp[x][y], dp[x-1][y], dp[x][y-1])

        palLength = dp[-1][-1]
        LP = s[endIndex - palLength:endIndex]
        return LP


s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
print(s.longestPalindrome('aabb'))
