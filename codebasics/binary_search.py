# Day 13 - Binary Search --------------
# decorators -- measure the time of a function
from util import time_it

@time_it
def linear_search(numbers_list, number_to_find):
  for index, element in enumerate(numbers_list):
    if element == number_to_find:
      return index
  return -1

@time_it
def binary_search(numbers_list, number_to_find):
  left_index = 0
  right_index = len(numbers_list) - 1
  mid_index = 0

  # 
  while left_index <= right_index:    
    mid_index = (left_index + right_index) // 2
    mid_number = numbers_list[mid_index]

    # Whenever mid index is equal to number to find
    if mid_number == number_to_find:
      # return the middle index
      return mid_index

    # if the middle index is less than the number to find.
    if mid_index < number_to_find:
      # have the left index be the middle index + 1
      left_index = mid_index + 1
    else:
      # have the right index be the middle index - 1
      right_index = mid_index - 1

  return -1

@time_it
def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
  # var
  mid_index = (left_index + right_index) // 2
  mid_number = numbers_list[mid_index]
  # if right is less than left we return -1 because we cant find the element.
  if right_index < left_index:
    return -1
  if mid_index >= (left_index + right_index) or mid_index < 0:
    return -1
  # if mid number is the one your looking for, return it.
  if mid_number == number_to_find:
    return mid_index
  # if mid is less than number were looking for. We set the index after mid to left.
  if mid_number < number_to_find:
    left_index = mid_index + 1
  else:
    # if mid is greater than number were looking for. We set the index before mid to right index.
    right_index = mid_index - 1
  # We call the function again in case we dont find it the first time.
  return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
  # numbers_list = [i for i in range(10000001)]
  # number_to_find = 1000000
  # index = linear_search(numbers_list, number_to_find)
  # print(f"Number found at index {index} using linear search")

  numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
  number_to_find = 45

  # index = binary_search(numbers_list, number_to_find)
  # print(f"Number found at index {index} using binary search")

  index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
  print(f"Number found at index {index} using recursive binary search")
