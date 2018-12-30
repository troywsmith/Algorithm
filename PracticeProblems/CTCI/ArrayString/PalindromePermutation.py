# Question 1.4
from collections import defaultdict

# def isPalindrome(s):
#   return s == s[::-1]


def isPermutationPalindrome(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    charMap = defaultdict()
    odds = 0

    for char in s:

        if char == ' ':
            continue

        char = char.lower()

        if char in charMap:
            if charMap[char] == False:
                charMap[char] = True
                odds -= 1
            else:
                charMap[char] = False
                odds += 1

        else:
            charMap[char] = False
            odds += 1

    return odds <= 1


print(isPermutationPalindrome('Tact Coa'))
print(isPermutationPalindrome('raceacar'))
