# number - title - tags
# tag=array\hashtable, difficulty=easy, acceptence=high_percent

# Array / HashTable problems ===============================

# 1512 - Number of Good Pairs - Array | Hash Table | Math | Counting
def numIdenticalPairs(nums):

  # time complexity - O(n^2)
  # good_pairs = []
  # for i in range(len(nums)):
  #   for j in range(len(nums)):
  #     if nums[i] == nums[j] and i < j:
  #       good_pairs.append([i,j])
  # print(len(good_pairs))

  # time complexity - O(n)
  hashmap = {}
  count = 0
  for i in nums:
    if i in hashmap:
      count += hashmap[i]
      hashmap[i] += 1
    else:
      hashmap[i] = 1
  print(count)

# numIdenticalPairs([1,2,3,1,1,3])
# numIdenticalPairs([1,1,1,1])
# numIdenticalPairs([1,2,3])

# 1365 - How Many Numbers Are Smaller Than the Current Number - Array | Hash table | Sorting | Counting

def smallerNumbersThanCurrent(nums):
  # time complexity - O(n)
  sortednums = sorted(nums)
  dict = {}
  output = []
  for i in range(len(sortednums)):
    if sortednums[i] not in dict:
      dict[sortednums[i]] = i
  for i in nums:
    output.append(dict[i])
  print(output)

# smallerNumbersThanCurrent([8,1,2,2,3])
# smallerNumbersThanCurrent([6,5,4,8])
# smallerNumbersThanCurrent([7,7,7,7])

# Two pointers ===============================

# 125 - Valid Palindrome - Two Pointers | String



