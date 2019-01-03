class Node():
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

    def search(self, val):
        if val < self.data:
            if self.left:
                self.left.search(val)
        elif val > self.data:
            if self.right:
                self.right.search(val)
        else:
            print(str(val) + ' is found')