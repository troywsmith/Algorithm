class ThreeStacks:
    def __init__(self, size):
        self.size = size
        self.items = [None] * 3 * size
        self.top = [0,0,0]
 
    def push(self, data, stackNum):
       if stackNum < 3 and stackNum >= 0:
           self.items[stackNum * self.size + self.top[stackNum]] = data
           self.top[stackNum] += 1
 
    def pop(self, stackNum):
        if stackNum < 3 and stackNum >= 0:
            temp = self.items[self.top[stackNum]]
            self.items[self.top[stackNum]] = None
            self.top[stackNum] -= 1
            return temp
 
    def stackSize(self, stackNum):
         return self.top[stackNum]

stacks = ThreeStacks(1)
stacks.push(1, 1)
stacks.push(1, 1)
stacks.push(1, 2)

print(stacks.items)