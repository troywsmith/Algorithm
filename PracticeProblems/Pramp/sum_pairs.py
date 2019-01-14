def find_pairs(arr, k):

    # Solution 1:
    # Sort array and remove duplicates
    arr.sort()
    arr = set(arr)
    arr = list(arr)

    # Store results in a set so duplicates are not allowed
    results = set()

    # Use 2 pointer, l at start, r at end
    l = 0
    r = len(arr) - 1
    while l < r:

        sm = arr[l] + arr[r]

        # If sum is less than k, move left pointer in
        if sm < k:
            l += 1

        # If sum is greater than k, move right pointer in
        elif sm > k:
            r -= 1

        # if elements add to k, add pair to results and move both pointers
        else:
            pair_string = str(arr[l]) + '_' + str(arr[r])
            results.add(pair_string)
            l += 1
            r -= 1

    for pair in results:
        normal_pair = pair.split('_')
        print(normal_pair)


# arr = [1, 3, 2, 3, 2, 5, 46, 6, 7, 4]
arr = [1, 3, 2, 3, 3, 4, 5, 2, 7, 3, 2, 5, 46, 6, 7, 4, 9, 8, 1]
k = 9
print(find_pairs(arr, k))
