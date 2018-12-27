class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        L = 0
        R = len(height)-1

        while L < R:
            x = R - L
            y = min(height[L], height[R])
            area = x * y
            maxArea = max(maxArea, area)
            if height[L] < height[R]:
                L += 1
            else:
                R -= 1

        return maxArea


s = Solution()
print('Max Area: {}'.format(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])))
