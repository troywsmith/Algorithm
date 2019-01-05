from collections import deque


class Node():
    """
    Binary Search Tree
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


def check_subtree(t2, t1):
    if t1 is None or t2 is None:
        return False
    if t1.val == t2.val:  # potential subtree
        if subtree_equality(t2, t1):
            return True
    return check_subtree(t2, t1.left) or check_subtree(t2, t1.right)


def subtree_equality(t2, t1):
    if t2 is None and t1 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t2.val == t1.val:
        return subtree_equality(t2.left, t1.left) and subtree_equality(t2.right, t1.right)
    return False


if __name__ == '__main__':
    T1 = Node(10)
    T1.left = Node(8)
    T1.left.left = Node(7)
    T1.left.right = Node(9)

    T1.right = Node(12)
    T1.right.left = Node(11)
    T1.right.right = Node(13)

    T2 = Node(12)
    T2.left = Node(11)
    T2.right = Node(13)

    # T1.right = T2

    T1.inorderTraversal()
    print(' ')
    T2.inorderTraversal()

    ans = check_subtree(T1, T2)
    print(ans)