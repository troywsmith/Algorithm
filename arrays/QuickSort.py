def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def quick_sort_helper(arr, first, last):
    if first < last:
        splitpoint = partition(arr, first, last)

        quick_sort_helper(arr, first, splitpoint - 1)
        quick_sort_helper(arr, splitpoint + 1, last)

def partition(arr, first, last):
    pivotvalue = arr[first]

    left = first + 1
    right = last

    done = False

    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left += 1

        while arr[right] >= pivotvalue and right >= left:
            right -= 1

        if right < left:
            done = True

        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

        print(arr)

    temp = arr[first]
    arr[first] = arr[right]
    arr[right] = temp

    return right


print(quick_sort([235, 2, 6, 23, 64, 24, 3, 64, 253, 45]))