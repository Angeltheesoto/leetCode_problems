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
class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
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
  // turn the string into an array
  let newArr = s.split(" ");
  // remove all the blank, spaces in the array
  newArr = newArr.filter((el) => {
    return /\S/.test(el);
  });
  // remove the last element in the array
  let lastIndex = newArr.pop();
  // return the last element
  return lastIndex.length;
}
// console.log(lengthOfLastWord("Hello World")); // 5
// console.log(lengthOfLastWord("   fly me   to   the moon  ")); // 4
// console.log(lengthOfLastWord("luffy is still joyboy")); // 6

// 66. Plus One ----------------------------------------------------------

// Without BigInt
function plusOne(digits) {
  let num = digits.join("");
  num = parseInt(num);
  num = num + 1;
  num = num.toString();
  num = num.split("");
  return num;
}
// With BigInt
function plusOne(digits) {
  // turn the array to a string
  let num = digits.join("");
  // turn the string to a Big number and add 1 to it
  num = BigInt(num);
  num = num + BigInt(1);
  // turn the string back to an array
  num = num.toString();
  num = num.split("");
  return num;
}

// console.log(plusOne([1, 2, 3])); // [1, 2, 4]
// console.log(plusOne([4, 3, 2, 1])); // [4, 3, 2, 2]
// console.log(plusOne([9])); // [1, 0]
// console.log(plusOne([6, 1, 4, 5, 3, 9, 0, 1, 9, 5, 1, 8, 6, 7, 0, 5, 5, 4, 3])); // [1, 0]

// 67. Add Binary ----------------------------------------------------------

// Binary addition - Rules
// 0 + 0 = 0
// 0 + 1 = 1
// 1 + 0 = 1
// 1 + 1 = 0, carry over the 1, i.e. 10

function addBinary(a, b) {
  // return (parseInt(a, 2) + parseInt(b, 2)).toString(2);
  // OR --
  let sum = "";
  let carry = 0;
  let i = a.length - 1;
  let j = b.length - 1;
  while (i >= 0 || j >= 0) {
    let A = a[i] ? a[i] : "0";
    let B = b[j] ? b[j] : "0";
    sum = String(A ^ B ^ carry) + sum;
    if (A === B && A !== String(carry)) {
      carry = Number(!carry);
    }
    i--;
    j--;
  }
  if (carry) {
    sum = String(carry) + sum;
  }
  return sum;
}

// console.log(addBinary("11", "1")); // 100
// console.log(addBinary("1010", "1011")); // '10101

// 69. Sqrt(x) ----------------------------------------------------------

function mySqrt(x) {
  // return Math.sqrt(x);
  // for (let i = 0; i <= x; i++) {
  //   if (x[i] ** 2 === x) {
  //     return x[i];
  //   }
  // }
  if (x <= 1) {
    return x;
  }
  for (let i = 2; i <= x; i++) {
    if (i * i === x) {
      return i;
    }
    if (i * i > x) {
      return i - 1;
    }
  }
}

// console.log(mySqrt(4)); // 2
// console.log(mySqrt(8)); // 2.82842... round to 2

// 70. Climbing Stairs ----------------------------------------------------------

// time complexity - O(n)
function climbStairs(n) {
  const memo = [1, 1, 2];
  for (let i = 3; i <= n; i++) {
    memo[i] = memo[i - 1] + memo[i - 2];
  }
  return memo[n];
}

// console.log(climbStairs(1));
// console.log(climbStairs(2));
// console.log(climbStairs(3));
// console.log(climbStairs(4));

// 83. Remove Duplicates from Sorted List ---------------------------------------------
// class Queue {
//   constructor(val, next) {
//     this.val = val === undefined ? 0 : val;
//     this.next = next === undefined ? null : next;
//   }
// }
// function ListNode(val, next) {
//   this.val = val === undefined ? 0 : val;
//   this.next = next === undefined ? null : next;
// }
function deleteDuplicates(head) {
  let dummy = new ListNode(-Infinity, head);
  let curr = head;
  let prev = dummy;

  while (curr) {
    if (curr.val === prev.val) {
      while (curr && curr.val === prev.val) {
        curr = curr.next;
      }
      prev.next = curr;
    } else {
      prev = curr;
      curr = curr.next;
    }
  }
  return dummy.next;
}
// console.log(deleteDuplicates([1, 1, 2]));
// console.log(deleteDuplicates([1, 1, 2, 3, 3]));

// 88. Merge Sorted Array ---------------------------------------------
// time complexity - O(m + n) = O(n)
function merge(nums1, m, nums2, n) {
  let first = n - 1;
  let second = n - 1;
  let i = m + n - 1;

  while (second >= 0) {
    let fVal = nums1[first];
    let sVal = nums2[second];

    if (fVal > sVal) {
      nums1[i] = fVal;
      i--;
      first--;
    } else {
      nums1[i] = sVal;
      i--;
      second--;
    }
  }
  return nums1;

  // return `Parameters are, nums1: ${nums1}, m: ${m}, nums2: ${nums2}, n: ${n} `;
  // const arr1 = nums1.slice(0, m);
  // const arr2 = nums2.slice(0, n);
  // for (let i = 0; i < arr2.length; i++) {
  //   arr1.push(arr2[i]);
  // }
  // for (let i = 0; i < arr1.length; i++) {
  //   for (let j = i + 1; j < arr1.length; j++) {
  //     if (arr1[i] > arr1[j]) {
  //       temp = arr1[i];
  //       arr1[i] = arr1[j];
  //       arr1[j] = temp;
  //     }
  //   }
  // }
  // return arr1;
}
// console.log(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)); // [1,2,2,3,5,6]
// console.log(merge([1], 1, [], 0)); // [1]
// console.log(merge([0], 0, [1], 1)); // [1]

// 94. Binary Tree Inorder Traversal ---------------------------------------------
// time complexity - O(-)

function inorderTraversal(root) {
  let node = root;
  const result = [];
  while (node) {
    if (node.left) {
      result.push(node.val);
      node = node.right;
    } else {
      const pred = findPredecessor(node);
      if (pred.right === node) {
        pred.right = nullresult.push(node.val);
        node = node.right;
      } else {
        pred.right = node;
        node = node.left;
      }
    }
  }
  return result;

  // let tourist = root;
  // let solution = [];

  // while (tourist !== null) {
  //   let guide = tourist.left;

  //   if (tourist.left !== null) {
  //     while (guide.right !== null && guide.right !== tourist) {
  //       guide = guide.right;
  //     }
  //     if (guide.right === null) {
  //       guide.right = tourist;
  //       tourist = tourist.left;
  //     } else {
  //       guide.right = null;
  //       solution.push(tourist.val);
  //       tourist = tourist.right;
  //     }
  //   } else {
  //     solution.push(tourist.val);
  //     tourist = tourist.right;
  //   }
  // }
  // return solution;
}

function findePredecessor(root) {
  let node = root.left;
  while (node.right && node.right !== root) {
    node = node.right;
  }
  return node;
}

console.log(inorderTraversal([1, null, 2, 3])); // [1,3,2]
console.log(inorderTraversal([])); // []
console.log(inorderTraversal([1])); // [1]
