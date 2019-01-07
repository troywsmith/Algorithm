def updateBits(n, m, i, j):
    """
    Input: N & M (32-bit numbers), i & j (bit positions)
    Problem: Insert M into N such that M starts at bit j and end at bit i
    Assumptions: bits j through i have enough space to fit all of M
    """

    # will equal sequence of all ls
    allOnes = ~0

    # ls before position j,
    # then 0s. left = 11100000
    left = allOnes << (j + 1)

    # l's after position i. right = 00000011
    right = ((1 << i) - 1)

    # All ls, except for 0s between
    # i and j. mask 11100011
    mask = left | right

    # Clear bits j through i then put min there
    n_cleared = n & mask

    # Move m into correct position.
    m_shifted = m << i

    return (n_cleared | m_shifted)


# Driver Code
if __name__ == '__main__':
    n = 1024  # in Binary N = 10000000000
    m = 19    # in Binary M = 10011
    i = 2
    j = 6
    result = updateBits(n, m, i, j)
    print(bin(result))
