function printNumber(n) {
  // base case:
  if (n===0) {
    return;
  }
  console.log(n);
  printNumber(n-1);
}
printNumber(10);