const maxCoins = (nums) => {
  let points = 0;
  for (let i = 0; i < nums.length; i++) {
    while (nums[i - 1] && nums[i + 1]) {
      points += (nums[i - 1] * nums[i] * nums[i + 1])
      nums.splice(i, 1);
    }
  }
  while (nums.length) {
    let i = 0;
    if (nums[i - 1]) {
      points += (nums[i] * nums[i - 1]);
      nums.splice(i, 1);
    } else if (nums[i + 1]) {
      points += (nums[i] * nums[i + 1]);
      nums.splice(i, 1);
    } else {
      points += nums[i];
      nums.splice(i, 1);
    }
    i++
  }
  return points;
}

console.log(maxCoins([3, 1, 5, 8]));