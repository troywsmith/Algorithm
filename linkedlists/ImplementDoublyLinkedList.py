class Node(object):
  def __init__(self, value):
    self.prev_node = None
    self.value = value
    self.next_node = None

a = Node(1)
b = Node(2)
c = Node(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

print(b.prev_node.value)
print(a.next_node.value)
print(c.value)