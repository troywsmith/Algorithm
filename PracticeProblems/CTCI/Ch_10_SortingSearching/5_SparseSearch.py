# def search(arr, s):
#     """
#     Naive Method
#     Time Complexity: O(n)
#     Space Complexity: O(1)
#     """
#     for i, elem in enumerate(arr):
#         if elem == s:
#             return i


def search(arr, word):
    """
    Description: Binary Search w/ fix for empty string issue
    Time Complexity: O(log n) average, O(n) worst
    Space Complexity: O(1) + recurse
    """
    if len(arr) < 1:
        return False
    if len(arr) == 1:
        return arr[0] == word

    m = len(arr) // 2

    # If m is blank, we need to search for the closest valid word
    x, y = m-1, m+1
    while arr[m] == '':

        if x >= 0:
            if arr[x] != '':
                m = x

        if y <= len(arr) - 1:
            if arr[y] != '':
                m = y
        x -= 1
        y += 1

    if arr[m] == word:
        return m
    elif word < arr[m]:
        return search(arr[:m], word)
    else:
        return search(arr[m+1:], word)

    return -1


arr = ['at', '', '', '', 'ball', '', '', 'car', '', '', 'dad', '', '']
s = 'ball'
print(search(arr, s))
