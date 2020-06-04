"""
Name: Naive String Matching
Description: Returns all occurences of pattern string in text string
Input: a text string and a pattern string
Output: list of occurences
Time Complexity: best-O(n), worst O(m(n-m+1))
Space Complexity: 
Algorithm Technique: N/A
"""


def find_match(T, P):
    n = len(T)
    m = len(P)

    matches = []

    for i in range(n-m+1):

        if T[i:i+m] == P:
            matches.append(i)

    return('Matches at: ' + str(matches))


print(find_match('acaabc', 'aab'))
print(find_match('acaaca', 'aca'))
print(find_match('000010001010001', '0001'))