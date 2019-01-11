"""
You have an integer and you can flip exactly one bit from 0 to 1.
Write code to find the length of the longest sequence of 1s you could create.
"""


def flip_bit(n):
    """
    Time Complexity (WC): O(N^2) where N is digits in binary rep of n
    Questions: can be negative?
    """

    longest_subseq = 0
    curr_subseq = 0

    # Convert number to binary then to string. Also remove signed bits
    n = list(str(bin(n)))[2:]
    all_off = list('0' * (32 - len(n)))
    n = all_off + n

    # Iterate throught string
    zero_indexes = []
    for i, digit in enumerate(n):

        # Record longest subsequence of 1 bits
        if digit == '1':
            curr_subseq += 1
            longest_subseq = max(longest_subseq, curr_subseq)

        # Record the indexes of all 0 bits
        if digit == '0':
            zero_indexes.append(i)
            curr_subseq = 0

    # Iterate through index array
    for index in zero_indexes:
        curr_subseq = 0

        # For each index, set index in string to 1
        n[int(index)] = '1'

        # Iterate through string and record longest subseq if longer
        for digit in n:

            # print(digit, n)

            if digit == '1':
                curr_subseq += 1
                longest_subseq = max(longest_subseq, curr_subseq)
            else:
                curr_subseq = 0

        # Set index back to 0
        n[int(index)] = '0'

    # Return longest subsequence
    return longest_subseq


if __name__ == '__main__':
    n = 71
