class LFUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.data = {}
        self.order = []   

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.data.keys():
          self.order.append(key)
          print(self.order)
          return self.data[key]
        else:
          return -1
      

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # EVICTION PROCESS
        if len(self.data.keys()) >= self.capacity:
          evicted = self.order[0]
          self.order = self.order[1:]
          print(self.order)
          print('evict', evicted)

        else:
          self.data[key] = value
          self.order.append(key)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# LFUCache 
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
print(cache.get(3))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))
print(cache.data)