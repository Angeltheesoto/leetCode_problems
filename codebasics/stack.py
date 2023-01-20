# Day 7 - Stack --------------

# s = []
# s.append(['https://www.cnn.com/'])
# s.append(['https://www.cnn.com/world'])
# s.append(['https://www.cnn.com/india'])
# s.append(['https://www.cnn.com/china'])

# print('one: ', s)
# s.pop()
# print('two: ', s)
# s.pop()
# print('three: ', s)
# s.pop()
# print('four: ', s)
# s.pop()
# print('five: ', s)

from collections import deque
stack = deque()

class Stack:
  def __init__(self):
    self.container = deque()

  def push(self, val):
    self.container.append(val)

  def pop(self):
    return self.container.pop()

  def peek(self):
    return self.container[-1]

  def is_empty(self):
    return len(self.container) == 0

  def size(self):
    return len(self.container)

# Practice
def reverse_string(my_string):
  stack = Stack()

  for ch in my_string:
    stack.push(ch)
  # return stack.container
  rstr = ''
  while stack.size() != 0:
    rstr += stack.pop()
  return rstr

def is_match(ch1, ch2):
  map = {
    ")":"(",
    "]":"[",
    "}":"{"
  }
  return map[ch1] == ch2


def is_balanced(my_string):
  stack = Stack()
  
  for ch in my_string:
    if ch == '(' or ch == '{' or ch == '[':
      stack.push(ch)
    if ch == ')' or ch == '}' or ch == ']':
      if stack.size() == 0:
        return False
      if not is_match(ch, stack.pop()):
        return False

  return stack.size() == 0

s = Stack()
# stack.append("https://www.cnn.com/")
# stack.append("https://www.cnn.com/world")
# stack.append("https://www.cnn.com/india")
# stack.append("https://www.cnn.com/china")
# print(stack)

# s.push(5)
# s.push(9)
# s.push(34)
# s.push(78)
# s.push(12)
# print(s.peek())
# print(s.is_empty())
# print(s.pop())
# print(s.size())
# print(s.container)

# Practice
# print(reverse_string("We will conquere COVID-19"))
print(is_balanced("({a+b})"))