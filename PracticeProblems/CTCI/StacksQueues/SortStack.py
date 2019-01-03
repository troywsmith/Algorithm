class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]


def sortStack(s):
    r = Stack()

    while not s.isEmpty():

      tmp = s.pop()
      while not r.isEmpty() and r.peek() > tmp:

        s.push(r.pop())
      
      r.push(tmp)
    
    while not r.isEmpty():
      s.push(r.pop())

s = Stack()
s.push(4)
s.push(3)
s.push(7)
print(s.items)
sortStack(s)
print(s.items)