const selfDividingNumbers = (left, right) => {
  let results = [];

  for (let i = left; i <= right; i++) {
    for (let each in i) {
      console.log(each);
    }  
  }

  return results;
};


console.log(selfDividingNumbers(1, 22));