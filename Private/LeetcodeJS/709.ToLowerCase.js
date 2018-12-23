const toLowerCase = (str) => {
  let lower = '';
  for (let char of str) {
    lower += /[A-Z]/g.test(char) ? String.fromCharCode(char.charCodeAt(0) + 32) : char;
  }
  return lower;
};

console.log(toLowerCase("Hello"));
console.log(toLowerCase("here"));
console.log(toLowerCase("Lovely"));
