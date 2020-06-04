isPalindrome =(x) => {
  return parseInt(x.toString().split('').reverse().join('')) === x ? true : false;
};

console.log(isPalindrome(121));
console.log(isPalindrome(-121));
console.log(isPalindrome(10));