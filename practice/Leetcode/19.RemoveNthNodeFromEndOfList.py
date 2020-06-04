class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        # Two pointers (one starting at 0, the other at n)
        # Move pointers one by one
        # Stop when the fast pointer hits the end
        # remove the node at slow pointer
        # Time Complexity: O(L)
                
        slow, fast = head, head
        for _ in range(n):
            fast = fast.next
        
        if not fast:
          return head.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next
        return head