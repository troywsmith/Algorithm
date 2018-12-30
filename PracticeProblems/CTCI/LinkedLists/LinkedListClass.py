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

    def deleteNode(self, head, val):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = head
        if n.val == val:
            return head.next
        while n.next != None:
            if n.next.val == val:
                n.next = n.next.next
                return head
            n = n.next
        return head

    def printNodeList(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        n = self
        while n:
            print(n.val)
            n = n.next

    def removeDups(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        prev = None
        n = self
        while n:
            if n.val in seen:
                prev.next = n.next
            else:
                seen.add(n.val)
                prev = n
            n = n.next

    def findKthToLast(self, k):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = self
        fast = self
        for _ in range(k):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        return slow


head = Node(1)
nodes = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6, 7, 8, 9]
for x in range(1, len(nodes)):
    head.appendToTail(nodes[x])
head.removeDups()
kthToLast = head.findKthToLast(4)
print(kthToLast.val)