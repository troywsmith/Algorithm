// --- Directions
// Write a function that returns the number of vowels
// used in a string.  Vowels are the characters 'a', 'e'
// 'i', 'o', and 'u'.
// --- Examples
//   vowels('Hi There!') --> 3
//   vowels('Why do you ask?') --> 4
//   vowels('Why?') --> 0

// // iterative solution
// function vowels(str) {
//   let count = 0;
//   for (let i = 0; i < str.length; i++) {
//     if (/[aeiou]/i.test(str[i])) {
//       count ++;
//     }
//   }
//   return count;
// }

// condense solution
function vowels(str) {
  const matches = str.match(/[aeiou]/gi);
  return matches ? matches.length : 0;
}

// console.log(vowels('Why do you ask?'));
module.exports = vowels;