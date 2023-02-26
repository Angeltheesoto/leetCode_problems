
# !This is the Blind 75 questions that help prepare for interviews.
# !number - title - tags
# !tag=array\hashtable, difficulty=easy, acceptence=high_percent

# ?Array / HashTable problems ===============================
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

# MEDIUM -
# 49 - Group Anagrams - Array | Hash table | String | Sorting
def groupAnagrams(strs):
  # dic = {}
  # for i in range(len(strs)):
  #   curr = ''.join(sorted(strs[i]))
  #   if curr not in dic:
  #     dic[curr] = [i]
  #   else:
  #     dic[curr] += [i]
  # index_list = list(dic.values())
  # return dic.values()

  dic = {}
  for i in strs:
    curr = str(sorted(i))
    if curr not in dic:
      dic[curr] = [i]
    else:
      dic[curr].append(i)
  return dic
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams([""]))
# print(groupAnagrams(["a"]))

# 347 - Top K Frequent Elements - Array | Hash table | Divide and Conquer | etc..
from operator import itemgetter
def topKFrequent(nums, k):
  dic = {}
  for i in nums:
    if not i in dic:
      dic[i] = 1
    else:
      dic[i] += 1
  res = dict(sorted(dic.items(), key = itemgetter(1), reverse=True)[:k])
  print(list(res.keys()))
# print(topKFrequent([1,1,1,2,2,3], 2))
# print(topKFrequent([2, 3, 3, 3, 4, 4, 5, 5, 5], 2))

# 238 - Product of Array Except Self - Array | Prefix Sum


# ?Array / HashTable problems ===============================


# ?Two pointers =============================================
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
# ?Two pointers =============================================


# ?Sliding Window =======================================
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
# ?Sliding Window =======================================


# ?Stack =======================================
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
# ?Stack =======================================

# ?Binary Search =======================================
# ?Binary Search =======================================

# ?Linked List =======================================
class LLNode:
  def __init__(self, data=None, next=None):
    self.data = data 
    self.next = next 

class LinkedList(object):
  def __init__(self):
    self.head = None # Points to the head of the linked list.

# Methods to add element to list.
  def push(self, new_data):
    new_node = LLNode(new_data)
    new_node.next = self.head
    self.head = new_node
  def addToList(self, newData):
    newNode = LLNode(newData)
    if self.head is None:
      self.head = newNode
      return
    last = self.head
    while last.next:
      last = last.next
    last.next = newNode
# Method to print list.
  def printList(self):
    itr = self.head
    llstr = ''
    while itr:
      llstr += str(itr.data) + '-->'
      itr = itr.next
    print(llstr)

# 206 - Reverse Linked List - Linked List | Recursion
# T O(n), M O(1)
  def reverseList(self):
    prev = None
    curr = self.head
    while curr:
      nxt = curr.next
      curr.next = prev
      prev = curr
      curr = nxt
    self.head = prev

# 141 - Linked List Cycle - Linked List | Hash Table | Two Pointers
# T O(n), M O(1)
  def hasCycle(self):
    slow, fast = self.head, self.head
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next
      if slow == fast:
        return True
    return False
    # geeksforgeeks solution ==>
    # s = set()
    # temp = self.head
    # while(temp):
    #   if (temp in s):
    #     return True
    #   s.add(temp)
    #   temp = temp.next
    # return False

# 21 - Merge two Sorted Lists - Linked List | Recursion
# T O(), M O()
def mergeTwoLists(list1, list2):
  dummy = LLNode()
  tail = dummy
  # This works locally==>
  # while True:
  #   if list1 is None:
  #     tail.next = list2
  #     break
  #   if list2 is None:
  #     tail.next = list1
  #     break
  #   if list1.data <= list2.data:
  #     tail.next = list1
  #     list1 = list1.next
  #   else:
  #     tail.next = list2
  #     list2 = list2.next
  #   tail = tail.next
  # return dummy.next

  # This works on leetcode==>
  while list1 and list2:
    if list1.data < list2.data:
      tail.next = list1
      list1 = list1.next
    else:
      tail.next = list2
      list2 = list2.next
    tail = tail.next
  if list1:
    tail.next = list1
  elif list2:
    tail.next = list2
  return dummy.next

# if __name__ == '__main__':
  # Reverse LL
  # ll = LinkedList()
  # ll.push(1)
  # ll.push(2)
  # ll.push(3)
  # ll.push(4)
  # ll.push(5)
  # ll.printList()
  # ll.reverseList() # [5,4,3,2,1]
  # ll.printList()

  # Merge two
  # l1 = LinkedList()
  # l2 = LinkedList()
  # l1.addToList(1)
  # l1.addToList(2)
  # l1.addToList(3)
  # l2.addToList(2)
  # l2.addToList(3)
  # l2.addToList(4)
  # l1.printList()
  # l2.printList()
  # l1.head = mergeTwoLists(l1.head, l2.head)
  # l1.printList()

  # Linked List Cycle
  # ll = LinkedList()
  # ll.addToList(20)
  # ll.addToList(4)
  # ll.addToList(15)
  # ll.addToList(10)
  # ll.head.next.next.next.next = ll.head
  # if(ll.hasCycle()):
  #   print('Loop Found')
  # else:
  #   print('No Loop')
