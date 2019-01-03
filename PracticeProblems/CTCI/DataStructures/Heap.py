class MinHeap():
    def __init__(self):
        self.heap = []
        self.size = 0

    def heapify(self):
        pass

    def insert(self, data):
        """
        Time Complexity: O(log n)
        """
        self.heap.append(data)
        self.size += 1
        self.heapify(self.size)

    def delete(self, node):
        """
        Time Complexity: O(log n)
        """
        pass

    def extractMin(self):
        """
        Time Complexity: O(log n)
        """
        pass

