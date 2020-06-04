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


list1 = Node(1)
list1.appendToTail(5)
list1.appendToTail(3)
list1.appendToTail(8)

list2 = Node(8)
list2.appendToTail(7)
list2.appendToTail(9)

intersectList = Node(4)
intersectList.appendToTail(3)

end = intersectList
node1 = list1
while node1.next != None:
    node1 = node1.next
node1.next = end

end = intersectList
node1 = list2
while node1.next != None:
    node1 = node1.next
node1.next = end

list1.printNodeList()
list2.printNodeList()


def findIntersectingNode(list1, list2):
    """"
    Time Complexity: O(A + B)
    Space Complexity: O(1)
    """
    tail1 = list1
    n1 = 0
    while tail1:
        n1 += 1
        tail1 = tail1.next
    tail2 = list2
    n2 = 0
    while tail2:
        n2 += 1
        tail2 = tail2.next

    # if last nodes arent the same, they do not intersect
    if tail1 != tail2:
        return False

    # move faster pointer
    fast = list1 if n1 > n2 else list2
    slow = list1 if n1 < n2 else list2
    for _ in range(abs(n1-n2)):
        fast = fast.next

    # move pointers simultaneously, comparing each time
    while fast:
        if slow == fast:
            return slow
        slow = slow.next
        fast = fast.next

    return False


interNode = findIntersectingNode(list1, list2)
print(interNode.val)
