class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        min_len = float('inf')
        
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        for word in strs:
            if word == "": return ""
            if len(word) < min_len: min_len = len(word)

        for j in range(min_len):
            letter = [word[j] for word in strs]
            if len(set(letter)) != 1: return strs[0][0:j]

        return strs[0][0:min_len]


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))
print(solution.longestCommonPrefix(["flower"]))
print(solution.longestCommonPrefix(["aa", "a"]))
print(solution.longestCommonPrefix([]))