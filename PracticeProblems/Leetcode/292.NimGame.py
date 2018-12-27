class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # return n % 4 != 0
        counts = {}
        stones = n
        moves = range(1,4)

        while stones > 0:
          print(stones)

          move = 1
          counts[stones] = [stones - move for move in moves if stones > 2]
          stones -= move
        
        print(counts)

solution = Solution()
# print(solution.canWinNim(1))
# print(solution.canWinNim(2))
# print(solution.canWinNim(3))
# print(solution.canWinNim(4))
print(solution.canWinNim(10))
# print(solution.canWinNim(12))
# print(solution.canWinNim(20))