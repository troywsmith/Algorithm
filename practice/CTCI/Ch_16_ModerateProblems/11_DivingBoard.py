from collections import defaultdict
import pprint


def find_lengths(k, short, long):
    """
    Time Complexity: O(k * l)
    Space Complexity: (k)
    """

    # Store lengths in variable lengths
    lengths = defaultdict()

    # If k is 0, we cannot create any lengths
    lengths[0] = [0]

    # If k is 1, can be either short or long
    lengths[1] = [short, long]

    # Iterate from 2 to k
    for i in range(2, k+1):

        # Get k - 1 lengths
        last_lengths = lengths[i-1]
        new = set()

        for length in last_lengths:

            # Add a short to each length and store in lengths[k]
            new.add(length + short)

            # Add a long to each and store in lengths[k]
            new.add(length + long)

        # Set current planks to new lengths
        lengths[i] = new

    # Return lengths for k planks
    return lengths[k]


if __name__ == '__main__':

    k = 3
    short = 5
    long = 10
    print(find_lengths(k, short, long))
