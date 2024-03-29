
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
def productExceptSelf(nums):
  # answer = [1] # right
  # for i in range(len(nums)-1, 0, -1):
  #   answer.append(answer[-1] * nums[i])
  # answer = answer[::-1]
  # left = 1
  # for i in range(len(nums)):
  #   answer[i] = answer[i]*left
  #   left *= nums[i]
  # return answer
  res = [1] * (len(nums))
  prefix = 1
  for i in range(len(nums)):
    res[i] = prefix
    prefix *= nums[i]
  postfix = 1
  for i in range(len(nums) - 1, -1 , -1):
    res[i] *= postfix
# print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
# print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]
# print(productExceptSelf([0, 0])) # [0,0]
# print(productExceptSelf([1, 0])) # [0, 1]

# 128 - Longest Consecutive Sequence - 
def longestConsecutive(nums):
  numSet = set(nums)
  longest = 0
  for n in nums:
    # check if its the start of a sequence
    if (n-1) not in numSet: # if there is no left neighbor in numSet then its the start of a sequence.
      next_num = 0
      while (n + next_num) in numSet:
        next_num += 1 # increment count for every element that continues the sequence.
      longest = max(next_num, longest)
  return longest
# [1, 2, 3, 4, 100, 200]
# print(longestConsecutive([100,4,200,1,3,2])) # 4
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
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

# 15 - 3sum - Array | Two Pointers | Sorting
def threeSum(nums):
  res = []    # [ 0,  1,  2, 3, 4, 5] Index
  nums.sort() # [-4, -1, -1, 0, 1, 2] Values
  for i, a in enumerate(nums):
      if a > 0:
          break
      if i > 0 and a == nums[i - 1]:
          continue # skips to the next value if its the same as prev
      l, r = i + 1, len(nums) - 1
      while l < r:
          threeSum = a + nums[l] + nums[r]
          if threeSum > 0:
              r -= 1
          elif threeSum < 0:
              l += 1
          else:
              res.append([a, nums[l], nums[r]])
              l += 1
              r -= 1
              while nums[l] == nums[l - 1] and l < r:
                  l += 1 # if the next item is the same then continue
  return res
# print(threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
# print(threeSum([0,1,1]))
# print(threeSum([0,0,0]))

# 11 - Container With Most Water - 
def maxArea(height):
  a = 0
  b = len(height)-1
  heighest_water_amount = 0
  while a < b:
    distance_between_pointers = b - a
    if height[a] < height[b]:
      heighest_water_amount = max(height[a] * distance_between_pointers, heighest_water_amount)
      a += 1
    elif height[b] < height[a]:
      heighest_water_amount = max(height[b] * distance_between_pointers, heighest_water_amount)
      b -= 1
    else:
      if height[a] == height[b]:
        if height[a+1] > height[b-1]:
          heighest_water_amount = max(height[a] * distance_between_pointers, heighest_water_amount)
          a += 1
        else:
          heighest_water_amount = max(height[a] * distance_between_pointers, heighest_water_amount)
          b -= 1
  return int(heighest_water_amount)
# print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
# print(maxArea([1,1])) # 1
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

# 3 - longest substring without repeating characters - 
def lengthOfLongestSubstring(s):
  # 1. we create a dictionary to store all the substrings with a value to count how many times we have seen it.
  # 2. create two pointers to keep track of the substrings. [a = 0], [b = 0]
  # 3. while b != len(s)-1
  #   a. b++
  #   b. if the pointer b is the same as any previous characters:
  #       I. if dictionary[substring = pointer[a] to pointer[b]]:
  #         i. dictionary[substring = pointer[a] to pointer[b]] += 1
  #         i. a = b
  #       I. else: does not exist in dictionary
  #         i. dictionary[substring = pointer[a] to pointer[b]] = 1
  #         i. a = b
  # dic = {}
  # a, b = 0, 0
  # longest = 1
  # while b is not len(s):
  #   if s[b] in dic:
  #     a = max(a, dic[s[b]]+1)
  #   longest = max(longest, b - a + 1)
  #   dic[s[b]] = b
  #   b += 1
    # print(a, b, longest)
  # return longest

  charSet = set()
  l = 0
  res = 0
  for r in range(len(s)):
    while s[r] in charSet:
      charSet.remove(s[l])
      l += 1
    charSet.add(s[r])
    res = max(res, r - l + 1)
  return res
# print(lengthOfLongestSubstring("abcabcbb")) # 3
# print(lengthOfLongestSubstring("bbbbb")) # 1
# print(lengthOfLongestSubstring("pwwkew")) # 3

