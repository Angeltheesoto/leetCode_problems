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
{
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

  // #557 - Reverse Words in a String III - Two Pointers | String
  function reverseWords(s) {
    s = s.split(" ");
    // AUTOMATICALLY
    // let newArr = s.map((e) => e.split("").reverse().join(""));
    // newArr = newArr.join(" ");

    // MANUALLY
    // console.log(s);
    let sLength = s.length;
    for (let i = 0; i < sLength; i++) {
      const word = s[i].split("");
      word.reverse();
      s[i] = word.join("");
    }
    console.log(s);
  }
  // reverseWords("Let's take LeetCode contest");
  // reverseWords("God Ding");

  // #832 - Flipping an Image - Two Pointers | Array | Matrix | Simulation
  function flipAndInvertImage(image) {
    console.log(image);
    let reverseImage = image.map((e) => e.reverse());
    for (let i = 0; i < reverseImage.length; i++) {
      // console.log(reverseImage[i]);
      let container = reverseImage[i];
      for (let j = 0; j < container.length; j++) {
        // console.log(container[j]);
        if (container[j] == 1) {
          container[j] = 0;
        } else {
          container[j] = 1;
        }
      }
    }
    console.log(reverseImage);
  }
  // flipAndInvertImage([
  //   [1, 1, 0],
  //   [1, 0, 1],
  //   [0, 0, 0],
  // ]); // [[1,0,0],[0,1,0],[1,1,1]]
  // flipAndInvertImage([
  //   [
  //     [1, 1, 0, 0],
  //     [1, 0, 0, 1],
  //     [0, 1, 1, 1],
  //     [1, 0, 1, 0],
  //   ],
  // ]); // [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

  // #2108 - Find First Palindromic String in Array - Two Pointers | Array | String

  function firstPalindrome(words) {
    // console.log(words);
    // create a variable to store the firstPalindrome
    // loop through the array going to each iteem.
    // - Then check if the item is a palindrome, if it is then add it to a variable
    // - if not, then move onto the next item until you reach the end of the array.
    let palindrome = [];
    for (let i = 0; i < words.length; i++) {
      let reverseWords = words[i].split("").reverse().join("");
      if (reverseWords == words[i]) {
        palindrome.push(words[i]);
      }
    }
    palindrome = palindrome[0];
    if (palindrome === undefined) {
      palindrome = "";
    }
    console.log(palindrome);
  }

  // firstPalindrome(["abc", "car", "ada", "racecar", "cool"]); //  "ada"
  // firstPalindrome(["notapalindrome", "racecar"]); // "racecar"
  // firstPalindrome(["def", "ghi"]); // ""

  // #2000 - Reverse Prefix of Word - Two Pointers | String

  function reversePrefix(word, ch) {
    let chIndex = word.indexOf(ch);
    // console.log(`Find index of ch: ${chIndex}`);
    if (chIndex < 0) return console.log(word);
    let result = "";
    for (let i = chIndex; i >= 0; i--) {
      // console.log(`Loop 1 steps: ${result}`);
      result += word[i];
    }
    for (let j = chIndex + 1; j < word.length; j++) {
      // console.log(`Loop 2 steps: ${result}`);
      result += word[j];
    }
    console.log(result);
  }
  // reversePrefix("abcdefd", "d"); // "dcbaefd"
  // reversePrefix("xyxzxe", "z"); // "zxyxxe"
  // reversePrefix("abcd", "z"); // "abcd"

  // #942 - DI String Match - Two Pointers | Array | String | Greedy

  function diStringMatch(s) {
    /*
  1. Create Low pointer.
  2. Create high pointer
  3. create size variable
  4. create output array.
  5. loop through S.
    a. Condition if current character is "I".
      i. Push in low pointer.
      ii. Increment low pointer.
    b. Else
      i. Push in high pointer.
      ii. Decrement high pointer.
  6. Return Output.
  */

    let low = 0;
    let high = s.length;
    let size = s.length + 1;
    let output = new Array(size);
    // console.log(output);
    for (let i = 0; i < size; i++) {
      if (s[i] === "I") {
        console.log(`Output steps if 'I': ${output}`);
        output[i] = low;
        low++;
      } else {
        console.log(`Output steps if 'D': ${output}`);
        output[i] = high;
        high--;
      }
    }
    console.log(output);
  }

  // diStringMatch("IDID"); // [0,4,1,3,2]
  // diStringMatch("III"); // [0,1,2,3]
  // diStringMatch("DDI"); // [3,2,0,1]

  // #1768 - Merge Strings Alternately - Two Pointers | String
  function mergeAlternately(word1, word2) {
    console.log(word1, word2);

    let i = 0;
    let j = 0;
    let combinedLength = word1.length + word2.length - 1;
    let result = [];

    while (combinedLength > 0) {
      if (i !== word1.length) {
        result.push(word1[i]);
        i++;
      }
      if (j !== word2.length) {
        result.push(word2[j]);
        j++;
      }
      combinedLength--;
    }
    console.log(result.join(""));
  }
  // mergeAlternately("abc", "pqr"); // "apbqcr"
  // mergeAlternately("ab", "pqrs"); // "apbqrs"
  // mergeAlternately("abcd", "pq"); // "apbqcd"

  // #344 - Reverse String - Two Pointers | String
  function reverseString(s) {
    s = s.reverse();
    console.log(s);
  }

  // reverseString(["h", "e", "l", "l", "o"]);
  // reverseString(["H", "a", "n", "n", "a", "h"]);

  // #1332 - Remove Palindromic Subsequences - Two Pointers | String
  function removePalindromeSub(s) {
    // console.log(s);
    /*
  prompt: return the min num of steps to make the given string empty.
    1. if s is a palindrome return 1
    2. create a store value that equals 0, to record the amount of steps taken to make the string empty.
    3. loop through the string to find if the string has a palindrome
      a. if it does, remove the palindrome and increment store by 1
      b. else if it does not, remove last index and increment store by 1.
  */

    let reverseString = s.split("").reverse().join("");
    if (!s) {
      console.log(0);
    }
    const isPalidrome = (s) => {
      let i = 0;
      let j = s.length - 1;
      const arr = s.split("");
      while (i < j) {
        if (arr[i] !== arr[j]) {
          return false;
        }
        j--;
        i++;
      }
      return true;
    };
    console.log(isPalidrome(s) ? 1 : 2);
  }
  // removePalindromeSub("");
  // removePalindromeSub("ababa"); // 1
  // removePalindromeSub("abb"); // 2
  // removePalindromeSub("baabb"); // 2
}

