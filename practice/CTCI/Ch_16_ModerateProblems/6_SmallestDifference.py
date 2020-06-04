"""
Given two arrays of integers, compute the pair of values (one value in each array) with the smallest non-negative difference
Return the difference
"""


def smallest_pair(arr1, arr2):
    """
    Solution 2: O(N log N + M log M)
    """
    # Sort both the arrays
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    # Initiliaze the smallest diff to first elements in each array
    smallest_diff = abs(arr1[0] - arr2[0])
    pair = [arr1[0], arr2[0]]

    
    x = 0
    y = 0
    while x < len(arr1) and y < len(arr2):

        # If they are equal, difference is 0 and we cannot beat that
        if arr1[x] == arr2[y]:
            return 0

        # If element in arr1 is less than element in arr2, move arr1 pointer right
        elif arr1[x] < arr2[y]:
            diff = abs(arr1[x] - arr2[y])
            if diff < smallest_diff:
                smallest_diff = diff
                pair = [arr1[x], arr2[y]]
            x += 1

        # Otherwise arr1 element must be greater than arr1 element so we move arr2 pointer right
        else:
            diff = abs(arr1[x] - arr2[y])
            if diff < smallest_diff:
                smallest_diff = diff
                pair = [arr1[x], arr2[y]]
            y += 1

    # Return the smallest difference
    print(pair)
    return max(pair) - min(pair)


if __name__ == '__main__':
    arr1 = [1, 3, 15, 11, 2]      # [1,2, 3, 11, 15]
    arr2 = [23, 127, 235, 19, 8]  # [8,19,23,127,235]
    ans = smallest_pair(arr1, arr2)
    print('The smallest possible pair is {}'.format(ans))
