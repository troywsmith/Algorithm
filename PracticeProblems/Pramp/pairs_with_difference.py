from collections import defaultdict


def find_pairs_with_given_difference(arr, k):

    # If array has less than 2 elements, it cannot have a pair with diff k
    if len(arr) < 2:
        return []

    # Create a hash table for quick lookup
    diffMap = defaultdict()
    results = []

    # Iterate through array, store diff of x minus k
    for x in arr:
        diffMap[x - k] = x

    # Iterate through array to check if each element is a pair with element from before
    for y in arr:
        if y in diffMap:
            results.append([diffMap[y], y])

    # Return all pairs with corrent difference
    return results


if __name__ == '__main__':
    arr = [0, -1, -2, 2, 1]
    k = 1
    print(find_pairs_with_given_difference(arr, k))
