# Day 18 - Shell Sort --------------

# Shell sort is an optimization over insertion sort.
# Issues with insertion sort:
# When small elements are towards the end it takes many, 
# 1. Comparisons
# 2. Swaps

# Shell Sort lets you move heavier elements to the right hand side will make insertion sort easier and quicker to preform because it does less swaps and comparisons.

# General Goal:
# 1. Start with gap = n/2 and sort sub arrays
# 2. Keep reducing gap by n/2 in and keep on sorting subarrays.
# 3. Last iteration should have gap = 1. At this point it is the same as insertion sort.

# With gap of 3 only
# def shell_sort(arr):
#   size = len(arr)
#   # how much space between elements we move through the arr
#   gap = 3

#   for i in range(gap, size):
#     # the pointer we are on looping through the arr
#     anchor = arr[i]
#     # second pointer to loop through the arr
#     j = i
#     # if the element is within the range of gap and the prev element is grater than the next element keep doing this.
#     while j >= gap and arr[j - gap] > anchor:
#       print(f'Step: {arr} \n')
#       # here you copy the index value.
#       arr[j] = arr[j-gap] # arr[j-gap] is the previous element
#       # In each while loop iteration you want to reduce by gap.
#       j -= gap
#     # When this end then the last ele will be the new anchor element
#     arr[j] = anchor

def shell_sort(arr):
  size = len(arr)
  div = 2
  gap = size // div
  while gap > 0:
    index_to_delete = []
    for i in range(gap, size):
      print(f'Step: {arr} \n')
      anchor = arr[i]
      j = i
      while j >= gap and arr[j - gap] > anchor:
        if arr[j-gap] == anchor:
          index_to_delete.append(j)
        arr[j] = arr[j-gap]
        j -= gap
      arr[j] = anchor
      index_to_delete = list(set(index_to_delete))
      index_to_delete.sort()
      if index_to_delete:
        for i in index_to_delete[-1::-1]:
          del arr[i]
    div *= 2
    gap = gap // div


if __name__ == '__main__':
  # elements = [21,38, 29, 17, 4, 25, 11, 32, 9]
  elements = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
  shell_sort(elements)
  print(elements)
