def repeatedSubstringPattern(s):
    reversed(s)
    return s in (s + s)[1:-1]

print(repeatedSubstringPattern('abab'))
print(repeatedSubstringPattern('aba'))
print(repeatedSubstringPattern('abcabcabcabc'))