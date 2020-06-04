evalRPN = (tokens) => {
  const obj = {
    '+': (a, b) => a + b, 
    '-': (a, b) => a - b, 
    '*': (a, b) => a * b, 
    '/': (a, b) => ~~(a / b)
  };
  let result = [];
  for (let thing of tokens) {
    if (obj[thing]) {
      let second = result.pop();
      let first = result.pop();
      let operation = obj[thing];
      result.push(operation(first, second));
    } else {
      result.push(Number(thing));
    }
  }
  return result[0];
}

let start = new Date;
console.log(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]));
let end = new Date;
console.log(end.getTime() - start.getTime() + ' ms');
