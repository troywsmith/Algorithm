"""
Input: MxN matrix (each row and each column is sorted in ascending order)
Ouput: Find an element, val
"""
import random


# def search(matrix, target, start_row, end_row, start_col, end_col):

#     print(' ')
#     for row in matrix[start_row:end_row]:
#         print(row[start_col:end_col])

#     if len(matrix[start_row:end_row]) <= 2 or len(matrix[0]) <= 2:
#         return False

#     # Find middle element of middle row
#     mid_row = (start_row + end_row) // 2
#     mid_col = (start_col + end_col) // 2

#     mid_el = matrix[mid_row][mid_col]  # 74
#     print(mid_el)

#     if target == mid_el:
#         return True

#     # If target is higher, we can get rid of element to the left of middle index for all above middle
#     if target > mid_el:

#         # we want to start at row mid_i a
#         return search(matrix, target, mid_row, end_row, start_col, end_col)

#     # If target is lower, we can get rid of element to the right of middle index for all below middle
#     if target < mid_el:

#         # we want to start at row mid i _ 1
#         return search(matrix, target, start_row, mid_row+1, start_col, end_col)

#     return -1


# def random_num():
#     return random.randint(100, 900)


# def print_matrix(matrix):
#     for row in matrix:
#         print(row)

def b_search(arr, target):
    print(arr)
    if len(arr) <= 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == target:
            return True
        elif target < arr[mid]:
            return b_search(arr[:mid], target)
        else:
            return b_search(arr[mid+1:], target)
    return -1


def check_rows(rows, target):
    for row in rows:
        if row[0] <= target and target <= row[len(row)-1]:
            if b_search(row, target):
                return True
    return False


def check_cols(rows, target, start_col, end_col):
    for row in rows:
        if row[start_col] <= target and target <= row[end_col]:
            if b_search(row[start_col:end_col+1], target):
                return True
    return False


def search(arr, target):

    if len(arr) <= 1:
        return False

    rows = len(arr)
    cols = len(arr[0])

    mid_row = (rows-1) // 2
    mid_col = (cols-1) // 2
    midpoint = arr[mid_row][mid_col]

    if target == midpoint:
        return True

    if target > midpoint:
        if check_rows(arr[mid_row:], target):
            return True
        if check_cols(arr:mid_row], target, mid_col+1, cols-1):
            return True

    if target < midpoint:
        if check_rows(arr[:mid_row+1], target):
            return True
        if check_cols(arr[mid_row+1:], target, 0, mid_col):
            return True

    return False


if __name__ == '__main__':
    matrix = [
        [50, 52, 54, 86, 100],
        [60, 62, 64, 88, 101],
        [70, 72, 74, 89, 102],
        [80, 82, 84, 90, 105],
        [90, 92, 94, 96, 107]
    ]
    target = 88
    start_row = 0
    end_row = len(matrix)
    start_col = 0
    end_col = len(matrix[0])
    print(search(matrix, target))
    # print(search(matrix, target, start_row, end_row, start_col, end_col))
