const removeDuplicates = (nums) => {
  for (let i = 0; i < nums.length; i++) {
      while (nums[i] === nums[i + 1]) {
        nums.splice(i + 1, 1);
      }
  }
  return nums.length;
};

// const removeDuplicates = (nums) => {
//   let map = {};
//   for (let n of nums) {
//     map[n] ? map[n] += 1 : map[n] = 1;
//   }
//   return Object.keys(map).length;
// };

console.log(removeDuplicates([1,1,2]));
console.log(removeDuplicates([0,0,1,1,1,2,2,3,3,4]));