// factorial(n)

factorial = num => {
    if(num === 0 || num === 1)
      return 1;
    else if (num > 1) {
      return num * factorial(num - 1);
    } else if (num < 0) {
        return num * factorial(num + 1);
    } else
      return undefined;
  }
  
console.log(factorial(3));
console.log(factorial(0));
console.log(factorial(-3));