# 424 - longest Repeating Character Replacement - 
def characterReplacement(s, k):
  dic = {}
  res = 0
  l = 0
  for r in range(len(s)):
    dic[s[r]] = 1 + dic.get(s[r], 0) # increment or assaign the charcter in the dictionary.
    while (r-l+1) - max(dic.values()) > k: # checks if the window length is greater than our max length.
      dic[s[l]] -= 1
      l += 1
    res = max(res, r - l + 1)
  return res
# print(characterReplacement('ABAB', 2)) # 4
# print(characterReplacement('AABABBA', 1)) # 4

# 76 - Minimum Window SubString - 
def minWindow(s, t):
  if t == "": return ""
  countT, window = {}, {}
  for c in t:
    countT[c] = 1 + countT.get(c, 0)
  have, need = 0, len(countT)
  res, resLen = [-1, -1], float("infinity")
  l = 0
  for r in range(len(s)):
    c = s[r]
    window[c] = 1 + window.get(c, 0)
    if c in countT and window[c] == countT[c]:
      have += 1
    while have == need:
      # update our result
      if (r - l + 1) < resLen:
        res = [l, r]
        resLen = (r-l+1)
      # pop from the left of our window
      window[s[l]] -= 1
      if s[l] in countT and window[s[l]] < countT[s[l]]:
        have -= 1
      l += 1
  l, r = res
  return s[l:r+1] if resLen != float("infinity") else ""
# print(minWindow("ADOBECODEBANC", "ABC")) # "BANC"
# print(minWindow("a", "a")) # "a"
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
# 153 - Find Minimum in Rotated Sorted Array - Binary Search
def findMin(nums):
  res = nums[0]
  low = 0
  high = len(nums)-1
  while low <= high:
      if nums[low] < nums[high]:
        res = min(res, nums[low])
        break
      mid = (low + high) // 2
      res = min(res, nums[mid])
      if nums[mid] >= nums[low]:
        low = mid + 1
      else:
        high = mid - 1
  return res
# print(findMin([3,4,5,1,2])) # 1
# print(findMin([4,5,6,7,0,1,2])) # 0
# print(findMin([11,13,15,17])) # 11

# 33 - Search in Rotated Sorted Array - Binary Search
def search(nums, target):
  low = 0
  high = len(nums)-1
  while low <= high:
    mid = (low + high) // 2
    if target == nums[mid]:
      return mid
    # left sorted portion
    if nums[mid] >= nums[low]:
      if target > nums[mid] or target < nums[low]:
        low = mid + 1
      else:
        high = mid - 1
    # right sorted portion
    else:
      if target < nums[mid] or target > nums[high]:
        high = mid - 1
      else:
        low = mid + 1
  return - 1
# print(search([4,5,6,7,0,1,2], 0)) # 4
# print(search([4,5,6,7,0,1,2], 3)) # -1
# print(search([1], 0)) # -1
# print(search([1, 3, 5], 3)) # 1
# print(search([4,5,6,7,0,1,2], 5)) # 1
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

# 143 - Reorder List - Linked List | 
  def reorderList(self):
    # every positive position to be the linked list item
    # every odd item to be last item -n where n increments by 1 each time.

    # find middle
    slow, fast = self.head, self.head.next
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    second = slow.next
    prev = slow.next = None
    
    # reverse second half
    while second:
      temp = second.next
      second.next = prev
      prev = second
      second = temp
    
    # merge two half lists
    first, second = self.head, prev
    while second:
      temp1, temp2 = first.next, second.next
      first.next = second
      second.next = temp1
      first, second = temp1, temp2

# 19 - Remove Nth Node From End of List - Linked List | Two Pointers
  def removeNthFromEnd(self, n):
    # last = self.head
    # remove = self.head
    # count = 0
    # while last.next:
    #   last = last.next
    #   count += 1
    # if count == 1 and n == 1:
    #   count = 1
    # else:
    #   count = count - n
    # while count != 0:
    #   remove = remove.next
    #   count -= 1
    # remove.next = remove.next.next
    dummy = LLNode(0, self.head)
    left = dummy
    right = self.head
    while n > 0 and right:
      right = right.next
      n -= 1
    while right:
      left = left.next
      right = right.next
    left.next = left.next.next
    return dummy.next

# 23 - Merge k Sorted Lists - 
  def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
  
  def mergeList(self, l1, l2):
        dummy = LLNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

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

if __name__ == '__main__':
  ll = LinkedList()

