class Node():
    """
    Binary Search Tree
    """

    def __init__(self, data):
        self.data = data
        self.qty = 1
        self.left = None
        self.right = None
        self.left_size = 0

    def track(self, data):
        if self.data:
            if data < self.data:
                if not self.left:
                    self.left = Node(data)
                    self.left_size += 1
                else:
                    self.left.track(data)
            elif data > self.data:
                if not self.right:
                    self.right = Node(data)
                else:
                    self.right.track(data)
            else:
                self.qty += 1

    def search(self, val):
        if val < self.data:
            if self.left:
                self.left.search(val)
        elif val > self.data:
            if self.right:
                self.right.search(val)
        else:
            print(str(val) + ' is found')

    def traverse(self):
        if self.left:
            self.left.traverse()
        print(self.data, self.qty, self.left_size, )
        if self.right:
            self.right.traverse()


if __name__ == '__main__':

    int_dict = Node(5)
    int_dict.track(1)
    int_dict.track(4)
    int_dict.track(4)
    int_dict.track(5)
    int_dict.track(9)
    int_dict.track(7)
    int_dict.track(13)
    int_dict.track(3)
    # int_dict.print_ranks()
    int_dict.traverse()
