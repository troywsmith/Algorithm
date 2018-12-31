class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class SetOfStacks:
    def __init__(self):
        self.stacks = Stack()
        self.currentStack = Stack()

    def push(self, item):
        if len(self.currentStack.items) == 3:
            self.stacks.push(self.currentStack)
            self.currentStack = Stack()
            self.currentStack.push(item)
        else:
            self.currentStack.push(item)

    def pop(self):
        if self.currentStack:
            return self.currentStack.pop()
        else:
            return self.stacks.pop()


ss = SetOfStacks()
ss.push(1)
ss.push(2)
ss.push(3)
for stack in ss.stacks.items:
    print(stack.items)
print(ss.pop())