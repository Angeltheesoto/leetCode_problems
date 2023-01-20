# Day 8 - Queue --------------

# List as a queue -- has issues, not recommended.
# wmt_stock_price_queue = []
# wmt_stock_price_queue.insert(0, 131.10)
# wmt_stock_price_queue.insert(0, 132.12)
# wmt_stock_price_queue.insert(0, 135)

# print(wmt_stock_price_queue)
# wmt_stock_price_queue.pop()
# print(wmt_stock_price_queue)

# Collections.deque as Queue -- 

from collections import deque
from time import sleep
import threading

class Queue:
  def __init__(self):
    self.buffer = deque()

  def enqueue(self, val):
    self.buffer.appendleft(val)

  def dequeue(self):
    return self.buffer.pop()

  def is_empty(self):
    return len(self.buffer) == 0
  
  def size(self):
    return len(self.buffer)

  def front(self):
    return self.buffer[-1]

food_order_queue = Queue()
  # Practice
def place_order(order):
  for item in order:
    print('Your order is: ', item); sleep(0.5)
    food_order_queue.enqueue(item)

def serve_order():
  sleep(1)
  while True:
    order = food_order_queue.dequeue()
    print("Now Serving: ", order); sleep(2)

binary_queue = Queue()
def print_binary(num):
  binary_queue.enqueue('1')
  for i in range(num):
    front = binary_queue.front()
    print(" ", front)
    binary_queue.enqueue(front + '0')
    binary_queue.enqueue(front + '1')

    binary_queue.dequeue()

# Practice
print(print_binary(10))

# This just prints the code in order.
# print(place_order(['pizza','samosa','pasta','biryani','burger']))
# print(food_order_queue.buffer)
# print(serve_order())

# This is for printing the code simultaniously! Like async await.
# t1 = threading.Thread(target=place_order, args=(['pizza','samosa','pasta','biryani','burger'],))
# t2 = threading.Thread(target=serve_order)
# t1.start()
# t2.start()


# q = deque()
# q.appendleft(5)
# q.appendleft(8)
# q.appendleft(27)
# q.pop()
# q.pop()
# q.pop()
# print(q)

pq = Queue()
# pq.enqueue({
#   'company': 'Wall Mart',
#   'timestamp': '15 apr, 11.01 AM',
#   'price': 131.10
# })
# pq.enqueue({
#   'company': 'Wall Mart',
#   'timestamp': '15 apr, 11.02 AM',
#   'price': 132
# })
# pq.enqueue({
#   'company': 'Wall Mart',
#   'timestamp': '15 apr, 11.03 AM',
#   'price': 135
# })
# print(pq.buffer)

