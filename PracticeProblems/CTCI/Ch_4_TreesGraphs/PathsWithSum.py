from collections import deque


class Node():
    """
    Binary Tree
    """

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def FindPathsWithSum(root, target_sum):
    valid_paths = {}
    return FindPathsHelper(root, target_sum, 0, valid_paths)


def FindPathsHelper(node, target_sum, running_sum, valid_paths):
    if not node:
        return 0

    running_sum = running_sum + node.data

    if running_sum in valid_paths:
        valid_paths[running_sum] += 1
    else:
        valid_paths[running_sum] = 1

    count = int(running_sum == target_sum) + valid_paths.get(running_sum - target_sum, 0) + FindPathsHelper(node.left,
                                                                                                            target_sum, running_sum, valid_paths) + FindPathsHelper(node.right, target_sum, running_sum, valid_paths)
    valid_paths[running_sum] -= 1
    return count


if __name__ == '__main__':
    T1 = Node(1)
    T1.left = Node(3)
    T1.left.left = Node(5)
    T1.left.right = Node(3)
    T1.right = Node(4)
    T1.right.left = Node(2)
    T1.right.right = Node(1)
    ans = FindPathsWithSum(T1, 6)
    print(ans)
