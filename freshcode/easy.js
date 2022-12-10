// This is my own leetcode practice with specific tags first from easy to medium to hard. Stars mean i solved with no help.tag=array, difficulty=easy, acceptence=high%
// #number - title - tags
// Array / HashTable problems ===============================
// #1920 - Build Array from Permutation - Array | Simulation

function buildArray(nums) {
  let ans = [];
  for (let i = 0; i < nums.length; i++) {
    ans.push(nums[nums[i]]);
  }
  return ans;
}
// console.log(buildArray([0, 2, 1, 5, 3, 4])); // [0,1,2,4,5,3]
// console.log(buildArray([5, 0, 1, 2, 3, 4])); // [4,5,0,1,2,3]
// console.log(buildArray([0, 1, 2, 3]));

// #1929 - Concatenation of Array - Array
function getConcatenation(nums) {
  let ans = [];
  let ans2 = ans.concat(nums, nums);
  return ans2;
}
// console.log(getConcatenation([1, 2, 1])); // [1,2,1,1,2,1]
// console.log(getConcatenation([1, 3, 2, 1])); // [1,3,2,1,1,3,2,1]

// #1480 - Running Sum of 1d Array - Array | Prefix Sum
function runningSum(nums) {
  // Loop through each item in the array.
  // if at index 1 return index 1
  // else if index is greater than 1, add up all elements before it.
  // store all the elements in an array and return it.

  let arr = [];
  let store = 0;
  for (let i = 0; i < nums.length; i++) {
    store = store + nums[i];
    // console.log(store);
    arr.push(store);
  }
  console.log(arr);
}
// runningSum([1, 2, 3, 4]); // [1,3,6,10]
// runningSum([1, 1, 1, 1, 1]); // [1,2,3,4,5]
// runningSum([3, 1, 2, 10, 1]); // [3,4,6,16,17]

// #2011 - Final Value of Variable After Performing Operations - Array | String | Simulation
function finalValueAfterOperations(operations) {
  let x = 0;
  for (let i = 0; i < operations.length; i++) {
    if (operations[i] === "--X" || operations[i] === "X--") {
      // console.log(operations[i]);
      x = x - 1;
    } else {
      x = x + 1;
    }
  }
  // console.log(x);
}
// finalValueAfterOperations(["--X", "X++", "X++"]); // 1
// finalValueAfterOperations(["++X", "++X", "X++"]); // 3
// finalValueAfterOperations(["X++", "++X", "--X", "X--"]); // 0

// #1470 - Shuffle the Array - Array
function shuffle(nums, n) {
  // console.log(nums);
  let arr = [];
  let numOne = nums.slice(0, n);
  let numTwo = nums.slice(n, nums.length);
  for (let i = 0; i < numOne.length; i++) {
    arr.push(numOne[i]);
    arr.push(numTwo[i]);
  }
  // console.log(arr);
}
// shuffle([2, 5, 1, 3, 4, 7], 3); // [2,3,5,4,1,7]
// shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4); // [1,4,2,3,3,2,4,1]
// shuffle([1, 1, 2, 2], 2); // [1,2,1,2]

// #1512 - Number of Good Pairs - Array | Hash Table | Math | Counting
function numIdenticalPairs(nums) {
  // console.log(nums);
  // set a variable called goodPairs equal to 0
  // loop through the array nums
  // at each index compare every other index after it
  // if the index num matches, add 1 to goodPairs
  // when the loop is finished return the variable goodPairs
  let goodPairs = 0;
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (nums[i] === nums[j] && i < j) {
        goodPairs = goodPairs + 1;
      }
    }
  }
  // console.log(goodPairs);
}
// numIdenticalPairs([1, 2, 3, 1, 1, 3]); // 4
// numIdenticalPairs([1, 1, 1, 1]); // 6
// numIdenticalPairs([1, 2, 3]); // 0

// #1672 - Richest Customer Wealth - Array | Matrix
function maximumWealth(accounts) {
  // var store = 0;
  // run a for loop accounts
  // var sum = 0;
  // run a for loop;
  // we will add sum + acc[i]
  // use a method in js to find max num;
  let storeMaxValue = 0;
  for (let i = 0; i < accounts.length; i++) {
    let innerArray = accounts[i];
    let sum = 0;
    for (let j = 0; j < innerArray.length; j++) {
      sum = sum + innerArray[j];
      // console.log(sum);
    }
    storeMaxValue = Math.max(storeMaxValue, sum);
  }
  // return storeMaxValue;
  console.log(storeMaxValue);
}
maximumWealth([
  [1, 2, 3],
  [3, 2, 1],
]); // 6
maximumWealth([
  [1, 5],
  [7, 3],
  [3, 5],
]); // 10
maximumWealth([
  [2, 8, 7], // 17
  [7, 1, 3], // 11
  [1, 9, 5], // 15
]); // 17 //    43

// Two Pointers problems ===============================

// Sliding Window problems ===============================

// Stack problems ===============================

// Binary Search problems ===============================
