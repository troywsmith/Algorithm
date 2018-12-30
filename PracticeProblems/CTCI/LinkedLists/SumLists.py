class Node():

    def __init__(self, data=None):
        self.val = data
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
            if n.val:
                nodes.append(n.val)
            n = n.next
        print(nodes)

    def sumLists(self, list2):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        p = self
        q = list2
        sum_list = Node()
        carry = 0
        while p or q:
            if not p:
                i = 0
            else:
                i = p.val
            if not q:
                j = 0
            else:
                j = q.val
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.appendToTail(remainder)
            else:
                carry = 0
                sum_list.appendToTail(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.printNodeList()


list1 = Node(5)
list1.appendToTail(6)
list1.appendToTail(3)
list2 = Node(8)
list2.appendToTail(4)
list2.appendToTail(2)

print(365 + 248)
list1.sumLists(list2)