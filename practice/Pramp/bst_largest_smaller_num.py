def find_largest_smaller_val(root, num):

    # Store best answer so far (largest number we have seen that is smaller than num)
    result = -1

    node = root
    # Traverse tree
    while node:

        # If nodes key is < num: store key in result and move to the right
        if node.key < num:
            result = max(result, node.key)
            node = node.right

        # If nodes key is > num: go left and dont set result
        else:
            node = node.left

    # Return result
    return result