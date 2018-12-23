const partition = (s) => {
  let result = [];
  // deal with case that all letters by itself are palindromes
  result.push(s.split(''));

  let charMap = {};
  for (let char of s) {
    // console.log(char);
    (charMap[char]) ? charMap[char] += 1 : charMap[char] = 1;
  }

  // deal with all letters that have > 1 occur are palindromes
  for (let i = 0; i < charMap.length; i++) {
    if (charMap[i] > 1) {
      let curr = [char.repeat(charMap[i])];
      console.log(curr);
    }
  }

  const reverser = (str) => {
    return str.split('').reverse().join('');
  }
  console.log(reverser(s));

  // console.log(charMap);

  return result;
}

console.log(partition("aab"));