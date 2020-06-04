def sorted_merge(A, B):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    x = len(A) - len(B) - 1
    y = len(B) - 1

    # For back of A index
    z = len(A) - 1

    # Iterate i backwards through arrays from b-1 -> 0
    while y >= 0:

        # Compare elements. Swap greater element with back index
        if A[x] >= B[y]:
            A[z] = A[x]
            x -= 1

        elif B[y] > A[x]:
            A[z] = B[y]
            y -= 1

        z -= 1

    return A


# Driver Function
A = [1, 4, 7, 9, 16, 57, None, None, None]
B = [2, 5, 7]
print(sorted_merge(A, B))
