class Node():

    def __init__(self, val):
        self.val = val
        self.next = None

    def appendToTail(self, val):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        end = Node(val)
        n = self
        while n.next != None:
            n = n.next
        n.next = end

    def printNodeList(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        nodes = []
        n = self
        count = 0
        while n:
            nodes.append(n.val)
            n = n.next
            count += 1
            if count > 10:
                break
        print(nodes)


ll = Node('A')
ll.appendToTail('B')

HahNode = Node('C')
HahNode.appendToTail('D')
HahNode.appendToTail('E')
HahNode.appendToTail('F')

ll.next.next = HahNode
ll.printNodeList()

n = ll
while n.next:
    n = n.next
n.next = HahNode
ll.printNodeList()

def DetectLoop(ll):
    """"
    Time Complexity: O()
    Space Complexity: O()
    """
    node = ll
    seen = set()
    while node:
        if node in seen:
            return node
        else:
            seen.add(node)
        node = node.next
    return False

badNode = DetectLoop(ll)
print(badNode)
print(badNode.val)