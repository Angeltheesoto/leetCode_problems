// #number - title - tags
// tag=array, difficulty=easy, acceptence=highpercent

// Array / HashTable problems ===============================
{
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
    return storeMaxValue;
    // console.log(storeMaxValue);
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

  // #2114 - Maximum Number of Words Found in Sentences - Array | String
  function mostWordsFound(sentences) {
    let maxSentenceValue = 0;
    for (let i = 0; i < sentences.length; i++) {
      // /(\w+) regex = look for all words
      // /g regex = dont stop after one
      let wordCount = sentences[i].match(/(\w+)/g).length;
      maxSentenceValue = Math.max(maxSentenceValue, wordCount);
    }
    // console.log(maxSentenceValue);
  }
  // mostWordsFound([
  //   "alice and bob love leetcode",
  //   "i think so too",
  //   "this is great thanks very much",
  // ]); // 6
  // mostWordsFound(["please wait", "continue to fight", "continue to win"]); // 3

  // #1431 - Kids With the Greatest Number of Candies - Array
  function kidsWithCandies(candies, extraCandies) {
    let max = Math.max(...candies);
    for (let i = 0; i < candies.length; i++) {
      if (candies[i] + extraCandies >= max) {
        candies[i] = true;
      } else {
        candies[i] = false;
      }
    }
    console.log(candies);
  }

  // kidsWithCandies([2, 3, 5, 1, 3], 3); // [true,true,true,false,true]
  // kidsWithCandies([4, 2, 1, 1, 2], 1); // [true,false,false,false,false]
  // kidsWithCandies([12, 1, 12], 10); // [true,false,true]

  // #1365 - How Many Numbers Are Smaller Than the Current Number - Array | Hash Table | Sorting | Counting
  function smallerNumbersThanCurrent(nums) {
    let output = [];
    for (let i = 0; i < nums.length; i++) {
      let count = 0;
      for (let j = 0; j < nums.length; j++) {
        if (nums[i] > nums[j]) {
          count = count + 1;
        }
      }
      output.push(count);
    }
    console.log(output);
  }

  // smallerNumbersThanCurrent([8, 1, 2, 2, 3]); // [4,0,1,1,3]
  // smallerNumbersThanCurrent([6, 5, 4, 8]); // [2,1,0,3]
  // smallerNumbersThanCurrent([7, 7, 7, 7]); // [0,0,0,0]
}
// Two Pointers problems ===============================

// #125 - Valid Palindrome - Two Pointers | String
function isPalidrome(s) {
  s = s.replace(/\s/g, "");
  let string = s.replace(/[^a-zA-Z0-9 ]/g, "").toLowerCase();
  let reverseString = string.split("").reverse().join("").toLowerCase();
  if (string !== reverseString) {
    console.log(false);
  } else {
    console.log(true);
  }
}
// isPalidrome("A man, a plan, a canal: Panama"); // true
// isPalidrome("race a car"); // false
// isPalidrome(" "); // true
// isPalidrome("0P"); // false

// #2367 - Number of Arithmetic Triplets - Two Pointers | Hash Table | Array | Enumeration

function arithmeticTriplets(nums, diff) {
  // console.log(nums, diff);
  /*
  I. Create a newArray, and store the last index of nums in it.
  II. Take the last num in nums and subtract it with each item in the array going backwards.
  III. If one of the nums in nums[i - 1] - nums[i] = diff, change last index to nums[i] and add it to the newArray. Continue the process untill the index reaches 0.
  */

  let count = 0;
  const reverseArray = nums.reverse();
  for (let i = 0; i < reverseArray.length; i++) {
    for (let j = 0; j < reverseArray.length; j++) {
      for (let k = 0; k < reverseArray.length; k++) {
        if (
          reverseArray[i] - nums[j] == diff &&
          reverseArray[j] - reverseArray[k] == diff
        ) {
          count += 1;
        }
      }
    }
  }
  console.log(reverseArray);
  console.log(count);
}
// arithmeticTriplets([0, 1, 4, 6, 7, 10], 3); // 2
// arithmeticTriplets([4, 5, 6, 7, 8, 9], 2); // 2

// #557 - Reverse Words in a String III - Two Pointers |

// Sliding Window problems ===============================

// Stack problems ===============================

// Binary Search problems ===============================
