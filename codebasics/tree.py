# Day 9 - Tree --------------

class TreeNode:
  def __init__(self, data):
  # def __init__(self, name, designation):
    self.data = data # Represents any data
    # self.designation = designation
    self.children = [] # Child node is another tree node
    self.parent = None # stores the parent of the TreeNode

  # Add child node into the tree.
  def add_child(self, child):
    child.parent = self
    self.children.append(child)

  # Gets the level your at in the tree. By counting the number of parents.
  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level += 1
      p = p.parent
    return level

  # def print_tree(self):
  #   spaces = ' ' * self.get_level() * 3
  #   prefix = spaces + "|_" if self.parent else ""

  #   print(prefix + self.data)
  #   if self.children:
  #     for child in self.children:
  #       child.print_tree() # recursivly calls itself and all items in the tree.

  # PRACTICE -- Problem 1
  # def print_tree(self, property_name):
  #   if property_name == 'both':
  #     value = self.name + ' (' + self.designation + ') '
  #   elif property_name == 'name':
  #     value = self.name
  #   else:
  #     value = self.designation

  #   spaces = ' ' * self.get_level() * 3
  #   prefix = spaces + "|_" if self.parent else ""

  #   print(prefix + value)
  #   if self.children:
  #     for child in self.children:
  #       child.print_tree(property_name) # recursivly calls itself and all items in the tree.

  # PRACTICE -- Problem 2
  def print_tree(self, lvl):
    if self.get_level() > lvl:
      return

    spaces = ' ' * self.get_level() * 3
    prefix = spaces + "|_" if self.parent else ""

    print(prefix + self.data)
    if self.children:
      for child in self.children:
        child.print_tree(lvl)

# This builds our tree data structure for example.
def build_product_tree():
  root = TreeNode("Electronics") # ROOT NODE

  laptop = TreeNode("Laptop") # parent node
  laptop.add_child(TreeNode("Mac"))
  laptop.add_child(TreeNode("Surface"))
  laptop.add_child(TreeNode("Thinkpad"))

  cellphone = TreeNode("Cell Phone") # parent node
  cellphone.add_child(TreeNode("iPhone"))
  cellphone.add_child(TreeNode("Google Pixel"))
  cellphone.add_child(TreeNode("Vivo"))

  tv = TreeNode("TV") # parent node
  tv.add_child(TreeNode("Samsung"))
  tv.add_child(TreeNode("LG"))

  # Add the child elements to the root tree data structure.
  root.add_child(laptop)
  root.add_child(cellphone)
  root.add_child(tv)

  # prints the level at which node is at.
  # print(tv.get_level())
  return root # returns the whole tree structure.

def build_management_tree():
  root = TreeNode('Nilupul','CEO')

  INFA = TreeNode('Vishwa','Infrastructure Head')
  INFA.add_child(TreeNode('Dhaval','Cloud Manager'))
  INFA.add_child(TreeNode('Abhijit','App Manager'))

  CTO = TreeNode('Chinmay','CTO')
  CTO.add_child(INFA)
  CTO.add_child(TreeNode('Aamir','Application Head'))

  HR = TreeNode('Gels','HR Head')
  HR.add_child(TreeNode("peter","Recruitment Manager"))
  HR.add_child(TreeNode("Waqas","Policy Manager"))

  root.add_child(CTO)
  root.add_child(HR)

  return root

def build_location_tree():
  root = TreeNode('Global')

  GUJARAT = TreeNode('Gujarat')
  GUJARAT.add_child(TreeNode('Ahmedabad'))
  GUJARAT.add_child(TreeNode('Baroda'))

  KARANATAKA = TreeNode('Karanataka')
  KARANATAKA.add_child(TreeNode('Banglurur'))
  KARANATAKA.add_child(TreeNode('Mysore'))

  INDIA = TreeNode('India')
  INDIA.add_child(GUJARAT)
  INDIA.add_child(KARANATAKA)

  NJ = TreeNode('New Jersey')
  NJ.add_child(TreeNode('Princeton'))
  NJ.add_child(TreeNode('Trenton'))

  CAL = TreeNode('California')
  CAL.add_child(TreeNode('San Francisco'))
  CAL.add_child(TreeNode('Mountain View'))
  CAL.add_child(TreeNode('Palo Alto'))

  USA = TreeNode('USA')
  USA.add_child(NJ)
  USA.add_child(CAL)

  root.add_child(INDIA)
  root.add_child(USA)

  return root

if __name__ == '__main__':
  # root = build_product_tree() # assigning the tree structure to variable root
  # print(root.get_level())
  # root.print_tree() # prints the tree structure

  # PRACTICE
  # root = build_management_tree()
  # root.print_tree('designation')

  root = build_location_tree()
  root.print_tree(1)
  pass
