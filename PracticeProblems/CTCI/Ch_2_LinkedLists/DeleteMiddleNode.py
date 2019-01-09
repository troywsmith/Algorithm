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

    def deleteNode(self, node):
        """
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            return False


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
nodes = [n1, n2, n3, n4, n5]

n = n1
for node in nodes:
  n.next = node
  n = n.next
  print(n.val)

n1.printNodeList()
n1.deleteNode(n3)
n1.printNodeList()