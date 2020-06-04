const palindromePairs = (words) => {
  const reverser = (word) => {
    let arr = word.split('');
    let reversed = []
    arr.forEach(letter => {
      reversed.unshift(letter);
    });
    return (reversed.join('') === word) ? true : false;
  }
  let pairs = [];
  for (let i = 0; i < words.length; i++) {
    for (let j = 0; j < words.length; j++) {
      if (i !== j) {
        console.log(i, j);
        console.log(words[i], words[j]);
        if (reverser(words[i].concat(words[j]))) {
          pairs.push([i, j]);
        }
      }
    }
  }
  return pairs;
};
console.log(palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]));
console.log(palindromePairs(["bat", "tab", "cat"]));
