def addTwoNumbers(l1, l2):
    integer1 = str(l1.val)
    node = l1.next
    while node != None:
        integer1 += str(node.val)
        node = node.next

    integer2 = str(l2.val)
    node = l2.next
    while node != None:
        integer2 += str(node.val)
        node = node.next

    reversed_sum = str(int(integer1[::-1]) + int(integer2[::-1]))[::-1]
    result = [int(char) for char in reversed_sum]
    return result