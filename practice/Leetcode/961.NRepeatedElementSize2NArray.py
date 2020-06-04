class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        N = len(A) / 2
        counts = {}
        for num in A:
          counts[num] = 0

        for num in A:
          counts[num] += 1
          if counts[num] == N:
            return num



s = Solution()
print('Result: ' + str(s.repeatedNTimes([1,2,3,3])))
print('Result: ' + str(s.repeatedNTimes([2,1,2,5,3,2])))
print('Result: ' + str(s.repeatedNTimes([5,1,5,2,5,3,5,4])))