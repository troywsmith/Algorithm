ls = [1, 4, 1, 7, 3, 563, 2345, 456, 234, 3456, 34, 7, 3, 436, 2, 5]
tar = 74

# def linear_search(arr, target):
#   for x in range(len(arr)):
#     if arr[x] == target: return True
#   return False
# print(linear_search(ls, tar))

# def binarySearch(arr, target):
#   if len(arr) == 0: return False
#   else:
#     mid = len(arr) // 2
#     if arr[mid] == target: return True
#     else:
#       if target < arr[mid]: return binarySearch(arr[:mid], target)
#       else: return binarySearch(arr[mid + 1:], target)
# print(binarySearch(sorted(ls), tar))

# def bubble_sort(arr):
#   for x in range(len(arr) - 1):
#     for y in range(len(arr) - x - 1):
#       slow, fast = arr[y],  arr[y + 1]
#       if slow > fast: arr[y], arr[y + 1] = fast, slow
#   return arr
# print(bubble_sort(ls))

# def selection_sort(arr):
#     for x in range(len(arr) - 1):
#         minIndex = x
#         for y in range(x, len(arr)):
#             if arr[y] < arr[minIndex]: minIndex = y
#         arr[x], arr[minIndex] = arr[minIndex], arr[x]
#     return arr
# print(selection_sort(ls))


def insertion_sort(arr):
    pass


def shell_sort(arr):
    pass


# def merge_sort(arr):
#     # Base Case
#     if len(arr) <= 1:
#         return arr
#     # Recursive Case
#     else:
#         mid = len(arr) // 2
#         left = arr[:mid]
#         right = arr[mid:]
#         return merge_sorted_arrays(merge_sort(left), merge_sort(right))

# def merge_sorted_arrays(left, right):
#     result = []
#     while len(left) and len(right):
#         if left[0] < right[0]:
#             result.append(left[0])
#             left.pop(0)
#         else:
#             result.append(right[0])
#             right.pop(0)
#     result += left + right
#     return result

# print(merge_sort(ls))


def quick_sort(arr):
    pass