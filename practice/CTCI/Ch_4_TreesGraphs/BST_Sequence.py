class Node():
    """
    Binary Search Tree
    """

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

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


def bst_sequence(bst):
    return bst_sequence_partial([], [bst])


def bst_sequence_partial(partial, subtrees):

    # Return results if no more subtrees in current node
    if not len(subtrees):
        return [partial]

    sequences = []

    # For each subtree possibility, add a sequence
    for i, node in enumerate(subtrees):

        next_partial = partial + [node.data]
        next_substrees = subtrees[:i] + subtrees[i+1:]

        # Add left subtree data if available
        if node.left:
            next_substrees.append(node.left)

        # Add right subtree data if available
        if node.right:
            next_substrees.append(node.right)

        # Recurse with next sequence
        sequences += bst_sequence_partial(next_partial, next_substrees)

    return sequences


if __name__ == '__main__':

    bst = Node(7)
    arr = [4, 5, 9]

    for num in arr:
        bst.insert(num)

    combos = bst_sequence(bst)

    for combo in combos:
        print(combo)
