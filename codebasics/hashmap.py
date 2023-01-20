# Day 5 - HASH TABLE --------------

class HashTable:
  def __init__(self):
    self.MAX = 100
    self.arr = [[] for i in range(self.MAX)]

  def get_hash(self, key):
    h = 0
    for char in key:
      h += ord(char)
    return h % self.MAX

  # change __setitem__ to add()
  def __setitem__(self, key, val):
    h = self.get_hash(key)
    found = False
    # find out if key exists
    # enumerate is a function used to iterate throuh an array
    for idx, element in enumerate(self.arr[h]):
      if len(element)==2 and element[0]==key:
        self.arr[h][idx] = (key, val)
        found = True
        break
      # if key does not exist in that linked list
    if not found:
      self.arr[h].append((key, val))
  
  # change __getitem__ to get()
  def __getitem__(self, key):
    h = self.get_hash(key)
    # return self.arr[h]
    for element in self.arr[h]:
      if element[0] == key:
        return element[1]

  def __delitem__(self, key):
    h = self.get_hash(key)
    # self.arr[h] = []
    for index, element in enumerate(self.arr[h]):
      if element[0] == key:
        del self.arr[h][index]

  # HASH TABLE PRACTICE
  # 1. What was the average temperature in first week of Jan.
  # def average_temp(self, amount):
  #   # add all items up and divide by the amount of items there are
  #   for element in self.arr:
  #     if element != []:
  #       total = element[0][1]
  #       for i in range(total):
  #         new_total = sum(i)
  #         print(new_total)
        # print(type(total))
        # print(total)
        # print(element[0][1])
        


  # 2. What was the maximum temperature in first 10 days of Jan.
  def max_temp(self):
    pass

# RETURNS ---
t = HashTable()
# t.add('march 6', 130) # adds to the array based on hash number.
# print(t.get('march 6')) # returns 130

# t['march 6'] = 120 # also adds to the array
# t['march 6'] = 78
# t['march 8'] = 67
# t['march 9'] = 4
# t['march 17'] = 459

# print(t.arr) # retruns the hashmap
# del t['march 17']
# print(t['march 17'])
# print(t.arr) # retruns the hashmap

# RETURNS HASH TABLE PRACTICE QUESTIONS
# t['Jan 1'] = 27
# t['Jan 2'] = 31
# t['Jan 3'] = 23
# t['Jan 4'] = 34
# t['Jan 5'] = 37
# t['Jan 6'] = 38
# t['Jan 7'] = 29
# t['Jan 8'] = 30
# t['Jan 9'] = 35
# t['Jan 10'] = 30

# print(t.arr)
# t.average_temp(7)

# Creating a custom HashTable Data Structure ------

class HashTable(object):
  def __init__(self, size=10):
    self.num_elements = 0 # how many entries we put into the hashtable, collisions, if num_elements > size then resize
    self.data = [0] * size # list gets initialized
    # self.data = {} # built in python dictionary 
    self.size = len(self.data)
    print(self.data)

# our_hash_table = HashTable() # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]



