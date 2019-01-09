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


class Tower:
    def __init__(self, i):
        self.disks = Stack()
        self.index = i

    def add(self, disk):
        if not self.disks.isEmpty() and self.disks.peek() < disk:
            print('cannot add disk {} to {}'.format(disk, self.disks.items))
        else:
            self.disks.push(disk)

    def moveTopTo(self, destination_tower):
        top = self.disks.pop()
        destination_tower.add(top)

    def moveDisks(self, n, destination, buffer):
        if n > 0:
            self.moveDisks(n-1, buffer, destination)
            self.moveTopTo(destination)
            buffer.moveDisks(n-1, destination, self)


def printTowers(towers):
    for i, tower in enumerate(towers):
        print(str(i) + ': ' + str(tower.disks.items))
    print(' ')


if __name__ == '__main__':

    towers = [Tower(1), Tower(2), Tower(3)]

    disks = [3, 2, 1]
    n = len(disks)
    for num in disks:
        towers[0].disks.push(num)
    
    printTowers(towers)

    towers[0].moveDisks(n, towers[2], towers[1])

    printTowers(towers)

else:
    print('Importing: Towers of Hanoi Algorithm')