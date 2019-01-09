"""
Question: Generate a number not in input file
Input: file w/ 4 billion nonnegative integers
Output: unique number
Contraints: Only have 1GB of memory
"""

# def generate_number(int_file):
#     """
#     We can just save the biggest number and return that number + 1
#     """
#     max_num = 1
#     for num in int_file:
#         max_num = max(max_num, num)
#     return max_num+1


from collections import defaultdict


def generate_number(int_file):
    """
    Binary Method
    """
    bin_nums = defaultdict()

    # Create a hash table that stores the size of each numbers binary version
    for num in int_file:
        bin_ver_len = len(bin(num))
        bin_nums[bin_ver_len] = num

    # Return the largest numbers of bits plus 1
    lengths = bin_nums.keys()
    size_largest_bin_num = lengths[len(lengths)-1]
    new_num_bin = '1' + ('0' * size_largest_bin_num)
    new_num = int(new_num_bin, 2)

    return new_num


nums = [124, 124, 14, 124, 12, 4, 14, 124, 1, 4, 1252, 6, 4, 3,
        4563, 7, 357, 3, 7, 357, 3, 734, 57, 347, 3, 7345, 73473, 7, 100000000000000000000000000000000]
print(generate_number(nums))
