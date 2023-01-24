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
# my solution
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


# 1512 - Number of Good Pairs - Array | Hash Table | Math | Counting
def numIdenticalPairs(nums):

  # good_pairs = []
  # for i in range(len(nums)):
  #   for j in range(len(nums)):
  #     if nums[i] == nums[j] and i < j:
  #       good_pairs.append([i,j])
  # print(len(good_pairs))

  hashmap = {}
  count = 0
  for i in nums:
    if i in hashmap:
      count += hashmap[i]
      hashmap[i] += 1
    else:
      hashmap[i] = 1
  print(count)



numIdenticalPairs([1,2,3,1,1,3])
# numIdenticalPairs([1,1,1,1])
# numIdenticalPairs([1,2,3])