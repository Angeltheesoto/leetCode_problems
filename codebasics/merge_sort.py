# Day 17 - Merge Sort --------------

# def merge_sort(arr, key):
#   # if our arr size is less than 1, just return the arr
#   if len(arr) <= 1:
#     return
#   # divide array into two parts
#   mid = len(arr) // 2
#   left = arr[:mid]
#   right = arr[mid:]
#   merge_sort(left)
#   merge_sort(right)
#   merge_two_sorted_lists(left, right, arr)

# def merge_two_sorted_lists(a,b, arr):
#   # sorted_list = []
#   len_a = len(a)
#   len_b = len(b)
#   i = j = k = 0
#   # loops through both arrays
#   while i < len_a and j < len_b:
#     # if element at a is less than equal to element at b..
#     if a[i] <= b[j]:
#       # add it to the sorted list..
#       arr[k] = a[i]
#       # increment i
#       i+=1
#     else:
#       # add it to the sorted list...
#       arr[k] = b[j]
#       # increment j
#       j+=1
#     k += 1
#   # This adds everything after one loop ended 
#   while i < len_a:
#     arr[k] = a[i]
#     i+=1 
#     k+=1
#   while j < len_b:
#     arr[k] = b[j]
#     j+=1
#     k+=1

# practice
def merge_sort(elements, key, descending=False):
  size = len(elements)
  if size == 1:
    return elements
  left_list = merge_sort(elements[0:size//2], key, descending)
  right_list = merge_sort(elements[size//2:], key, descending)
  sorted_list = merge(left_list, right_list, key, descending)
  return sorted_list

def merge(left_list, right_list, key, descending=False):
  merged = []
  if descending:
    while len(left_list) > 0 and len(right_list) > 0:
      if left_list[0][key] >= right_list[0][key]:
        merged.append(left_list.pop(0))
      else:
        merged.append(right_list.pop(0))
  else:
    while len(left_list) > 0 and len(right_list) > 0:
      if left_list[0][key] <= right_list[0][key]:
        merged.append(left_list.pop(0))
      else:
        merged.append(right_list.pop(0))
  merged.extend(left_list)
  merged.extend(right_list)
  return merged

if __name__ == '__main__':
  # merge two list
  # a = [5,8,12,56]
  # b = [7,9,45,51]
  # print(merge_two_sorted_lists(a,b))

  # merge_sort
  # arr = [10, 3, 15, 7, 8, 23, 98, 29]
  # merge_sort(arr)
  # print(arr)

  # practice
  elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
  merge_sort(elements, key='age', descending=True)
  print(elements)
