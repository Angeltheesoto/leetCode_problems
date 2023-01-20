# Day 11 - Binary Search Tree(BST) 2 --------------
# class ---
class binarySearchTree:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
  
  # methods ---
  def add_child(self, data):
    if data == self.data:
      return
    if data < self.data:
      if self.left:
        self.left.add_child(data)
      else:
        self.left = binarySearchTree(data)
    else:
      if self.right:
        self.right.add_child(data)
      else:
        self.right = binarySearchTree(data)

  def in_order_traversal(self):
    elements = []
    if self.left:
      elements += self.left.in_order_traversal()
    elements.append(self.data)
    if self.right:
      elements += self.right.in_order_traversal()
    return elements

  def search(self, val):
    if self.data == val:
      return True
    if val < self.data:
      if self.left:
        return self.left.search(val)
      else:
        return False
    if val > self.data:
      if self.right:
        return self.right.search(val)
      else:
        return False

  def find_max(self):
    if self.right is None:
      return self.data
    return self.right.find_max()

  def find_min(self):
    if self.left is None:
      return self.data
    return self.left.find_min()

  # Practice
  # Deletes a value.
  def delete(self, val):
    # is the value less than the curr node.
    if val < self.data:
      # if so, search left subtree
      if self.left:
        # recursivly call delete method on left subtree
        self.left = self.left.delete(val)
    # is the value greater than the curr node.
    elif val > self.data:
      # if so, search right subtree
      if self.right:
        # recursively call delete method on right subtree
        self.right = self.right.delete(val)
    else:
      # if left and right are none return none because you reached the last data-point
      if self.left is None and self.right is None:
        return None
      # if only left is none then return the right node
      if self.left is None:
        return self.right
      # if only right is none then return the left node
      if self.right is None:
        return self.right

      # takes the min value from right side
      min_val = self.left.find_min()
      # put the min val up one level to be the parent node
      self.data = min_val
      # delete the right subtree min val that you moved above
      self.left = self.left.delete(min_val)
    # returns the new tree.
    return self

# trees ---
def build_tree(elements):
  root = binarySearchTree(elements[0])
  for i in range(1, len(elements)):
    root.add_child(elements[i])
  return root

# display ---
if __name__ == '__main__':
  numbers = [17,4,1,20,9,23,18,34]
  numbers_tree = build_tree(numbers)

  print(numbers_tree.in_order_traversal())
  numbers_tree.delete(20)
  print(numbers_tree.in_order_traversal())

"""
Depth-first search:
  - Traverse through left subtree(s) first, then traverse through the right subtree(s)

Breadth-first search:
  - Traverse through one level of children nodes, then traverse through the level of grandchildren nodes and so on...

"""

