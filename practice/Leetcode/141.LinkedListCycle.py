# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        node = head
        seen = set()
        while node:
            if node in seen:
                return True
            else:
                seen.add(node)
            node = node.next
        return False