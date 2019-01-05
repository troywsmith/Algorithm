from collections import deque
import random


class Node():
    """
    Binary Tree
    """

    def __init__(self, data=None, left=None, right=None):
        self.val = data
        self.left = left
        self.right = right

    def inorderTraversal(self):
        if self.left:
            self.left.inorderTraversal()
        print(self.val)
        if self.right:
            self.right.inorderTraversal()

    def getRandomNode(self):
        """
        Solution: Breadth-First Search
        Time Complexity: O(n) where n is the number of nodes in the tree
        """
        nodes = []

        # BFS to get all the nodes in the tree
        queue = deque()
        queue.append(self)
        while queue:
            node = queue.popleft()
            nodes.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        for node in nodes:
            print(node.val)

        # Return a random node in the list of all the nodes
        return nodes[random.randint(0, len(nodes)-1)]


if __name__ == '__main__':
    T1 = Node(10)
    T1.left = Node(8)
    T1.left.left = Node(7)
    T1.left.right = Node(9)
    T1.right = Node(12)
    T1.right.left = Node(11)
    T1.right.right = Node(13)

    ans = T1.getRandomNode()
    print(ans.val)
