const kMostFrequent = (nums, k) => {
  let map = {};
  nums.forEach(num => !map[num] ? map[num] = 1 : map[num]++);
  let keys = Object.keys(map);
  keys.sort((a, b) => map[b] - map[a]);
  return keys.slice(0,k).map(key => parseInt(key));
}

console.log(kMostFrequent([1, 6, 2, 1, 6, 1, 6], 2))
console.log(kMostFrequent([-1, -1], 2))

