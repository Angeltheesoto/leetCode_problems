# Repersents an individual element in the node list.
class Node:
  def __init__(self, data=None, next=None):
    self.data = data # data can contain int, num, or complex obj
    self.next = next # Points to the next element

# Linked list class that holds the functions.
class LinkedList:
  # 1. Prepares the new class with a head variable.
  def __init__(self):
    self.head = None # Points to the head of the linked list.
  
  # 2. This function takes the data and inserts it at the beginning of the linked list.
  def insert_at_begining(self, data):
    node = Node(data, self.head)
    self.head = node

  # 3. This function is used to test out the other functions, this is a utility function. This lets us see our linked list data.
  def print(self):
    if self.head is None:
      print("Linked list is empty")
      return
    # if head is not blank..
    itr = self.head
    llstr = ''

    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next

    print(llstr)

  # 4. This function puts the data at the end of the list.
  def insert_at_end(self, data):
    # if head is none have data go to head
    if self.head is None:
      self.head = Node(data, None)
      return
    # else loop through the list from head to the end then add data to the last itr.next
    itr = self.head
    while itr.next:
      itr = itr.next

    itr.next = Node(data, None)

  # 5. This function creates a new linked list. It loops through the items and insert them at the end using the insert_at_end function.
  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)

  # 6. This function gets the length of the items in the linked list with a counter.
  def get_length(self):
    count = 0
    itr = self.head
    while itr:
      count+=1
      itr = itr.next
    return count

  # 7. This function removes an element at a given index.
  def remove_at(self, index):
    if index < 0 or index >= self.get_length():
      # its similar to catch(err) in JavaScript
      raise Exception("Invalid index")
    # If your trying to remove the head of the linked list.
    if index == 0:
      self.head = self.head.next
      return
    # this takes care of all other cases. If the count is before the index to be removed, that index will point to the next.next(two down) to skip over the one to be removed.
    count = 0
    itr = self.head
    while itr:
      if count == index - 1:
        itr.next = itr.next.next
        break
      itr = itr.next
      count += 1

  # 8. This function inserts a value at a specific index while keeping everything the same.
  def insert_at(self, index, data):
    # This is for invalid inputs.
    if index < 0 or index > self.get_length():
      raise Exception("Invalid Index")

    # This is for inserting at beginning
    if index == 0:
      self.insert_at_begining(data)
      return

    # for all other cases, 
    count = 0
    itr = self.head
    while itr:
      # you want to modify the next pointer of the previous element. This way we stop at the previous element
      if count == index - 1:
        # this points the next element to next.
        node = Node(data, itr.next)
        itr.next = node
        break
      # continues the loop of each item
      itr = itr.next
      count += 1

# My Code ---
  def insert_after_value(self, data_after, data_to_insert):
    if self.head is None:
      return
    
    if self.head.data == data_after:
      self.head.next = Node(data_to_insert, self.head.next)
      return

    count = 0
    itr = self.head
    # while itr != None: # This or the one below works to iterate
    while itr:
      # if itr.data != data_after:
      #   raise Exception("No values match.")
      if itr.data == data_after:
        node = Node(data_to_insert, itr.next)
        itr.next = node
        break
      itr = itr.next
      count += 1

  def remove_by_value(self, data):
    if self.head is None:
      return
    
    if self.head.data == data:
      self.head = self.head.next
      return

    count = 0
    itr = self.head
    while itr:
      # if itr.data == data:
      #   self.remove_at(count)
      if itr.next.data == data:
        itr.next = itr.next.next
        break

      itr = itr.next
      count += 1

  def reverseList(self):
    prev = None
    curr = self.head
    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    self.head = prev

# This is a simple loop to go through each element in the linked list.
# itr = self.head
# while itr:
#   itr = itr.next

# In Short: It Allows You to Execute Code When the File Runs as a Script, but Not When It’s Imported as a Module
if __name__ == '__main__':
  ll = LinkedList()
  ll.insert_values([1, 2, 3, 4])
  ll.print()
  # ll.reverseList()
  ll.recursiveReverseList()
  ll.print()


