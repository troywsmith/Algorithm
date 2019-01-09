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

    def reverseAndClone(self, node):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        head = None
        while node:
            n = Node(node.val)
            n.next = head
            head = n
            node = node.next
        return head

    def isEqual(self, one, two):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        while one and two:
            if one.val != two.val:
                return False
            one = one.next
            two = two.next
        return one == None and two == None

    def isPalindrome(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        reversedList = self.reverseAndClone(self)
        return self.isEqual(self, reversedList)


ll = Node('r')
ll.appendToTail('a')
ll.appendToTail('c')
ll.appendToTail('e')
ll.appendToTail('c')
ll.appendToTail('a')
ll.appendToTail('r')
ll.printNodeList()
print(ll.isPalindrome())