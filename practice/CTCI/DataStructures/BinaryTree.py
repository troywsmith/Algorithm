class Node():
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

    def insertLeft(self, data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insertLeft(data)
        else:
            self.data = data

    def insertRight(self, data):
        if self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insertRight(data)
        else:
            self.data = data


if __name__ == '__main__':
    root = Node(4)
    left = True
    for i in range(1, 21, 2):
        print(left, i)
        if left:
            root.insertLeft(i)
        else:
            root.insertRight(i)
        left = not left
    root.inorderTraversal()
