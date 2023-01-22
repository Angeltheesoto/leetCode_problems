# Day 16 - Insertion Sort --------------
# use for small arrays not for big arrays

def insertion_sort(arr):
  for i in range(1, len(arr)):
    # anchor is the element were dealing with currently
    anchor = arr[i]
    j = i - 1
    # loop through the sorted array in the array.
    while j >= 0 and arr[j] > anchor:
      # Swap the anchor with the value in the sorted array
      arr[j+1] = arr[j]
      j = j - 1
    # have the new anchor be the last swapped element in the sorted part of the array.
    arr[j+1] = anchor

if __name__ == '__main__':
  arr = [11,9,29,7,2,15,28]
  insertion_sort(arr)
  print(arr)
