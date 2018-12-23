// --- Directions
// Print out the n-th entry in the fibonacci series.
// The fibonacci series is an ordering of numbers where
// each number is the sum of the preceeding two.
// For example, the sequence
//  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
// forms the first ten entries of the fibonacci series.
// Example:
//   fib(4) === 3

// brute force:
// function fib(n) {
//   let array = [0, 1];
//   for (let i=0; i<n; i++) {
//     array.push(array[array.length-1] + array[array.length-2]);
//   }
//   return array[array.length-2];
// }

// // iterative solution (runtime: linear)
// function fib(n) {
//   const s = [0, 1];
//   for (let i = 2; i <= n; i++) {
//     let a = s[i - 2];
//     let b = s[i - 1];
//     s.push( a + b );
//   }
//   return s[n];
// }

// // recursive solution (runtime: exponential)
// function fib(n) {
//   if (n < 2) {
//     return n;
//   }
//   return fib(n - 1) + fib(n - 2);
// }

// memoized recursive solution (runtime: )
function memoize(fn) {
  const cache = {};
  return function (...args) {
    if (cache[args]) {
      return cache[args];
    }

    const result = fn.apply(this, args);
    cache[args] = result;

    return result;
  };
}

function slowFib(n) {
  if (n < 2) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
}

const fib = memoize(slowFib);

module.exports = fib;
