# Day 10 - Binary Search Tree(BST) --------------

class BinarySearchTreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

  def add_child(self, data):
    if data == self.data:
      return
    if data < self.data:
      # add to left
      if self.left:
        self.left.add_child(data)
      else:
        self.left = BinarySearchTreeNode(data)
    else:
      # add to right
      if self.right:
        self.right.add_child(data)
      else:
        self.right = BinarySearchTreeNode(data)

  def in_order_traversal(self):
    elements = []
    # visit left tree
    if self.left:
      elements += self.left.in_order_traversal()
    # visit base node
    elements.append(self.data)
    # visit right tree
    if self.right:
      elements += self.right.in_order_traversal()
    return elements

  def search(self, val):
    if self.data == val:
      return True
    if val < self.data:
      # val might be in left subtree
      if self.left:
        return self.left.search(val)
      else:
        return False
    if val > self.data:
      # val might be in right subtree
      if self.right:
        return self.right.search(val)
      else:
        return False

  # PRACTICE --
  def find_min(self):
    arr = self.in_order_traversal()
    num = arr[0]
    for i in arr:
      if num > i:
        num = i
    return num

  def find_max(self):
    arr = self.in_order_traversal()
    num = arr[0]
    for i in arr:
      if i > num:
        num = i
    return num

  def calculate_sum(self):
    total = self.in_order_traversal()
    sum = 0
    for i in total:
      sum += i
    return sum

  def post_order_traversal(self):
    elements = []
    if self.left:
      elements += self.left.post_order_traversal()
    if self.right:
      elements += self.right.post_order_traversal()
    elements.append(self.data)
    return elements

  def pre_order_traversal(self):
    elements = [self.data]
    if self.left:
      elements += self.left.pre_order_traversal()
    if self.right:
      elements += self.right.pre_order_traversal()
    return elements

# Build our tree
def build_tree(elements):
  root = BinarySearchTreeNode(elements[0])
  for i in range(1, len(elements)):
    root.add_child(elements[i])
  return root

# Logs the data
if __name__ == '__main__':
  numbers = [17,4,1,20,9,23,18,34]
  numbers_tree = build_tree(numbers)
  # print(numbers_tree.in_order_traversal())
  # print(numbers_tree.search(210))

  # PRACTICE --
  print(numbers_tree.find_min())
  print(numbers_tree.find_max())
  print(numbers_tree.calculate_sum())
  print(numbers_tree.in_order_traversal())
  print(numbers_tree.post_order_traversal())
  print(numbers_tree.pre_order_traversal())