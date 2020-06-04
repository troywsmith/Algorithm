class MinStack:

    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin == None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(5)
    print(obj.q)
    obj.push(2)
    print(obj.q)
    obj.push(-3)
    print(obj.q)
    obj.push(4)
    print(obj.q)
    obj.pop()
    print(obj.q)
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_4)
    print(obj.q)
