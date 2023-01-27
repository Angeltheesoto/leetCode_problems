# This is the Blind 75 questions that help prepare for interviews.
# number - title - tags
# tag=array\hashtable, difficulty=easy, acceptence=high_percent

# Array / HashTable problems ===============================
# 217 - Contains duplicate - Array | Hash table | Sorting
class Solution(object):
  def containsDuplicate(self, nums):
    # time complexity= O(n^2)
    # for i in range(len(nums)):
    #   for j in range(i + 1, len(nums)):
    #     if nums[i] == nums[j]:
    #       return True
    # return False

    # time complexity= O(n)
    hashset = set()
    for n in nums:
      if n in hashset:
        return True
      # loops through each element in the array and adds them to set() and if any are already there it returns true.
      hashset.add(n)
    return False
# if __name__ == '__main__':
#   sol = Solution()
#   print(sol.containsDuplicate([1,2,3,1])) # True
#   print(sol.containsDuplicate([1,2,3,4])) #False
#   print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])) # True

# 242 - Valid Anagram - String | Sorting | Hash table
def isAnagram(s, t):
  # time complexity - O(s+t)
  # if len(s) != len(t):
  #   return False
  # countS, countT = {}, {}
  # for i in range(len(s)):
  #   # key value - we count the occurence of each chtr in string s, t
  #   countS[s[i]] = 1 + countS.get(s[i], 0)
  #   countT[t[i]] = 1 + countT.get(t[i], 0)
  # for c in countS:
  #   # if the key in S does not equal in T return false
  #   if countS[c] != countT.get(c):
  #     return False
  # return True
  
  # time complexity - O(nlogn) - space - O(1)
  # my solution
  sort_s = sorted(s)
  sort_t = sorted(t)
  if sort_s == sort_t:
    return True
  return False
# print(isAnagram('anagram', "nagaram"))
# print(isAnagram('rat', "car"))
# print(isAnagram('a', "ab"))

# 1 - Two Sum - Array | Hash table
def twoSum(nums, target):
  # time complexity - O(n^2)
  # for i in range(len(nums)):
  #   for j in range(i+1, len(nums)):
  #     # return nums[j]
  #     if nums[i] + nums[j] == target:
  #       return [i, j]

  # time complexity - O(n) - space - (n)
  hashmap = {} # val : index
  for i, n in enumerate(nums):
    diff = target - n
    if diff in hashmap:
      return [hashmap[diff], i]
    hashmap[n] = i
  return
# print(twoSum([2,7,11,15], 9))
# print(twoSum([3,2,4], 6))
# print(twoSum([3, 3], 6))
# Array / HashTable problems ===============================


# Two pointers =============================================
# 125 - Valid Palindrome - Two Pointers | String
import re
class Solution_two(object):
  def reverseList(self, arr):
    start = 0
    end = len(arr) - 1
    while start < end:
      arr[start] = arr[end]
      arr[end] = arr[start]
      start += 1
      end -= 1
  def isPalindrome(self, s):
    # newString = ''.join(filter(str.isalnum, s)).lower()
    newString = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    newString = [x for x in newString]
    # two pointers ---
    start = 0
    end = len(newString) - 1
    while start < end:
      if newString[start] != newString[end]:
        return False
      else:
        start += 1
        end -= 1
    return True
    # First solution ---
    reverseString = []
    for i in reversed(newString):
      reverseString.append(i)
    if ''.join(newString) == ''.join(reverseString):
      return True
    return False
# if __name__ == "__main__":
#   soltwo = Solution_two()
#   print(soltwo.isPalindrome("A man, a plan, a canal: Panama"))
#   print(soltwo.isPalindrome("race a car"))
#   print(soltwo.isPalindrome(" "))
# Two pointers =============================================


# Sliding Window =======================================
# 121 - Best Time to Buy and Sell Stock - Array | Dynamic Programming
def maxProfit(prices):
  # print(prices)
  # prompt: we want to find the max amount of profit we can earn from the array with the n amount of days.
  """
  1. iterate through the array.
  2. check if any item after the curr item is greater than the item.
    a. if it is then store the value minus the item in a variable if the value is greater than the variable value.
  3. return the variable value.
  """
  l, r = 0, 1 # left = buy, right = sell
  maxP = 0

  while r < len(prices):
    # profitable ?
    if prices[l] < prices[r]:
      profit = prices[r] - prices[l]
      maxP = max(maxP, profit)
    else:
      l = r
    r += 1
  print(maxP)
# maxProfit([7,1,5,3,6,4])
# maxProfit([7,6,4,3,1])
# maxProfit([1,2,3,4,5])
# Sliding Window =======================================


# Stack =======================================
# 20 - Valid Parentheses - Stack | String
# Time complexity= O(n)
def isValid(s):
  stack = []
  hashmap = {
    ')': '(',
    ']': '[',
    '}': '{'
  }

  # for i in s:
  #   if i == '(' or i == '[' or i == '{':
  #     stack.append(i)
  #     print(stack)
  #   if i == ')' or i == ']' or i == '}':
  #     if len(stack) == 0:
  #       return False
  #     if hashmap[i] != stack.pop():
  #       return False
  # return len(stack) == 0

  for c in s:
    if c not in hashmap:
      stack.append(c)
      continue
    if not stack or stack[-1] != hashmap[c]:
      return False
    stack.pop()
  return not stack

# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("(]"))
# print(isValid("]"))
# Stack =======================================

# Binary Search =======================================
# pass
# Binary Search =======================================

# Linked List =======================================
# 206 - Reverse Linked List - Linked List | Recursion
class LinkedList(object):
  def reverseList(self, head):
    return head

if __name__ == '__main__':
  ll = LinkedList()
  print(ll.reverseList([1,2,3,4,5])) # [5,4,3,2,1]
  print(ll.reverseList([1,2])) # [2,1]
# Linked List =======================================
