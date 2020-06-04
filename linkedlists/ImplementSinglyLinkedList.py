class Node(object):
  def __init__(self, value):
    self.value = value
    self.nextnode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c

# 1
print(a.value)

# 2
print(a.nextnode.value)
print(b.value)

# 3
print(b.nextnode.value)
print(c.value)