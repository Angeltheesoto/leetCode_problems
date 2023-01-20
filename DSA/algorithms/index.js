// ALGORITHMS

// Big-O Guide:
// O(1) - Calculation not dependent on the input size.
// O(N) - 1 Loop
// O(N^2) - 2 Loop
// O(logn) - Input size reduced by half.

// Day 7 - Fibonacci Sequence
// Big-O - O(N)

function Fibonacci(n) {
  let arr = [0, 1];
  for (let i = 2; i < n; i++) {
    arr[i] = arr[i - 1] + arr[i - 2];
  }
  return arr;
}

// console.log(Fibonacci(2));
// console.log(Fibonacci(3));
// console.log(Fibonacci(5));
// console.log(Fibonacci(7));

// Day 8 - Factorial of a number
// Big-O - O(N)

function Factorial(n) {
  let result = 1;
  for (let i = 2; i <= n; i++) {
    result = result * i;
  }
  return result;
}

// console.log(Factorial(0)); // 1
// console.log(Factorial(4)); // 24
// console.log(Factorial(5)); // 120

// Day 9 - Prime Number
// Big-O - O(N)

function isPrime(n) {
  if (n < 2) {
    return false;
  }
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

// console.log(isPrime(5)); // true
// console.log(isPrime(3)); // true
// console.log(isPrime(7)); // true
// console.log(isPrime(4)); // false
// console.log(isPrime(9)); // false

// Day 9 - Power of Two
// Big-O - O(logn)

function powerOfTwo(n) {
  if (n < 1) {
    return false;
  }
  while (n > 1) {
    if (n % 2 !== 0) {
      return false;
    }
    n = n / 2;
  }
  return true;
}

// console.log(powerOfTwo(1)); // true
// console.log(powerOfTwo(2)); // true
// console.log(powerOfTwo(5)); // false

// Day 11 - Recursion
// Big-O - O(N^2)

function recursiveFibonacci(n) {
  // base case
  if (n < 2) {
    return n;
  }
  // recursive case
  return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
}

// console.log(recursiveFibonacci(0)); // 0
// console.log(recursiveFibonacci(2)); // 1
// console.log(recursiveFibonacci(6)); // 8

// Day 13 - Recursion factorial of a number
// Big-O - O(n)

function recursiveFactorial(n) {
  if (n === 0) {
    return 1;
  }
  return n * recursiveFactorial(n - 1);
}

// console.log(recursiveFactorial(4)); // 4*3*2*1 = 24
// console.log(recursiveFactorial(5)); // 5*4*3*2*1 = 120
// console.log(recursiveFactorial(6)); // 6*5*4*3*2*1 = 720

// Day 15 - Linear search
// Big-O - O(N)

function linearSearch(n, t) {
  for (let i = 0; i < n.length; i++) {
    if (t === n[i]) {
      return i;
    }
  }
  return -1;
}

// console.log(linearSearch([-5, 2, 10, 4, 6], 10)); // 2
// console.log(linearSearch([-5, 2, 10, 4, 6], 6)); // 4
// console.log(linearSearch([-5, 2, 10, 4, 6], -1)); // -1

// Day 17 - Binary search
// Big-O - O(logN)

function binarySearch(n, target) {
  let low = 0;
  let high = n.length - 1;
  while (low <= high) {
    let mid = Math.floor((low + high) / 2);
    if (n[mid] === target) {
      return mid;
    }
    if (n[mid] > target) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }
  return -1;
}

// console.log(binarySearch([-5, 2, 4, 6, 10], 10)); // 4
// console.log(binarySearch([-5, 2, 4, 6, 10], 6)); // 3
// console.log(binarySearch([-5, 2, 4, 6, 10], 20)); // -1

// Day 18 - Recursive Binary search
// Big-O - O(logn)

function recursiveBinarySearch(n, l, r, t) {
  while (l <= r) {
    let mid = Math.floor((r + l) / 2);
    if (n[mid] === t) {
      return mid;
    }
    if (n[mid] > t) {
      return recursiveBinarySearch(n, l, mid - 1, t);
    } else {
      return recursiveBinarySearch(n, mid + 1, r, t);
    }
  }
  return -1;
}

let arr = [-5, 2, 4, 6, 10];
let low = 0;
let high = arr.length;

// console.log(recursiveBinarySearch(arr, low, high - 1, 10)); // 4
// console.log(recursiveBinarySearch(arr, low, high - 1, 6)); // 3
// console.log(recursiveBinarySearch(arr, low, high - 1, 20)); // -1

// Day 18 - Recursive Binary search
// Big-O - O(logn)

