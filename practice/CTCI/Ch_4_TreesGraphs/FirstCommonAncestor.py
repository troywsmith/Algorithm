class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.data)
        if self.right:
            self.right.inorderTraversal()

    def depth(self):
        height = 0
        node = self
        while node:
            height += 1
            node = node.parent
        return height


def firstCommonAncestor(p, q):
    """
    Questions:
    - Do the nodes have links to their parents?

    Steps:
    # Get height of p
    # Get height of q
    # Move the longer one to the height of the shorter one
    # Traverse up until they equal
    # If they do not equal return False

    Time Complexity: O(d) where d is the depth of the tree
    Space Complexity: O(1)
    """
    # Get difference of heights between p and 1
    delta = abs(p.depth() - q.depth())

    # Determine the nodes with the shorter and longer heights
    shorter, longer = (p, q) if delta < 0 else (q, p)

    # Move the longer one to the height of the shorter one
    for _ in range(abs(delta)):
        longer = longer.parent

    # Traverse up until they equal
    while shorter and longer:
        if shorter == longer:
            return shorter
        shorter = shorter.parent
        longer = longer.parent

    # If they do not equal return False
    return False


if __name__ == '__main__':

    # Root Node
    root = Node('a')

    # Left Subtree
    root.left = Node('b')
    root.left.parent = root
    root.left.left = Node('c')
    root.left.left.parent = root.left
    root.left.right = Node('d')
    root.left.right.parent = root.left
    root.left.left.left = Node('h')
    root.left.left.left.parent = root.left.left

    # Right Subtree
    root.right = Node('e')
    root.right.parent = root
    root.right.left = Node('f')
    root.right.left.parent = root.right
    root.right.right = Node('g')
    root.right.right.parent = root.right

    ans = firstCommonAncestor(root.left.left, root.right.left)
    print(ans.data)
