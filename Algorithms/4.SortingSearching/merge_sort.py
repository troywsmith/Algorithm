def mergeSort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Recursive Case
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        return mergeSortedArrays(mergeSort(left), mergeSort(right))


def mergeSortedArrays(left, right):

    merged = []

    while len(left) and len(right):

        if left[0] < right[0]:
            merged.append(left[0])
            left.pop(0)

        else:
            merged.append(right[0])
            right.pop(0)

    merged += left + right
    return merged


print(mergeSort([4346, 346, 2345, 8, 32, 8, 34, 6, 3, 8, 3, 8888]))
