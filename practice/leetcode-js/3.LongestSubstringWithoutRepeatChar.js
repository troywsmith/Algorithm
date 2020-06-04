lengthOfLongestSubstring = (s) => {
  // start with first char
  // find index of next occurence of that char
  // subtract i from that index and return diff
  // repeat for all char in string
  let result = 0;
  let arr = [];
  for (var i = 0; i < s.length; i++) {
      arr = arr.slice(arr.indexOf(s[i]) + 1)
      result = Math.max(arr.push(s[i]), result)
  }
  return result
};

console.log(lengthOfLongestSubstring('abcabcbb'));
console.log(lengthOfLongestSubstring('bbbbb'));
console.log(lengthOfLongestSubstring('pwwkew'));