// Sliding Window problems ===============================
// Example:
{
  function maxSubArraySum(nums, size) {
    let currSum = 0;
    let maxSumSeen = -Infinity;

    for (let i = 0; i < nums.length; i++) {
      currSum += nums[i];
      if (i >= size - 1) {
        maxSumSeen = Math.max(currSum, maxSumSeen);
        currSum -= nums[i - (size - 1)];
      }
    }
    console.log(maxSumSeen);
  }

  const arr1 = [1, 2, 3, 5, 4, 8, 6, 2];
  // maxSubArraySum(arr1, 3);
}

{
  // #121 - Best Time to Buy and Sell Stock - Sliding Window | Array | Dynamic Programming
  function maxProfit(prices) {
    // console.log(prices);
    /*
      1. Create a variable to store the curr value, and a variable to store the maxProfit.
      2. Create a for loop to loop through prices array.
      3. Create a second for loop to loop through all other items.
        a. if arr[i]
          i. profit = arr2[j] - arr[i]
          i. maxProfit = Math.max(curr, maxProfit)
      4. return maxProfit
    */

    let buy = prices[0];
    let profit = 0;

    for (let i = 0; i < prices.length; i++) {
      if (buy > prices[i]) {
        buy = prices[i];
        prices[i] = 0;
      } else {
        console.log(`Buy: ${buy}, Profit: ${profit} `);
        profit = Math.max(prices[i] - buy, profit);
      }
    }
    console.log(profit);
  }
  // maxProfit([7, 1, 5, 3, 6, 4]); // 5
  // maxProfit([7, 6, 4, 3, 1]); // 0

  // #1876 - Substrings of Size Three with Distinct Characters - Sliding Window | Hash Table | String | Counting
  function countGoodSubstrings(s) {
    // console.log(s);
    /*
    1. create variables:
      a. for turning s into an array to be traversed.
      b. for counter to hold the amount of good substrings.
    2. create a forLoop for s.length
      a. if (i >= 2), console.log(s[i])
      b. else ...
    */
    let arr = s.split("");
    let curr;
    let count = 0;
    // console.log(arr);
    for (var i = 0; i < arr.length; i++) {
      if (arr[i + 2] != undefined) {
        curr = [arr[i], arr[i + 1], arr[i + 2]];
        if (
          arr[i] != arr[i + 1] &&
          arr[i] != arr[i + 2] &&
          arr[i + 1] != arr[i + 2]
        ) {
          count += 1;
        }
      }
    }
    console.log(count);
  }

  // countGoodSubstrings("xyzzaz"); // 1
  // countGoodSubstrings(" "); // 0
  // countGoodSubstrings("aababcabc"); // 4

  // #1763 - Longest Nice Substring - Sliding Window | Hash Table | String ...
  function longestNiceSubstring(s) {
    s = s.split(""); // turns string to array
    const stringLength = s.length; // length of string
    let max = ""; // return value

    for (let i = 0; i < stringLength - 1; i++) {
      // for loop
      let substr = [s[i]]; // loop through all items in string to make this.

      for (let j = i + 1; j < stringLength; j++) {
        // second for loop
        substr.push(s[j]);
        let isNice = true;

        for (const c of substr) {
          // similar to .map
          if (
            !substr.includes(c.toLowerCase()) ||
            !substr.includes(c.toUpperCase())
          ) {
            isNice = false;
          }
        }
        if (isNice && substr.join("").length > max.length) {
          max = substr.join("");
        }
      }
    }
    console.log(max);
  }
  // longestNiceSubstring("YazaAay"); // "aAa"
  // longestNiceSubstring("Bb"); // "Bb"
  // longestNiceSubstring("c"); //

  // #2379 - Minimum Recolors to Get K Consecutive Black Blocks - Sliding Window | String
  function minimumRecolors(blocks, k) {
    let temp = "B".repeat(k);
    if (blocks.indexOf(temp) !== -1) return 0;
    let count = Number.POSITIVE_INFINITY;
    for (let i = 0; i <= blocks.length - k; i++) {
      let tempCount = 0;
      for (let j = i; j < i + k; j++) {
        if (blocks[j] === "W") tempCount++;
      }
      count = Math.min(tempCount, count);
    }
    return count;
  }
  // minimumRecolors("WBBWWBBWBW", 7); // 3
  // minimumRecolors("WBWBBBW", 2); // 0

  // #2269 - Find the K-Beauty of a Number - Sliding Window | String
  function divisorSubstrings(num, k) {
    // console.log(num, k);
    /*
    1. create variables:
      a. let count = 0; this will increment the amount of k-beauty.
    2. create a for loop.
      a. if num[i] divide num has a remainder of 0. 
        i. increment count.
      b. return count
    */
    let curr = 0;
    let count = 0;
    let nums = Array.from(String(num));
    for (let i = 0; i < nums.length; i++) {
      console.log(nums[i]);
      // if (i >= k - 1 && i != undefined) {
      //   curr = num[i];
      //   console.log(curr);
      // }
    }
    // console.log(count);
  }
  // divisorSubstrings(240, 2); // 2
  // divisorSubstrings(430043, 2); // 2

  function toWindows(inputArray, size) {
    return inputArray.reduce((acc, _, index, arr) => {
      if (index + size > arr.length) {
        // we've reached the maximum number of windows, so don't add any more
        return acc;
      }
      // add a new window of [currentItem, maxWindowSizeItem)
      return acc.concat(
        // wrap in extra array, otherwise .concat flattens it
        [arr.slice(index, index + size)]
      );
    }, []);
  }
  const input = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  console.log(toWindows(input, 3));
}

// Stack problems ===============================

// Binary Search problems ===============================
