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


def removeDups(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    prev = None
    n = head
    while n:
        if n.val in seen:
            prev.next = n.next
        else:
            seen.add(n.val)
            prev = n
        n = n.next