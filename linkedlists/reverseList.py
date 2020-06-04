class LinkedList:

    def __init__(self, val):
        self.val = val
        self.next = None


def printList(head):
    hi = head
    while hi:
        print(hi.val)
        hi = hi.next
    print('')


def reverseList(head):

    prevNode = None
    currNode = head

    while currNode:
        nextNode = currNode.next
        currNode.next = prevNode
        prevNode = currNode
        currNode = nextNode

    head = prevNode
    return head


if __name__ == '__main__':

    # Create Linked List
    head = LinkedList(1)
    node = head
    vals = [2, 3, 4, 5, 6, 7, 8, 9]
    for val in vals:
        node.next = LinkedList(val)
        node = node.next

    printList(head)

    # Reverse List
    head = reverseList(head)

    printList(head)