# ?Linked List =======================================

# ?Trees =======================================
# This creates our tree.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def PrintTree ( self ) :
       if self.left :
           self.left.PrintTree ()
       print ( self.val, end= ' ' ) ,
       if self.right :
           self.right.PrintTree ()

class Tree_Functions(object):
# 226 - Invert Binary Tree - Tree | Depth-First Search(DFS) | Breadth-First Search(BFS) | Binary Tree
  def invertTree(self, root):
    if not root:
      return None
    # swap the children
    tmp = root.left
    root.left = root.right
    root.right = tmp
    # recursively invert subtrees
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

# 104 - Maximum Depth of Binary Tree - Tree | Depth-First Search(DFS) | Breadth-First Search(BFS) | Binary Tree
  def maxDepth(self, root):
    pass

# if __name__ == '__main__':
# This creates our tree.
# INVERT TREE
  # create_tree = TreeNode(4)
  # create_tree.left = TreeNode(2)
  # create_tree.right = TreeNode(7)
  # create_tree.left.left = TreeNode(1)
  # create_tree.right.right = TreeNode(9)
  # print('Initial Tree :',end = ' ' )
  # create_tree.PrintTree()
  # # This inverts our tree.
  # Tree_Functions().invertTree(root=create_tree)
  # print('\nInverted Tree :', end=' ')
  # create_tree.PrintTree()
# ?Trees =======================================

# ?1-D Dynamic Programming =======================================
# 70 - Climbing Stairs - Math | Dynamic Programming | Memoization
def climbStairs(n):
    memo = {}
    memo[1] = 1
    memo[2] = 2
    def climb(n):
        if n in memo:
            return memo[n]
        else:
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]
    return climb(n)
# print(climbStairs(3))
# print(climbStairs(4))
# print(climbStairs(5))
# print(climbStairs(6))
# print(climbStairs(7))
# print(climbStairs(8))
# print(climbStairs(9))
# print(climbStairs(10))
# ?1-D Dynamic Programming =======================================

# ?Bit Manipulation =======================================
# 191 - Number of 1 Bits - Divide and Conquer | Bit Manipulation
def hammingWeight(n):
    count = 0
    while n:
      n &= n - 1
      count += 1
    return count
# print(hammingWeight('00000000000000000000000000001011'))
# print(hammingWeight('00000000000000000000000010000000'))
# print(hammingWeight('11111111111111111111111111111101'))

# 338 - Counting Bits - Dynamic Programming | Bit Manipulation
def countBits(n):
  dp = [0] * (n + 1)
  offset = 1
  for i in range(1, n+ 1):
    if offset * 2 == i:
      offset = i
    dp[i] = 1 + dp[i - offset]
  return dp
# print(countBits(2))
# print(countBits(5))

# 190 - Reverse Bits - Divide and Conquer | Bit Manipulation
def reverseBits(n):
  # bit = bin(n)
  # bit_len = bin(n)[2:]
  # reverse_num = bit[-1:1:-1]
  # reverse_num += (len(bit_len) - len(reverse_num))*'0'
  # reverse_num = int(reverse_num, 2)
  # return reverse_num

  res = 0
  for i in range(0, 32):
    res <<= 1
    if n & 1: # checks if the inputs value is 1. [0 & 1 = 0] | [1 & 1 = 1]
      res += 1
    n >>= 1
  return res
# print(reverseBits(0b0000010100101000001111010011100))
# print(reverseBits(0b11111111111111111111111111111101))

# 280 - Missing Number - Array | Hash Table | Math | Binary Search | Bit Manipulation | Sorting
def missingNumber(nums):
  # MY solution:
  # sorted_nums = sorted(nums)
  # if len(nums):
  #   does_it_exist = sorted_nums.count(0)
  #   if not does_it_exist:
  #     return 0
  # for i in range(sorted_nums[0], sorted_nums[-1] + 1):
  #   if i not in sorted_nums:
  #     return i
  # return sorted_nums[-1] + 1
  res = len(nums)
  for i in range(len(nums)):
    print(res)
    print('arithmic', i, nums[i])
    res += (i - nums[i])
  return res
# print(missingNumber([3,0,1])) # 2
# print(missingNumber([0,1])) # 2
# print(missingNumber([9,6,4,2,3,5,7,0,1])) # 8
# print(missingNumber([0])) # 1
# print(missingNumber([1])) # 0
# print(missingNumber([1, 2])) # 0

# ?Bit Manipulation =======================================
