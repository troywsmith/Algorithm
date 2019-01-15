def sum_swap(arr1, arr2):
    """
    Time Complexity: O(N + M)
    Space Complexity: O(N)
    """

    shorter, longer = (arr1, arr2) if len(arr1) < len(arr2) else (arr2, arr1)

    # Find sums of each array
    shorter_sum = sum(shorter)
    longer_sum = sum(longer)

    # Convert longer to a hashtable for quick lookup
    longer_set = set(longer)

    # For each element in shorter arr
    for s, num in enumerate(shorter):

        # Calculate complement of element that we need to find in longer array
        comp = (shorter_sum - longer_sum) - num

        # See if complement is in longer set
        if comp in longer_set:

            # If match, swap
            l = longer.index(comp)
            shorter[s], longer[l] = longer[l], shorter[s]
            return [shorter[s], longer[l]]
      
    return False


if __name__ == '__main__':
    arr1 = [4, 1, 2, 1, 1, 2]   # sum = 11
    arr2 = [3, 6, 3, 3]		      # sum = 15
    print(arr1, arr2)
    print(sum_swap(arr1, arr2))
    print(arr1, arr2)
