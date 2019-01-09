def b_search(arr, start, end, val):

    while start <= end:
        m = (start + end) // 2

        if arr[m] == val:
            return m

        elif val < arr[m]:
            end = m
        else:
            start = m+1

    return -1


def search(listy, val):
    """
    Constraints:
    - Cannot find size of arr
    - Can still get element at index i in O(1) time
    - If i is beyond size of arr, it returns -1

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """

    # Optimization: compare multiples of 10 to create a start and upper bound on the size
    start, end = 1, 1
    while listy[end] < val:
        start = end
        end *= 2

    return b_search(listy, start, end, val)


arr = [2, 4, 6, 7, 12, 45, 246, 234, 2525, 25235, 252352, 234, -1]
negs = [-1] * 10*100
val = 45
print(search(arr+negs, val))
