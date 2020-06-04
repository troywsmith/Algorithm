def merge_sort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Recursive Case
    else:
        midpoint = len(arr) // 2

        left = merge_sort(arr[:midpoint])
        right = merge_sort(arr[midpoint:])

        return merge_sorted_arrays(left, right)

def merge_sorted_arrays(arr1, arr2):

    merged = []

    while len(arr1) and len(arr2):

        if arr1[0] < arr2[0]:
            merged.append(arr1[0])
            arr1.pop(0)

        else:
            merged.append(arr2[0])
            arr2.pop(0)

    merged += arr1 + arr2

    return merged


print(merge_sort([213, 32, 234, 5, 234, 34, 24, 475, 2, 2357]))
