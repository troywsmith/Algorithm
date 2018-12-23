def findLengthLast(s):
    words = s.strip().split()
    if words == []: return 0
    else: return len(words[-1])

print(findLengthLast('  '))
print(findLengthLast('a'))
print(findLengthLast('a '))
print(findLengthLast(' a'))
print(findLengthLast(' a '))
print(findLengthLast(' day'))
print(findLengthLast('Hello World'))