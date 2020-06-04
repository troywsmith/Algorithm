def nth_to_last_node(n, head):

  left = head
  right = head

  for i in range(n-1):
    if not right.nextnode:
      raise LookupError('Error: n is larger than the linked list')
    
    right = right.nextnode

  while right.nextnode:
    left = left.nextnode
    right = right.nextnode

  return left

class Node:
  def __init__(self, value):
    self.value = value
    self.nextnode  = None

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a) 
print(target_node.value)