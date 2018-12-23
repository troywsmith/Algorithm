// --- Directions
// Given a string, return true if the string is a palindrome
// or false if it is not.  Palindromes are strings that
// form the same word if it is reversed. *Do* include spaces
// and punctuation in determining if the string is a palindrome.
// --- Examples:
//   palindrome("abba") === true
//   palindrome("abcdefg") === false

function palindrome(str) {

  // // solution 1:
  // let reversed = str
  //   .split('')
  //   .reduce( (reverse, char) => {
  //   return char + reverse
  // }, '');
  // return reversed === str;

  // solution 2:
  return str
  .split('')
  .every( (char, i) => {
    return char === str[str.length - i -1]
  }
  );


}


// console.log(palindrome('abba'));
// console.log(palindrome('abcdefg'));
module.exports = palindrome;
