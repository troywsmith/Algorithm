class Solution:
    def maxCrossSum(self, nums, l, m, r):
        sum = 0
        left_sum = float('-inf')
        for i in range(m, l-1, -1):
            sum += nums[i]
            if sum > left_sum:
                left_sum = sum

        sum = 0
        right_sum = float('-inf')
        for i in range(m+1, r+1):
            sum += nums[i]
            if sum > right_sum:
                right_sum = sum

        return left_sum + right_sum

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1

        if l == r:
            return nums[0]

        m = r // 2
        
        return max(
            self.maxSubArray(nums[:m+1]),
            self.maxSubArray(nums[m+1:r+1]),
            self.maxCrossSum(nums, l, m, r)
        )


sol = Solution()
print(sol.maxSubArray([1,2]))
# print(sol.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
