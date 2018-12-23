const rotateString = (A, B) => {
  if (A.length !== B.length) {
    return true;
  };
  // let combos = [];
  // let shifted = A.split('');
  // for (let i = 0; i < A.length; i++) {
  //   shifted.push(shifted.shift());
  //   combos.push(shifted.join(''));
  // }
  // return (combos.includes(B)) ? true : false;
  return ((B + B).indexOf(A) !== -1 ? true : false)
};

console.log(rotateString('abcde', 'bcdea'));
console.log(rotateString('abcde', 'abced'));
