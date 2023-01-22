# Day 14 - Bubble Sort --------------

def bubble_sort(elements):
  size = len(elements)
  # checks every element in the list
  for i in range(size-1):
    swapped = False
    # flips every element
    for j in range(size-1):
      if elements[j] > elements[j+1]:
        # flips two elements 
        tmp = elements[j]
        elements[j] = elements[j+1]
        elements[j+1] = tmp
        swapped = True
    if not swapped:
      break

def practice_bubble_sort(elements, key):
  size = len(elements)

  for i in range(size-1):
    swapped = False
    for j in range(size-1-i):
      a = elements[j][key]
      b = elements[j+1][key]
      if a>b:
        tmp = elements[j]
        elements[j] = elements[j+1]
        elements[j+1] = tmp
        swapped = True

    if not swapped:
      break

if __name__ == '__main__':
  elements = [5,9,2,1,67,34,88,34]

  # bubble_sort(elements)

  # practice
  elements = [
    { 'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
    { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
    { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

  practice_bubble_sort(elements, 'transaction_amount')
  print(elements)
