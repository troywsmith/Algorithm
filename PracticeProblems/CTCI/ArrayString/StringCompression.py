# Question 1.6

def compressString(s):
    """
    Time Complexity: O(n+m) ?? 
    Space Complexity: O(m)
    """

    if len(s) <= 2:
        return s

    currChar = ''
    k = 0
    count = 0
    compressList = []

    for char in s:

        if char == currChar:
            k += 1

        else:
            if count > 0:
                compressList.append(currChar + str(k))

            currChar = char
            k = 1

        count += 1

    compressList.append(currChar + str(k))
    compressed = ''.join(compressList)
    return compressed if len(currChar) < len(s) else s


print(compressString('aabcccccaaa'))
print(compressString('aa'))
print(compressString('a'))
print(compressString('aaaaaaaab'))
print(compressString('baaaaaaaab'))
