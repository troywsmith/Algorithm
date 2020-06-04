def countingSort(arr, k):

    # Build count array
    count = [0 for _ in range(k+1)]
    for num in A:
        count[num] += 1

    # Modify count so each value adds the previous value
    for x in range(1, len(count)):
        count[x] += count[x-1]

    # Create new arr same size as input arr
    result = [0] * len(arr)

    for num in arr:
        result[count[num] - 1] = num
        count[num] -= 1

    return result


A = [1, 4, 1, 2, 7, 5, 2]
print(countingSort(A, 9))
