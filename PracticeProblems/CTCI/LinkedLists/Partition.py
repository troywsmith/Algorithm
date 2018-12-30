class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def appendToTail(self, val):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        end = Node(val)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def printNodeList(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        nodes = []
        n = self
        while n:
            nodes.append(n.val)
            n = n.next
        print(nodes)



def partitionList(node, x):
    leftHead = None
    leftTail = None
    rightHead = None
    rightTail = None
    while node:
        next = node.next
        node.next = None
        if node.val < x:
            if not leftHead:
                leftHead = node
                leftTail = leftHead
            else:
                leftTail.next = node
                leftTail = node
        else:
            if not rightHead:
                rightHead = node
                rightTail = rightHead
            else:
                rightTail.next = node
                rightTail = node
        node = next
    if not leftHead:
        node = rightHead
    leftTail.next = rightHead
    node = leftHead