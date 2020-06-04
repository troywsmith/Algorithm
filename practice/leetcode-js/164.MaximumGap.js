const maximumGap = (nums) => {
  if (nums.length < 2) {
    return 0;
  }
  nums.sort(function(a,b) { return a - b; });  
  let diffs = [];
  for (let i = 0; i < nums.length - 1; i++) {
    diffs.push(nums[i+1] - nums[i]);
  }
  return Math.max(...diffs);
};

console.log(maximumGap([3, 6, 9, 1]));
console.log(maximumGap([10]));
console.log(maximumGap([1, 3, 100]));