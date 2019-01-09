from collections import Counter


def getPerms(s):
    """
    Solution: Naive
    Time Complexity: O(N!)
    """
    hash_table = Counter()
    for char in s:
        hash_table[char] += 1
    perms = []
    makePermsForWord(' ', hash_table, perms)
    return perms


def makePermsForWord(word, hash_table, perms):
    sm_hash = sum(hash_table.values())
    if sm_hash <= 0:
        perms.append(word)
    else:
        for char in hash_table:
            hash_copy = hash_table.copy()
            if hash_copy[char] <= 1:
                hash_copy.pop(char, None)
            else:
                hash_copy[char] -= 1
            makePermsForWord(s + char, hash_copy, perms)


if __name__ == '__main__':
    s = 'abbb'
    perms = getPerms(s)

    print('Here are all the permutations for the word: {}'.format(s))
    for i, perm in enumerate(perms):
        print('{}: {}'.format(i+1, perm))

else:
    print('Importing: String Permutations (with duplications) Algorithm')