// --- Directions
// Given a string, return the character that is most
// commonly used in the string.
// --- Examples
// maxChar("abcccccccd") === "c"
// maxChar("apple 1231111") === "1"

function maxChar(str) {
  
  //// solution 1:
  // const charMap={};
  // for (let char of str) {
  //   charMap[char] ? charMap[char] += 1 : charMap[char] = 1;
  // }
  // let arr = Object.values(charMap);
  // let max = Math.max(...arr);
  // return Object.keys(charMap).find(key => charMap[key] === max);

  // solution 2:
  const charMap={};
  let max = 0;
  let maxChar = '';

  for (let char of str) {
    charMap[char] ? charMap[char] += 1 : charMap[char] = 1;
  }

  for (let char in charMap) {
    if (charMap[char] > max) {
      max = charMap[char];
      maxChar = char;
    }
  }

  return maxChar;
}

// console.log(maxChar("apple 1231111"));
module.exports = maxChar;