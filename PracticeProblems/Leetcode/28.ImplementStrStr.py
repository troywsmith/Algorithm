def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(needle) == 0:
        return 0

    if len(haystack) < len(needle) or len(haystack) == 0:
        return -1

    H = len(haystack)
    N = len(needle)
    d = 256
    q = 101
    h = 0
    n = 0

    z = pow(d, N-1, q)

    # Compute hash value for needle as well as first N long sequence of needle
    for i in range(N):
        n = (d*n + ord(needle[i])) % q
        h = (d*h + ord(haystack[i])) % q

    # Iterate through haystack
    for i in range(H-N+1):

        # If hash values are equal, return i
        if n == h:
            if needle == haystack[i:i+N]:
                return i

        # Break if we are at the end of the haystack
        if i == H - N:
            break

        # If not, rehash h by adding removing first char and adding new

        old_char = haystack[i]
        new_char = haystack[i + N]

        h = (d*(h - ord(old_char)*z) + ord(new_char)) % q

    return -1