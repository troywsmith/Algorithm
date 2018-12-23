def isSubsequence(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    print(s, t)

    # Normalize t
    newT = ''
    sI = 0
    for char in t:
        if sI < len(s):
          if char == s[sI]:
              newT += char
              sI += 1

    return s == newT

print('Result: ' + str(isSubsequence('abc', 'ahbgdc')))
print('Result: ' + str(isSubsequence('axc', 'ahbgdc')))
print('Result: ' + str(isSubsequence('aaa', 'ahbagdac')))
print('Result: ' + str(isSubsequence('aaa', 'a')))