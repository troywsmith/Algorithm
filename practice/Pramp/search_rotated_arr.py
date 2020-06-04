def search_rotated_array(arr, num):
    return search(arr, num, 0, len(arr)-1)


def search(arr, num, l, r):

    # If left less than right, num is not in arr
    if l > r:
        return -1

    # Find midpoint
    m = (l + r) // 2

    # Check if mid element is equal to num. If it is, return that index
    if arr[m] == num:
        return m

    # If first element is less than midpoint, left half is ordered correctly
    if arr[l] <= arr[m]:

        # Check if num is between the values. If it is, we can normal b search left subarray
        if arr[l] <= num and num <= arr[m]:
            return search(arr, num, l, m-1)

        # If not, we can repeat process with right subarray
        else:
            return search(arr, num, m+1, r)

    # If midpoint is less than last element, right half is ordered correctly
    elif arr[m] < arr[r]:

        # Check if num is between the values. If it is, we can normal b search right subarray
        if arr[m] <= num and num <= arr[r]:
            return search(arr, num, m+1, r)

        # If not, we can repeat process with left subarray
        else:
            return search(arr[:m], num, l, m-1)

    # If above conditions fail, we have an error
    else:
        return 'ERROR'


if __name__ == '__main__':
    arr = [9, 12, 17, 2, 4, 5]
    num = 9
    print(search_rotated_array(arr, num))