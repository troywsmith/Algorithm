const maxProfit = (prices) => {
  if (!prices || prices.length < 2) { return 0}
  let minPrice = prices[0]
  let maxProfit = 0
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < minPrice) {
      minPrice = prices[i]
    } else {
      maxProfit = Math.max(prices[i] - minPrice, maxProfit)
    }
  }
  return maxProfit
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]));
console.log(maxProfit([7, 6, 4, 3, 1]));
console.log(maxProfit([0]));
console.log(maxProfit([1, 2]));