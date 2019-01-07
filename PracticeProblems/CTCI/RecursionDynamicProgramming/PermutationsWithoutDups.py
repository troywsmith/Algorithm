def makePermsForChar(word, c):
    perms = []
    for i in range(len(word)):
        perms.append(word[:i] + c + word[i:])
    perms.append(word + c)
    return perms


def getPerms(s):
    """
    Solution: Naive
    Time Complexity: O(N!)
    """
    if len(s) <= 0:
        return None

    # Base Case
    if len(s) == 1:
        return [s[0]]

    subprob_perms = getPerms(s[1:])

    perms = []

    for word in subprob_perms:
        more_perms = makePermsForChar(word, s[0])
        perms.extend(more_perms)

    return perms


if __name__ == '__main__':
    s = 'abcde'
    perms = getPerms(s)

    print('Here are all the permutations for the word: {}'.format(s))
    for i, perm in enumerate(perms):
        print('{}: {}'.format(i+1, perm))

else:
    print('Importing: String Permutations (no duplications) Algorithm')