"""
Question: Print Duplicates
Input: array w/ all numbers 1 through N
Output: print duplicates
Contraints: 4 KB of memory
"""


def print_duplicates(arr):
    # 1 KB = 1024 bytes = 8192 bits
    # 4 KB = 4000 bytes = 32768 bits 
    # (4000/24) = 167 ints ?

    # How can we compress an int to a small size? Trie?

    return



# nums = [1, 12, 3, 13, 12, 312, 3, 123, 123, 12, 3, 512, 45, 12, 412, 31,
#         24, 124, 124, 1, 41, 41, 4, 12, 412, 4, 124, 124, 12, 412, 41, 2, 1]
nums = [1, 8, 4, 14, 82, 736]
print_duplicates(nums)
