// Write a function to find the longest common prefix string amongst an array of strings.
// If there is no common prefix, return an empty string "".

const longestCommonPrefix = (strs) => {
  let prefix = "";
  let example = strs[0];
  for (let word of strs) {
    for (let i = 0; i < word.length; i++) {
      console.log(word[i]);
      if (example[i] !== word[i]) {
        prefix = example.slice(0, i);
        return prefix;
      }
    }
  }
  return prefix;
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
console.log(longestCommonPrefix(["dog","racecar","car"]));
