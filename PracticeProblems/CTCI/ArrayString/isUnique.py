# Question 1.1


def isUnique(s):
    """ 
    Implementation using another data structure 
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    for char in s:
        if char in seen:
            return False
        else:
            seen.add(char)
    return True


def isUnique2(s):
    """ 
    Implementation without using another data structure 
    Time Complexity: O(n log n)
    Space Complexity: O(n) - because of built in timsort
    """
    s = sorted(s)
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            return False
    return True
