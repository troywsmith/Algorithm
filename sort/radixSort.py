def countingSort(arr, exp):
  
    n = len(arr)

    # Build count array
    count = [0] * 10
    for i in range(0, n):
        index = arr[i] / exp
        count[index % 10] += 1

    # Modify count so each value adds the previous value
    for x in range(1, 10):
        count[x] += count[x-1]

    # Create new arr same size as input arr
    result = [0] * len(arr)

    i = n - 1
    while i >= 0:
        index = arr[i] / exp
        result[count[index % 10] - 1] = arr[i]
        count[(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = result[i]


def radixSort(arr, d):
    maxElem = max(arr)

    exp = 1
    while maxElem / exp > 0:
        countingSort(arr, exp)
        exp *= 10

    return arr


A = [329, 457, 657, 839, 436, 720, 355]
print(radixSort(A, 3))
