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

// Uses linked list Data Structure and Recursion algorithm
// var mergeTwoLists = function (list1, list2) {
//   // return [list1, list2];
//   let stack = [];

//   for (let i = 0; i < list1.length; i++) {
//     for (let j = 0; j < list2.length; j++) {
//       if (list1[i] === list2[j]) {
//         stack.push(list1[i], list2[j]);
//       }
//     }
//   }

//   const spreaded = [...list1, ...list2];
//   const nonMatches = spreaded.filter((el) => {
//     return !(list1.includes(el) && list2.includes(el));
//   });

//   let mid = stack[Math.floor((stack.length - 1) / 2)];
//   mid.push(nonMatches);

//   return stack;
// };

// console.log(mergeTwoLists([1, 2, 4], [1, 3, 4]));

// time complexity O(n+m)
// space complexity O(1)
function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}
var mergeTwoLists = function (list1, list2) {
  let curr = new ListNode(0);
  let head = curr;
  while (list1 && list2) {
    if (list1.val <= list2.val) {
      curr.next = list1;
      list1 = list1.next;
    } else {
      curr.next = list2;
      list2 = list2.next;
    }
    curr = curr.next;
  }
  if (list1 !== null) {
    curr.next = list1;
  } else {
    curr.next = list2;
  }
  return head.next;
};

// console.log(mergeTwoLists([1, 2, 4], [1, 3, 4]));
// mergeTwoLists([1, 2, 4], [1, 3, 4]);

// 26. Remove Duplicates from Sorted Array ----------------------------------------------------------

// var removeDuplicates = function (nums) {
//   uniq = [...new Set(nums)];
//   let numsLength = nums.length;
//   let newNumsLength = uniq.length;
//   let underscores = numsLength - newNumsLength;
//   for (let i = 0; i < underscores; i++) {
//     uniq.push("_")[i];
//   }
//   return uniq;
// };

var removeDuplicates = function (nums) {
  let index = 1;
  for (let i = 0; i < nums.length - 1; i++) {
    if (nums[i] !== nums[i + 1]) {
      nums[index] = nums[i + 1];
      index++;
    }
  }
  return index;
};

// console.log(removeDuplicates([1, 1, 2]));
// console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));

// 27. Remove Element ----------------------------------------------------------

/*
1. create index variable (starting at 0.)
2. Loop through index.
  a. Condition if current value doesn't equal "val".
    i. Set nums[index] to nums[i]
    ii. Increment index.
3. Return index
*/
var removeElement = function (nums, val) {
  let index = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== val) {
      nums[index] = nums[i];
      index++;
    }
  }
  return index;
};
// Time complexity - O(N)
// Space complexity - O(1)

// console.log(removeElement([3, 2, 2, 3], 3));
// console.log(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2));

// 58. Length of Last Word ----------------------------------------------------------

function lengthOfLastWord(s) {
  let newArr = s.split(" ");
  newArr = newArr.filter((el) => {
    return /\S/.test(el);
  });
  let lastIndex = newArr.pop();
  return lastIndex.length;
}
// console.log(lengthOfLastWord("Hello World")); // 5
// console.log(lengthOfLastWord("   fly me   to   the moon  ")); // 4
// console.log(lengthOfLastWord("luffy is still joyboy")); // 6
