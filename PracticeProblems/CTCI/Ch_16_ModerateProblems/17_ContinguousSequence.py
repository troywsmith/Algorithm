
# def find_largest_sum(arr):
#     """
#     Time Complexity: O(n^2)
#     Space Complexity: O(1)
#     """

#     # Store max_sum and current sum
#     max_sum = 0

#     # Iterate through array
#     for i in range(len(arr)):

#         curr_sum = arr[i]

#         # If element alone is greater than max, set it to max
#         max_sum = max(max_sum, curr_sum)

#         # Get subarray sum
#         for j in range(i+1, len(arr)):

#             curr_sum += arr[j]
#             print(arr[i], arr[j], curr_sum)

#             # If current sum is greater than max, set it to max
#             max_sum = max(max_sum, curr_sum)

#     # Return max sum
#     return max_sum


def find_largest_sum(arr):
    """
    Time Complexity:
    Space Complexity:
    """

    curr_sum = 0
    max_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
        curr_sum = 0 if curr_sum < 0 else curr_sum

    return max_sum


if __name__ == '__main__':
    arr = [2, -8, 3, -2, 4, -10]
    print(find_largest_sum(arr))
