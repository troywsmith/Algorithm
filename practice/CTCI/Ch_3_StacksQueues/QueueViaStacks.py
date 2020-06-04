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

    def size(self):
        return len(self.items)


class MyQueue:
    def __init__(self):
        self.stackNewest = Stack()
        self.stackOldest = Stack()

    def size(self):
        return self.stackNewest.size() + self.stackOldest.size()

    def enqueue(self, item):
        self.stackNewest.push(item)

    def shiftStacks(self):
        if self.stackOldest.isEmpty():
            while not self.stackNewest.isEmpty():
                self.stackOldest.push(self.stackNewest.pop())

    def peek(self):
        self.shiftStacks()
        return self.stackOldest.peek()

    def dequeue(self):
        self.shiftStacks()
        return self.stackOldest.pop()

    def isEmpty(self):
        return self.stackNewest.items == [] and self.stackOldest.items == []
