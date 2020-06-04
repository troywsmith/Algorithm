class HashTable(object):

  def __init__(self, size):
    self.size = size
    self.slots = [None] * self.size
    self.data = [None] * self.size

  def put(self, key, data):
    
    hashvalue = self.hashfunction(key, len(self.slots))

    if self.slots[hashvalue] == None:
      self.slots[hashvalue] = key
      self.data[hashvalue] = data

    else:

      if self.slots[hashvalue] == key:
        self.data[hashvalue] = data

      else:
        nextslot = self.reshash(hashvalue, len(self.slots))

        while self.slots[nextslot] != None and self.slots[nextslot] != key:
          nextslot = self.reshash(nextslot, len(self.slots))

        if self.slots[nextslot] == None:
          self.slots[nextslot] = key
          self.data[nextslot] = data
          
        else:
          self.data[nextslot] = data

  def hashfunction(self, key, size):
    return key % size

  def reshash(self, oldhash, size):
    return (oldhash + 1) % size

  def get(self, key):
    startslot = self.hashfunction(key, len(self.slots))
    data = None
    stop = False
    found = False
    position = startslot

    while self.slots[position] != None and not found and not stop:

      if self.slots[position] == key:
        found == True
        data = self.data[position]

      else:
        position = self.reshash(position, len(self.slots))
        if position == startslot:
          stop = True
    
    return data

  def __getitem__(self, key):
    return self.get(key)

  def __setitem__(self, key, data):
    return self.put(key, data)

h = HashTable(5)

h.put(1, 'one')
h.put(2, 'two')
h.put(3, 'three')

print(h.get(1))