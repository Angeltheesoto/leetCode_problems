# Day 19 - Selection Sort --------------

def find_min_element(arr):
  min = 10000000
  for i in range(len(arr)):
    if arr[i] < min:
      min = arr[i]
  return min

# def selection_sort(arr):
#   size = len(arr)
#   for i in range(size-1):
#     min_index = i
#     for j in range(min_index+1, size):
#       if arr[j] < arr[min_index]:
#         min_index = j
    
#     if i != min_index:
#       arr[i], arr[min_index] = arr[min_index], arr[i]

# Practice
def selection_sort(arr, key):
  size = len(arr)
  for i in range(size-1):
    min_index = i
    for j in range(min_index+1, size):
      if arr[j][key] < arr[min_index][key]:
        min_index = j
    
    if i != min_index:
      arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == '__main__':
  # elements = [78, 12, 15, 8, 61, 53, 23, 27]
  # selection_sort(elements)

  # practice
  elements = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

  selection_sort(elements, 'First Name')

  print(elements)
  # print(find_min_element(elements))


