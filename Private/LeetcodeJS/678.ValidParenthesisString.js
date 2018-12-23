checkValidString = (s) => {
  let ends = [];
  let result = [];
  if (s === ' ') {
    return true;
  }
  if (s[0] === ')') {
    return false;
  }
  for (let i = 0; i < s.length / 2; i++) {
    ends.push(s[i] + s[s.length - 1 - i]);
  }
  let re = /\(\)|\(\*|\*\)|\*\*/;
  ends.forEach(elem => {
    if (!re.test(elem)) {
      result.push(false);
    }
  })
  return result.includes(false) ? false : true;
};
// '()', '**', '(*', '*)'
console.log(checkValidString("()"));
console.log(checkValidString("(*)"));
console.log(checkValidString("(*()"));
console.log(checkValidString("((((*))"));
