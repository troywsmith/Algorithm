class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(char) for char in str((int(''.join([str(x) for x in digits])) + 1))]


solution = Solution()
print(solution.plusOne([1,2,3]))
print(solution.plusOne([4,3,2,1]))

# Edge case 9 at end
print(solution.plusOne([1,2,9]))

# Edge case array is [0]
print(solution.plusOne([0]))