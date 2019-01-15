def subsort(arr):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    m = 0
    n = len(arr) - 1

    # Iterate through array from front and back
    found_m, found_n = False, False
    while not found_m and not found_n:

        # If m and n ever meet, return 0 as the array is sorted
        if m == n:
            return 0

        # Once we find first unsorted adj elem from front, set index to m
        if not found_m:
            if arr[m] <= arr[m+1]:
                m += 1
            else:
                found_m = True

        # Once we find first unsorted adj elem from back, set to n
        if not found_n:
            if arr[n] >= arr[n-1]:
                n -= 1
            else:
                found_n = True

    # Find lowest and highest in unsorted range
    lowest = float('inf')
    highest = float('-inf')
    for num in arr[m:n+1]:
        lowest = min(lowest, num)
        highest = max(highest, num)

    # Find correct position in left part of array
    for i in range(len(arr)):
        if arr[i] > lowest:
            m = i
            break
    
    # Find correct position in right part of array
    for i in range(len(arr)-1, n, -1):
        if arr[i] < highest:
            n = i
            break

    return (m, n)


if __name__ == '__main__':
    arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(subsort(arr))
