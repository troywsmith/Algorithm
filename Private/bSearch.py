def binarySearch(arr, val):
    if len(arr) == 0:
        return False

    else:
        mid = len(arr) // 2

        if arr[mid] == val:
            return True

        elif arr[mid] < val:
            return binarySearch(arr[mid+1:], val)

        else:
            return binarySearch(arr[:mid], val)

print(binarySearch([1,2,3,4,5,6,7,8,9], 9))