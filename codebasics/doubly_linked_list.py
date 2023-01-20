class Node:
  def __init__(self, data=None, next=None, prev=None):
    self.data = data
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  # 1. This function is used to test out the other functions, this is a utility function. This lets us see our linked list data.
  def print(self):
    if self.head == None:
      print('The list is empty.')
      return
    itr = self.head
    dllstr = ""
    while itr:
      dllstr += str(itr.data) + '-->'
      itr = itr.next
    print(dllstr)

# inserts one element at the beginning
  def insert_at_beginning(self, data):
    if self.head == None:
      node = Node(data, self.head, None)
      self.head = node
    else:
      node = Node(data, self.head, None)
      self.head.prev = node
      self.head = node

  def insert_at_end(self, data):
    if self.head is None:
      self.head = Node(data, None, None)
      return
    itr = self.head
    while itr.next:
      itr = itr.next
    itr.next = Node(data, None, itr)

  def insert_values(self, data_list):
    self.head = None
    for data in data_list:
      self.insert_at_end(data)

  def print_forward(self):
    if self.head is None:
      print('Linked list is empty.')
      return
    itr = self.head
    llstr = ''
    while itr != None:
      llstr += str(itr.data) + '-->'
      itr = itr.next
    print(llstr)

  def print_backward(self):
    if self.head is None:
      print("Linked list is empty")
      return
    last_node = self.get_last_node()
    itr = last_node
    llstr = ''
    while itr:
      llstr += itr.data + '-->'
      itr = itr.prev
    print(llstr)

  def get_last_node(self):
      itr = self.head
      while itr.next:
        itr = itr.next
      return itr

if __name__ == "__main__":
  ll = DoublyLinkedList()
  # ll.insert_at_beginning(["banana", "mango", "grapes", "orange"])
  # ll.insert_at_end(["banana", "mango", "grapes", "orange"])
  ll.insert_values(["banana", "mango", "grapes", "orange"])
  # ll.print()
  ll.print_forward()
  # ll.get_last_node()
  ll.print_backward()
