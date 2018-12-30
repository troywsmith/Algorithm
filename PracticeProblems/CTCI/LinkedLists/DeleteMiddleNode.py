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



def deleteMiddleNode(node):
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next
    else:
        return False