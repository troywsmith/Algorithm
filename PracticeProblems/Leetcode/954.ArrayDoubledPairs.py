from collections import Counter


def canReorderDoubled(arr):
    """
    :type A: List[int]
    :rtype: bool
    """

    count = Counter(arr)
    print(count)

    for x in sorted(arr, key=abs):
        if count[x] == 0:
            continue

        if count[2*x] == 0:
            return False

        count[x] -= 1
        count[2*x] -= 1

    print(count)
    return True


if __name__ == '__main__':
    arr = [4, -2, 2, -4]
    # arr = [2, 1, 2, 4]
    # arr = [3, 1, 3, 6]
    # arr = [1, 2, 4, 16, 8, 4]
    print(canReorderDoubled(arr))