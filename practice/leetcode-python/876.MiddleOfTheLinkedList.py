"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.
If there are two middle nodes, return the second middle node.
"""

def middleNode(head):
  slow = head
  fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
  return slow

print(middleNode([1,2,3,4,5]))