// let singleNumber = (nums) => {
//   let sorted = nums.sort()
//   for (let i = 0; i < sorted.length; i++) {
//     if (sorted[i] !== sorted[i - 1] && sorted[i] !== sorted[i + 1]) {
//       return sorted[i]
//     }
//   }
//   return sorted
// };

let singleNumber = nums => eval(nums.join('^'));

console.log('Answer: ', singleNumber([2,2,1]))
console.log('Answer: ', singleNumber([4,1,2,1,2]))
console.log(2^2^1)
console.log(4^1^2^1^2)