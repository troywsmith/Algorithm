"""
This problem was asked by Dropbox.
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".
"""

def getColumnID(n):

    result = []
    while n > 0:
        remain = n % 26
        if remain == 0:
            result.append('Z')
            n = (n / 26) - 1
        else:
            result.append(chr((remain - 1) + ord('A')))
            n = n / 26

    return ''.join(result[::-1])

print('Column ID: ' + getColumnID(1))
print('Column ID: ' + getColumnID(27))
print('Column ID: ' + getColumnID(2))
print('Column ID: ' + getColumnID(200))
print('Column ID: ' + getColumnID(900))
print('Column ID: ' + getColumnID(90124132130))