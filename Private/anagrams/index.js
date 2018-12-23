// --- Directions
// Check to see if two provided strings are anagrams of eachother.
// One string is an anagram of another if it uses the same characters
// in the same quantity. Only consider characters, not spaces
// or punctuation.  Consider capital letters to be the same as lower case
// --- Examples
//   anagrams('rail safety', 'fairy tales') --> True
//   anagrams('RAIL! SAFETY!', 'fairy tales') --> True
//   anagrams('Hi there', 'Bye there') --> False

// function anagrams(stringA, stringB) {
//   // brute force 
//   function makeCharMap(str) {
//     const charMap = {};
//     let array = str
//     .replace(/[^\w]/g, '')
//     .toLowerCase()
//     .split('');
//     for (let char of array) {
//       charMap[char] ? charMap[char] += 1 : charMap[char] = 1;
//     }
//     return charMap;
//   };
//   const aMap = makeCharMap(stringA);
//   const bMap = makeCharMap(stringB);

//   result = [];
//   //first check to see if the lengths are equal 
//   // if they are not, end function and return false
//   if (Object.keys(aMap).length !== Object.keys(bMap).length) {
//     return false;
//   } 
//   //then compare the keys values
//   for (let char in aMap) {
//     if (aMap[char] !== bMap[char]) {
//       return false;
//     }
//   } 
//   return true;
// }

function anagrams(stringA, stringB) {
  // alternative solution:
  function cleanString(str) {
    return str
    .replace(/[^\w]/g, '')
    .toLowerCase()
    .split('')
    .sort()
    .join('');
  }
  return (cleanString(stringA) === cleanString(stringB)) ? true : false;
}

module.exports = anagrams;
