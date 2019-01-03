from collections import deque


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


def DepthLists(root):
    """
    BFS but capturing and returning each level of the tree as deques
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    levels = []
    l1 = deque([root.data])
    levels.append(l1)

    thislevel = [root]
    while thislevel:

        nextlevel = []
        level = deque()
        for n in thislevel:

            if n.left:
                nextlevel.append(n.left)
                level.append(n.left.data)

            if n.right:
                nextlevel.append(n.right)
                level.append(n.right.data)

        if level:
            levels.append(level)

        thislevel = nextlevel

    return levels


if __name__ == '__main__':
    root = Node(4)
    root.insert(2)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(5)
    root.insert(7)
    levels = DepthLists(root)
    for level in levels:
        print(level)