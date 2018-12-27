def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    node1, node2 = l1, l2
    result = []

    while node1 and node2:
        if node1.val < node2.val:
            result.append(node1.val)
            node1 = node1.next
        else:
            result.append(node2.val)
            node2 = node2.next

    while node1:
        result.append(node1.val)
        node1 = node1.next

    while node2:
        result.append(node2.val)
        node2 = node2.next

    return result