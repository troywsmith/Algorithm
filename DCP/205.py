"""
This problem was asked by IBM.
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.
"""

# # Brute Force
# import itertools
# def findNextOrder(n):
#   nStr = str(n)
#   chars = [x for x in nStr]
#   perms = list(itertools.permutations(chars))
#   intPerms = sorted([int(''.join(perm)) for perm in perms])
#   return intPerms[intPerms.index(n) + 1]
# print(findNextOrder(489))

# Better Solutioin
def findNextOrder(n):
    nStr = str(n)

    result = n - 1
    while result < n:
      print(result)
      result = int(nStr)

    return result

print(findNextOrder(489))