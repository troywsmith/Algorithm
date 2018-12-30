def isStringRotation(A, B):
    """
    Time Complexity:
    Space Complexity:
    """
    if len(A) != len(B):
        return False

    rotatePoint = 0
    for i in range(len(A)):
        if A[i] == B[rotatePoint]:
            rotatePoint += 1

    return A == B[rotatePoint:] + B[:rotatePoint]


print(isStringRotation('waterbottle', 'erbottlewat'))
print(isStringRotation('waterbottle', 'ewaterbottl'))
print(isStringRotation('waterwater', 'erwaterwat'))
print(isStringRotation('aaaba', 'aabaa'))
print(isStringRotation('bbaa', 'baba'))