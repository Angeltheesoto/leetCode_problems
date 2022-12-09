// Gravity Flip
function flip(d, a) {
  // return d + "\n" + a;
  return d === "R"
    ? a.sort(function (x, y) {
        return x - y;
      })
    : a.sort(function (x, y) {
        return y - x;
      });
}

// console.log(flip("R", [3, 2, 1, 2])); // [1, 2, 2, 3]
// console.log(flip("L", [1, 4, 5, 3, 5])); // [5, 5, 4, 3, 1]

// CHECK SAME CASE

function sameCase(a, b) {
  // if ((a.toUpperCase() == a) === (b.toUpperCase() == b)) {
  //   return 1;
  // } else if ((a.toUpperCase() == a) !== (b.toUpperCase() == b)) {
  //   return 0;
  // } else if (a == /[a-z]/i.test(a) || b == /[a-z]/i.test(b)) {
  //   return -1;
  // } else {
  //   return -1;
  // }

  if (
    a.toUpperCase() === a.toLowerCase() ||
    b.toLowerCase() === b.toUpperCase()
  ) {
    return -1;
  } else if (
    (a === a.toLowerCase() && b === b.toLowerCase()) ||
    (a === a.toUpperCase() && b === b.toUpperCase())
  ) {
    return 1;
  } else {
    return 0;
  }
}

// console.log(sameCase("C", "B")); // 1
// console.log(sameCase("b", "a")); // 1
// console.log(sameCase("d", "d")); // 1
// console.log(sameCase("A", "s")); // 0
// console.log(sameCase("c", "B")); // 0
// console.log(sameCase("b", "Z")); // 0
// console.log(sameCase("\t", "Z")); // - 1
// console.log(sameCase("H", ":")); // - 1
