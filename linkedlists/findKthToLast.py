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


def findKthToLast(head, k):

    slow = fast = head
    for _ in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow


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
    k = 3
    kth = findKthToLast(head, k)
    print(kth.val)
