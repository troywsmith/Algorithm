# Question 1.2
from collections import defaultdict


def checkPermutation(s, t):
    """
    Time Complexity: O(mlogm + nlogn)
    Space Complexity: O(m+n)
    """
    if len(s) != len(t):
        return False
    if sorted(s) != sorted(t):
        return False
    return True


def checkPermutation2(s, t):
    """
    Time Complexity: O(m+n)
    Space Complexity: O(n)
    """
    if len(s) != len(t):
        return False

    sMap = defaultdict()
    for x in range(len(s)):
        if s[x] in sMap:
            sMap[s[x]] += 1
        else:
            sMap[s[x]] = 1

    for x in range(len(t)):
        sMap[t[x]] -= 1
        if sMap[t[x]] < 0:
            return False

    return True
