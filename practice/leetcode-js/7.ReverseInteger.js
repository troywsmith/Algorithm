var reverse = function(x) {
  let arr         = x.toString().split('').reverse();
  let sign        = (arr[arr.length - 1] === '-') ? -1 : 1;
  let result      = parseInt(arr.join('')) * sign;
  let overflow    = Math.pow(2, 31)
  return (result > overflow || result < overflow * -1) ? 0 : result;
}
console.log(reverse(123));
console.log(reverse(-1534236469));
