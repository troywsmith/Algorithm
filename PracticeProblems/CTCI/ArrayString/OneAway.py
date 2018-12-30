# Question 1.5
def isOneAway(s, t):
    """
    can do one of the following edits once: insert, remove, replace
    """
    m = len(s)
    n = len(t)

    if s == t:
        return True

    if abs(m-n) > 1:
        return False

    (smaller, bigger) = (s, t) if len(s) < len(t) else (t, s)
    smallerIndex = 0
    biggerIndex = 0

    foundDiff = False

    while smallerIndex < len(smaller) and biggerIndex < len(bigger):
        if smaller[smallerIndex] != bigger[biggerIndex]:
            if foundDiff:
                return False
            foundDiff = True

            if len(smaller) == len(bigger):
                smallerIndex += 1

        else:
            smallerIndex += 1

        biggerIndex += 1

    return True


print(isOneAway('pale', 'ple'))
print(isOneAway('pales', 'pale'))
print(isOneAway('pale', 'bale'))
print(isOneAway('pale', 'bake'))
print(isOneAway('all', 'aal'))
