# def findMagicIndex(arr):
#     """
#     Solution: Naive Approach
#     Time Complexity: O(n)
#     """
#     for x, num in enumerate(arr):

#         if x == num:
#             return x

#     return False


def findMagicIndex(arr, start, end):
    """
    Solution: Binary Search
    Time Complexity: O(log n)
    """
    modified_arr = arr[start:end+1]

    if not modified_arr:
        return False

    if len(modified_arr) < 1:
        return False

    m = start + len(modified_arr) // 2

    if arr[m] == m:
        return m

    elif arr[m] > m:
        return findMagicIndex(arr, start, m-1)

    else:
        return findMagicIndex(arr, m+1, end)


if __name__ == '__main__':

    arr = [-12, 4, 2, 4, 6, 8, 10]

    print(findMagicIndex(arr, 0, len(arr)-1))
