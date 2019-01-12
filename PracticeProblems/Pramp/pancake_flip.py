def flip_arr(arr, k):
    i = 0
    while i <= k:
        arr[i], arr[k] = arr[k], arr[i]
        i += 1
        k -= 1

    return arr


def find_max(arr):
    max_i = 0
    max_num = float('-inf')

    for i, num in enumerate(arr):
        if num > max_num:
            max_i = i
            max_num = num

    return max_i


def pancake_sort(arr):

    # intitialize current end to actual end of arr
    end = len(arr) - 1

    while end >= 1:

        # find index of max element in arr
        max_i = find_max(arr[:end+1])

        # flip arr up to biggest element index
        arr = flip_arr(arr, max_i)

        # flip entire arr up to current end
        arr = flip_arr(arr, end)

        end -= 1

    return arr


if __name__ == '__main__':
    arr = [1, 5, 4, 3, 2]
    print(arr)
    print(pancake_sort(arr))
