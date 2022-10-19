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

// 9. Palindrome Number ---------------------------------------------------------------

var isPalindrome = (x) => {
  let numReverse = String(x).split("").reverse().join("");
  if (x == numReverse) {
    return true;
  } else {
    return false;
  }
};
// console.log(isPalindrome(121)); // true
// console.log(isPalindrome(-121)); // false
// console.log(isPalindrome(102)); // false

// How to find the middle index of a number -
// function extractMiddle(str) {
//   var position;
//   var length;
//   if (str.length % 2 == 1) {
//     position = str.length / 2;
//     length = 1;
//   } else {
//     position = str.length / 2 - 1;
//     length = 2;
//   }
//   return str.substring(position, position + length);
// }
// console.log(extractMiddle("12345"));

// 13. Roman to Integer ---------------------------------------------------------------

var romanToInt = function (s) {
  const map = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let res = 0;
  s.split("").forEach((num, i) => {
    if (map[num] < map[s[i + 1]]) {
      res -= map[num];
    } else {
      res += map[num];
    }
  });
  return res;
};
// console.log(romanToInt("III")); // return 3
// console.log(romanToInt("LVIII")); // return 58
// console.log(romanToInt("MCMXCIV")); // return 1994

// 14. Longest Common Prefix ----------------------------------------------------------

var longestCommonPrefix = function (strs) {
  // prefx = ''
  // loop through characters (char, index)
  // loop through strs(str)
  // if str[index] !== char
  // return prefix
  // prefix = prefix + char
  // return prefix
  let prefix = "";
  if (strs.length === 0) return prefix;
  for (let i = 0; i < strs[0].length; i++) {
    const character = strs[0][i];
    for (let j = 0; j < strs.length; j++) {
      if (strs[j][i] !== character) return prefix;
    }
    prefix = prefix + character;
  }
  return prefix;
};

// var longestCommonPrefix = function (strs) {
//   let prefix = strs[0];
//   for (let i = 1; i < strs.length; i++) {
//     while (strs[i].indexOf(prefix) !== 0) {
//       prefix = prefix.substring(0, prefix.length - 1);
//     }
//   }
//   return prefix;
// };

// console.log(longestCommonPrefix(["flower", "flow", "flight"])); // 'fl'
// console.log(longestCommonPrefix(["dog", "docecar", "dor"])); // ''

// 20. Valid Parentheses ----------------------------------------------------------

// time complexity O(N) - because we have to iterate through every single character in the string.
// space complexity O(N) - because
var isValid = function (s) {
  let stack = [];
  let hashMap = {
    "(": ")",
    "[": "]",
    "{": "}",
  };

  for (let ch of s) {
    if (hashMap[ch]) {
      // ch is an opening bracket
      stack.push(hashMap[ch]);
    } else if (stack.length > 0 && stack[stack.length - 1] === ch) {
      // ch is a closing bracket and top of stack matches
      stack.pop();
    } else {
      // ch is a closing bracket and top of the stack doesn't match
      return false;
    }
  }
  return stack.length === 0;
};

// console.log(isValid("()")); // True
// console.log(isValid("()[]{}")); // True
// console.log(isValid("(]")); // False
// console.log(isValid("(){}}{")); // False
// console.log(isValid("([]){")); // False
// console.log(isValid("{[]}")); // True

// 21. Merge Two Sorted Lists ----------------------------------------------------------

var mergeTwoLists = function (list1, list2) {};

console.log(mergeTwoLists([1, 2, 4], [1, 3, 4]));
