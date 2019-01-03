class Node():
    """
    Binary Search Tree
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data


def ConvertSortedArrToMinimalBST(arr):
    """
    Time Complexity: O(n)
    """
    # If there are no elements in arr, return false
    if not arr:
        return None

    # Insert middle item
    mid = len(arr) // 2
    n = Node(arr[mid])

    # Do the same for the left and right halves
    n.left = ConvertSortedArrToMinimalBST(arr[:mid])
    n.right = ConvertSortedArrToMinimalBST(arr[mid+1:])
    return n


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    tree = ConvertSortedArrToMinimalBST(arr)

    # A utility function to print the preorder traversal of the BST
    def preOrder(node):
        if not node:
            return
        print(node.data)
        preOrder(node.left)
        preOrder(node.right)

    preOrder(tree)