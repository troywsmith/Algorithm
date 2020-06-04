# arr = [1,2,3,4,5,6,7,8,9] -> [7,8,9,1,2,3,4,5,6]: has been rotated BEFORE mid
# arr = [1,2,3,4,5,6,7,8,9] -> [9,1,2,3,4,5,6,7,8]: has been rotated BEFORE mid
# arr = [1,2,3,4,5,6,7,8,9] -> [3,4,5,6,7,8,9,1,2]: has been rotated AFTER mid
# arr = [1,2,3,4,5,6,7,8,9] -> [6,7,8,9,1,2,3,4,5]: has been rotated AFTER mid
# val = 5


def b_search_rotated_array(arr, val):

    if len(arr) < 1:
        return False
    if len(arr) == 1:
        return arr[0] == val

    else:
        l = 0
        m = len(arr) // 2
        r = len(arr) - 1

        if arr[l] == val or arr[m] == val or arr[r] == val:
            return True

        # Rotation happens before midpoint so right is sorted correctly
        elif arr[l] > arr[m] and arr[m] < arr[r]:

            # If value is between mid and end elem, if it is, b search that range,
            if arr[m] < val and arr[r] >= val:
                return b_search_rotated_array(arr[m:r+1], val)

            # If not, repeat with left range
            else:
                return b_search_rotated_array(arr[l:m], val)

        # Rotation happens after midpoint so left is ordered correctly
        elif arr[l] < arr[m] and arr[r] < arr[m]:

            # If value is between start and mid elem, search that range,
            if arr[0] <= val and arr[m] > val:
                return b_search_rotated_array(arr[l:m+1], val)

            # If not, search right range
            else:
                return b_search_rotated_array(arr[m+1:r], val)

        else:
            if b_search_rotated_array(arr[:m], val):
                return True
            elif b_search_rotated_array(arr[m+1:], val):
                return True
            else:
                return False

    return -1


arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
# arr = [9, 1, 2, 3, 4, 5, 6, 7, 8]
# arr = [3, 4, 5, 6, 7, 8, 9, 1, 2]
# arr = [2, 4, 5, 2, 2, 2, 2]
val = 8

print(b_search_rotated_array(arr, val))
