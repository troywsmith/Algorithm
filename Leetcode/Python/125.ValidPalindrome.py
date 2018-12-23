class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        alnums = ''.join([x.lower() for x in s if x.isalnum()])
        return alnums == alnums[::-1]

solution = Solution()
print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("race a car"))