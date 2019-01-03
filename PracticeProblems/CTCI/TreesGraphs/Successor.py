class TreeNode():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def insert(self, data):
        newNode = TreeNode(data)
        newNode.parent = self

        if newNode.data <= self.data:
            if self.left:
                self.left.insert(data)
            else:
                self.left = newNode

        elif newNode.data > self.data:
            if self.right:
                self.right.insert(data)
            else:
                self.right = newNode


def LeftmostChild(node):
    if not node:
        return None

    while node.left:
        node = node.left

    return node


def FindSuccessor(node):
    """
    Finds the next node in an inorder traversal
    """
    if not node:
        return None

    if node.right:
        return LeftmostChild(node.right)

    else:
        q = node
        parent = q.parent

        while parent and parent.left != q:
            q = parent
            parent = parent.parent

        return parent


if __name__ == '__main__':
    root = TreeNode(4)
    root.insert(2)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(7)

    n = root.left.right
    print(n.data)
    ans = FindSuccessor(n)
    if ans:
        print(ans.data)
    else:
        print('No greater node, must be the rightmost node')
