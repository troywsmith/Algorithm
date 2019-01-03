class Node():
    """
    Binary Tree Node
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def ValidateBST(root, minVal, maxVal):
    """
    Time Complexity: O(N)
    Space Complexity: O(log N)
    """
    if not root:
        return True

    if minVal and root.data <= minVal:
        return False

    if maxVal and root.data > maxVal:
        return False

    return ValidateBST(root.left, minVal, root.data) and ValidateBST(root.right, root.data, maxVal)


if __name__ == '__main__':
    root = Node(4)

    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)

    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(7)

    print('Checking if input is a Binary Search Tree')
    ans = ValidateBST(root, None, None)
    print(ans)