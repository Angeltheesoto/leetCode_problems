# Day 15 - Quick Sort -------

# quick sort - use divide and conquer
# Hoare partition schema
# Lomuto partition schema

def swap(a, b, arr):
  if a != b:
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def hoare_partition(elements, start, end):
  pivot_index = start
  pivot = elements[pivot_index]
  while start < end:
    while start < len(elements) and elements[start] <= pivot:
      start += 1
    while elements[end] > pivot:
      end -= 1
    if start < end:
      swap(start, end, elements)
  swap(pivot_index, end, elements)
  return end

def lomuto_partition(elements, start, end):
  pivot = elements[end]
  p_index = start
  for i in range(start, end):
    if elements[i] <= pivot:
      swap(i, p_index, elements)
      p_index += 1
    swap(p_index, end, elements)
    return p_index

def quick_sort(elements, start, end):
  if len(elements) == 1:
    return

  if start < end:
    pi = hoare_partition(elements, start, end)
    quick_sort(elements, start, pi - 1) # left partition
    quick_sort(elements, pi + 1, end) # right partition

if __name__ == '__main__':
  elements = [11, 9, 29, 7, 2, 15, 28]
  quick_sort(elements, 0, len(elements)-1)
  print(elements)