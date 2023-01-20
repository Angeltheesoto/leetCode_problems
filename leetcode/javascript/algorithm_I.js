// 704. Binary Search ----------------------------------------------------------

var search = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    if (target === nums[i]) {
      return nums.indexOf(nums[i]);
    }
  }
  return -1;
};

// console.log(search([-1, 0, 3, 5, 9, 12], 0));

// 278. First Bad Version ----------------------------------------------------------

function isBadVersion(num) {
  if (num >= 4) {
    return true;
  }
}

var solution = function (isBadVersion) {
  return function (n) {
    let start = 1;
    let end = n;
    while (start <= end) {
      let mid = Math.floor((start + end) / 2);
      if (isBadVersion(mid)) {
        end = mid - 1;
      } else {
        start = mid + 1;
      }
    }
    return start;
  };
};

// console.log(solution(isBadVersion)(3)); // false
// console.log(solution(isBadVersion)(5)); // true
// console.log(solution(isBadVersion)(4)); // true

// 35. Search Insert Position ----------------------------------------------------------

// Psuedocode--
// go through the given array
// if the target is equal to an item in the array return the index
// else return where the index would be at that target number

// space complexity - O(1)
// time complexity - O(logn)
var searchInsert = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;
  if (target < nums[left]) return 0;
  if (target > nums[right]) return nums.length;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (target === nums[mid]) return mid;
    else if (target < nums[mid]) right = mid - 1;
    else left = mid + 1;
  }
  return left;
};

console.log(searchInsert([1, 2, 5, 6], 5)); // 2
console.log(searchInsert([1, 2, 5, 6], 2)); // 1
console.log(searchInsert([1, 2, 5, 6], 7)); // 4
console.log(searchInsert([1, 2, 5, 6], 3)); // 2
console.log(searchInsert([1, 2, 5, 6], 4)); // 2
