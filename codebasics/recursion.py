# Day 20 - Recursion --------------

"""
# 3 steps into recursion
1. Divide big problem into small and simple problem.
2. Find a base condition with simple answer.
3. Return base condition answer to solve all sub problems.

5 + 10 -> 15
4 + 6 -> 10
3 + 3 -> 6
2 + 1 -> 3
1 -> 1
"""

# def find_sum(n):
#   sum = 0
#   for i in range(1, n+1):
#     print(i)
#     sum+=i
#   return sum

# recursive
# def find_sum(n):
#   if n == 1:
#     return 1
#   return n + find_sum(n-1)

# Fibonacci Sequence
def fib(n):
  if n == 0 or n == 1:
    return n
  return fib(n-1) + fib(n-2)

if __name__ == '__main__':
  # print(find_sum(5))
  print(fib(6))


