// 1. Two Sum -----------------------------------------------------------------

// time complexity = O(N^2) = cubic = because theres two loops.
// space complexity = O(1) = constant = because your not alocating any extra memory to solve the problem.
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
};
// We want j = i + 1 because else elements will compare to itself, [0,0], [1,1]. We will compare it to different pairs because we also cant have the same index two times.

// time complexity = O(N) = linear
// space complexity = O(N) = linear
var twoSum = function (nums, target) {
  let map = {};
  for (let i = 0; i < nums.length; i++) {
    let value = nums[i];
    let complementPair = target - value;
    if (map[complementPair] !== undefined) {
      return [map[complementPair], i];
    } else {
      map[value] = i;
    }
  }
};
// Hash maps space complexities are linear.
/*
map = {}
i = 0
value = 1
complement_pair = 10 - 1 = 9
*/

// console.log(twoSum([1, 2, 3], 5)); // return [1, 2]
// console.log(twoSum([2, 7, 11, 15], 9)); // return [0, 1]
// console.log(twoSum([3, 2, 4], 6)); // return [1, 2]
// console.log(twoSum([3, 3], 6)); // return [0, 1]

// ? -----------------------------------------------------------------
