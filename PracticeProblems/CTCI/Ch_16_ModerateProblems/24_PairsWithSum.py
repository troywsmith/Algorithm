def find_pairs(arr, target):

    if len(arr) <= 1:
        return 0

    # Store all valid pairs as set
    results = set()

    # Sort the array
    arr.sort()

    # Iterate over it from front and back with small and big pointers
    small = 0
    big = len(arr) - 1

    while small < big:

        curr_sum = arr[small] + arr[big]

        # If the target is less than small + big, move small right
        if target < curr_sum:
            big -= 1

        # If the target is greater than small + big, move big left
        elif target > curr_sum:
            small += 1

        # If none of those, they must be equal and we should add pair to result
        # Also, move small pointer right and big pointer left
        else:
            results.add((arr[small], arr[big]))
            small += 1
            big -= 1

    # Return results
    return results


if __name__ == '__main__':
    arr = [1, 3, 45, 6, 7, 4, 6, 8, 4, 7]
    tar = 8
    print(find_pairs(arr, tar))
