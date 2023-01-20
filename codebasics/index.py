# ARRAY PRACTICE

# Day 3 - Array DataStructure --------------
# https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/2_Arrays/2_arrays_exercise.md

# SECTION - 1. Let us say your expense for every month are listed below, ...
expenses = {'January': 2200, 'February': 2350, 'March': 2000, 'April': 2130, 'May': 2190}
expenses_list = [2200, 2350, 2600, 2130, 2190]

# print(expenses["January"])

# 1. In Feb, how many dollars you spent extra compare to January?
def jan_compare_feb():
  return expenses['February'] - expenses['January']
# print(jan_compare_feb())

# 2. Find out your total expense in first quarter (first three months) of the year.
def add_first_quarter(one, two, three):
  return one + two + three
# print(add_first_quarter(expenses["January"], expenses["February"], expenses["March"]))

# 3. Find out if you spent exactly 2000 dollars in any month
def exact_2000():
  for key, value in expenses.items():
    # print(key, value)
    if value == 2000:
      print(f"Expense in {key} is equal to 2000.")
    # else:
    #   print(f"Expense in {key} is not equal 2000.")
# print(exact_2000())

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
def add_expense(expense):
  print(expenses_list)
  expenses_list.append(expense)
  print(expenses_list)
# print(add_expense(1980))

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list based on this.
def refund(month, amount):
  print(expenses_list)
  expenses_list[month] = expenses_list[month] - int(amount)
  print(expenses_list)
# print(refund(3, 200))

# SECTION - 2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
# print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
# print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'
heros.pop()
heros.insert(3, 'black panther')
# print(heros)

# 4. Now you don't like thor and hulk because they get angry easily So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
heros[1] = 'doctor strange'
heros[2] = 'doctor strange'
# print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros = sorted(heros)
# print(heros)

# SECTION - 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# This adds an array of numbers inputed.
def create_list():
  num = input("Enter a number: ")
  my_list = []
  for i in range(int(num)):
    if len(num):
      my_list.append(i)
  print(my_list)
# create_list()

# This creates an array of odd numbers.
def all_odd_num():
  num = int(input("Enter a number: "))
  odd_list = []
  for i in range(num):
    if i % 2 == 1:
      odd_list.append(i)
  print(odd_list)
# all_odd_num()