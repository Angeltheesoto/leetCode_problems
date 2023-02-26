// https://www.youtube.com/watch?v=fAAZixBzIAI
// Binary Tree
// 1. At most 2 children per node.
// 2. Exactly 1 root.
// 3. Exactly 1 path b/w root and any node.

// Deapth First Search
class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

// iterative approach
// const depthFirstValues = (root) => {
//   if (root == null) return [];
//   // console.log(root);
//   const result = [];
//   const stack = [root];
//   while (stack.length > 0) {
//     const curr = stack.pop();
//     // console.log(curr.val);
//     result.push(curr.val);
//     if (curr.right) {
//       stack.push(curr.right);
//     }
//     if (curr.left) {
//       stack.push(curr.left);
//     }
//   }
//   console.log(result);
// };

// Recursive
const depthFirstValues = (root) => {
  if (root == null) return [];
  const leftValues = depthFirstValues(root.left);
  const rightValues = depthFirstValues(root.right);
  return [root.val, ...leftValues, ...rightValues];
  // console.log(...leftValues);
};

// Test_01
//      a
//    /  \
//   a    c
//  / \    \
// d  e     f
const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");
a.left = b;
a.right = c;
b.left = d;
b.right = e;
c.right = f;
// depthFirstValues(a); // [a, b, d, e, c, f]
depthFirstValues(["a", "b", "c", "d", "e", "f"]);
