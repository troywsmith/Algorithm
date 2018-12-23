def findSum(arr, val):
    left = 0
    right = len(arr) - 1

    while left < right:
        sm = arr[left] + arr[right]

        if sm == val:
            return True
        if sm < val:
            left += 1
        if sm > val:
            right -= 1

    return False


print(findSum([1, 2, 4, 7, 12, 22], 19))