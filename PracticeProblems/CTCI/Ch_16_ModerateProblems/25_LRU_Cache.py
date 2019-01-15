from collections import defaultdict


class Node:

    def __init__(self, word, time):
        self.word = word
        self.time = time
        self.prev = None
        self.next = None


class Cache:

    def __init__(self):
        self.items = defaultdict()
        self.head = None
        self.tail = None
        self.size = 0
        self.max_size = 4

    def add_item(self, word, time):

        # Evict item if max size is reached
        while self.size >= self.max_size:
            self.evict_item()

        # Create new linked list node for word
        node = Node(word, time)

        # Add new node to head of list
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node

        else:
            self.head = node
            self.tail = node

        # Add item to hash table
        self.items[word] = node

        # Increment size
        self.size += 1

    def retrieve_word(self, word):

        # Move item being retreived to head of linked list
        item_node = self.items[word]
        item_node.prev = self.head
        self.head = item_node
        return item_node

    def evict_item(self):

        next_tail = self.tail.prev
        self.tail = next_tail
        self.size -= 1

    def print_cache(self):

        print(' ')
        print('Hash Table:')
        for item, node in self.items.items():
            print('{} : {}'.format(item, node.time))

        print(' ')
        print('Linked List:')
        node = self.head
        print('H: {} - {}'.format(node.time, node.word))
        node = node.next
        while node.next:
            print('M: {} - {}'.format(node.time, node.word))
            node = node.next
        print('T: {} - {}'.format(node.time, node.word))


if __name__ == '__main__':
    cache = Cache()
    cache.add_item('hi', 1)
    cache.add_item('yo', 2)
    cache.add_item('sup', 3)
    cache.add_item('head', 4)
    cache.add_item('uh oh', 5)
    cache.print_cache()
