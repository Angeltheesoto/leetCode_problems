// ARRAYS & HASHING -_-
// 217.Contains Duplicate
// Time Complexity = O(N)
// Space Complexity = O(N)
function containsDuplicate(nums) {
  // Hashmap solution
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    if (map[nums[i]] === undefined) {
      map[nums[i]] = [i];
    } else {
      return true;
    }
  }
  return false;
}

// console.log(containsDuplicate([1, 2, 3, 1])); // true
// console.log(containsDuplicate([1, 2, 3, 4])); // false
// console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])); // true
// console.log(containsDuplicate([2, 14, 18, 22, 22])); // true

// 242. Valid Anagram
function isAnagram(s, t) {
  // Time Complexity = NlogN + MlogM
  // Sorted solution----------------
  // s = s.split("").sort().join("");
  // t = t.split("").sort().join("");
  // if (s.length !== t.length) {
  //   return false;
  // }
  // for (let i = 0; i < s.length; i++) {
  //   if (s[i] !== t[i]) {
  //     return false;
  //   }
  // }
  // return true;
  // hashmap solution----------------
  // Time Complexity = O(N)
  if (s.length !== t.length) return false;
  const sCount = {};
  const tCount = {};
  const N = s.length;
  for (let i = 0; i < N; i++) {
    if (!sCount[s[i]]) sCount[s[i]] = 0;
    if (!tCount[t[i]]) tCount[t[i]] = 0;
    sCount[s[i]]++;
    tCount[t[i]]++;
  }
  // console.log(s, ":", sCount);
  // console.log(t, ":", tCount);
  for (let ch in sCount) {
    if (sCount[ch] !== tCount[ch]) return false;
  }
  return true;
}

// console.log(isAnagram("anagram", "nagaram")); // true
// console.log(isAnagram("rat", "car")); // false
// console.log(isAnagram("arc", "car")); // true
// console.log(isAnagram("a", "ab")); // false

// 1. Two Sum
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}

// console.log(twoSum([2, 7, 11, 15], 9)); // [0,1]
// console.log(twoSum([3, 2, 4], 6)); // [1,2]
// console.log(twoSum([3, 3], 6)); // [0,1]
// console.log(twoSum([2, 5, 5, 11], 10)); // [1,2]
