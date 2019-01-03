
class BST_Node():
    """
    Binary Search Tree
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.data)
        if self.right:
            self.right.inorderTraversal()

    def preorderTraversal(self):
        print(self.data)
        if self.left:
            self.left.inorderTraversal()
        if self.right:
            self.right.inorderTraversal()

    def postorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        if self.right:
            self.right.inorderTraversal()
        print(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = BST_Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if not self.right:
                    self.right = BST_Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def search(self, val):
        if val < self.data:
            if self.left:
                self.left.search(val)
        elif val > self.data:
            if self.right:
                self.right.search(val)
        else:
            print(str(val) + ' is found')


def checkHeight(root):
    # Base Case
    if root == None:
        return -1

    leftHeight = checkHeight(root.left)
    if leftHeight == float('-inf'):
        return float('-inf')

    rightHeight = checkHeight(root.right)
    if rightHeight == float('-inf'):
        return float('-inf')

    heightDiff = leftHeight - rightHeight

    if abs(heightDiff) > 1:
        return float('-inf')
    else:
        return max(leftHeight, rightHeight) + 1


def checkBalanced(root):
    """
    Checks if a binary tree root is balanced
    Balanced: the diff between heights of the left and right subroot is 0 or 1
    Time Complexity: O(N)
    Space Complexity: O(H)
    """
    return checkHeight(root) != float('-inf')


if __name__ == '__main__':
    root = BST_Node(5)
    root.insert(1)
    root.insert(6)
    root.insert(4)
    root.insert(8)
    answer = checkBalanced(root)
    if answer:
        print('Tree is balanced')
    else:
        print('Tree is NOT balanced')