{  # ?Reverse LL
  # ll.push(1)
  # ll.push(2)
  # ll.push(3)
  # ll.push(4)
  # ll.push(5)
  # ll.printList()
  # ll.reverseList() # [5,4,3,2,1]
  # ll.printList()

  # ?Merge two
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

  # ?Linked List Cycle
  # ll.addToList(20)
  # ll.addToList(4)
  # ll.addToList(15)
  # ll.addToList(10)
  # ll.head.next.next.next.next = ll.head
  # if(ll.hasCycle()):
  #   print('Loop Found')
  # else:
  #   print('No Loop')

  # ?Reorder List
  # ll.push(4)
  # ll.push(3)
  # ll.push(2)
  # ll.push(1)
  # ll.printList()
  # ll.reorderList()
  # ll.printList()

  # ?Remove Nth Node From End of List
  # ll.push(5)
  # ll.push(4)
  # ll.push(3)
  # ll.push(2)
  # ll.push(1)
  # ll.printList()
  # ll.removeNthFromEnd(3)
  # ll.printList()

  # ?Merge k Sorted Lists
  # ll1 = LinkedList()
  # ll1.push(1)
  # ll1.push(4)
  # ll1.push(5)
  # ll2 = LinkedList()
  # ll2.push(1)
  # ll2.push(3)
  # ll2.push(4)
  # ll3 = LinkedList()
  # ll3.push(2)
  # ll3.push(6)
  # ll = LinkedList()
  # ll.push([ll1])
  # ll.push([ll2])
  # ll.push([ll3])
  # ll.mergeKLists(ll)
  }
# ?Linked List =======================================

# ?Trees =======================================
# This creates our tree.
class TreeNode(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree(object):
  def __init__(self):
    self.root = None
  def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.value))
            self.printt(curr_node.right)
  def insert(self, value):
      new_node = TreeNode(value)
      if self.root == None:
        self.root = new_node
      else:
        curr = self.root
        while(curr):
          if(value < curr.value):
            if(curr.left == None):
              curr.left = new_node
              return
            else:
              curr = curr.left
          else:
            if(curr.right == None):
              curr.right = new_node
              return
            else:
              curr = curr.right

# 226 - Invert Binary Tree - Tree | DFS ..
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

# 104 - Maximum Depth of Binary Tree - Tree | DFS ..
  def maxDepth(self, root):
      if not root:
          return 0
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 100 - Same Tree - Tree | 
  def isSameTree(self, p, q):
      if not p and not q:
          return True
      if p is not None and q is not None:
          return ((p.value == q.value) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
      return False

# 573 - Subtree of Another Tree - Tree | 
  def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))

# 235 - Lowest Common Ancestor of a Binary Search Tree - Tree | ..
  def lowestCommonAncestor(self, root, p, q):
    # find the LCA of two nodes given by p and q.
    curr = root
    while curr:
      if p.value > curr.value and q.value > curr.value:
        curr = curr.right
      elif p.value < curr.value and q.value < curr.value:
        curr = curr.left
      else:
        return curr.value

# 102 - Binary Tree Level Order Traversal - Tree | ..
  def levelOrder(self, root):
    # if not root:
    #   return []
    # result = []
    # queue = [root]
    # while queue:
    #   node = queue.pop(0)
    #   result.append(node.value)
    #   if node.left:
    #     queue.append(node.left)
    #   if node.right:
    #     queue.append(node.right)
    # return result
    res = []
    q = [root]
    while q:
      qLen = len(q)
      level = []
      for i in range(qLen):
        node = q.pop(0)
        if node:
          level.append(node.value)
          q.append(node.left)
          q.append(node.right)
      if level:
        res.append(level)
    return res

if __name__ == '__main__':
  # myTree2 = BinarySearchTree()
  # myTree2.insert(2)
  # myTree2.insert(1)
  # myTree2.insert(4)
  # myTree2.insert(3)
  # myTree2.insert(5)
  myTree = BinarySearchTree()
  myTree.insert(2)
  myTree.insert(1)
  myTree.insert(4)
  myTree.insert(3)
  myTree.insert(5)
  myTree.printt(myTree.root)
  #     2
  #    / \
  #   1   4
  #      / \
  #     3   5

{
  # Inver Binary Tree
  # print(myTree.invertTree(myTree.root))

  # Maximum Depth of Binary Tree
  # print(myTree.maxDepth(myTree.root))

  # Same Tree
  # print(myTree.isSameTree(myTree.root, myTree2.root))

  # Subtree of Another Tree
  # print(myTree.isSubtree(myTree.root, myTree2.root))

  # Lowest Common Ancestor of a Binary Search Tree
  # print(myTree.lowestCommonAncestor(myTree.root, TreeNode(1), TreeNode(8)))

  # Binary Tree Level Order Traversal
  # print(myTree.levelOrder(myTree.root))
}
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
