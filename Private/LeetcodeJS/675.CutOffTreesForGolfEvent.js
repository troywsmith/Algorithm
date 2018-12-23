const cutOffTree = (forest) => {
  // if (forest[0][0] === 1) {
  //   return -1;
  // };
  let steps = 0;

  for (let i = 0; i < forest.length; i++) {

    // top row
    if (forest[0][i] < forest[0][i+1]) {
      forest[0][i] = 0;
      steps++;
    }
  };

  
  if (forest[0][forest.length - 1] < forest[1][forest.length - 1]) {
    forest[0][forest.length - 1] = 0;
    steps++;
  }
  console.log(forest);

  return steps;
}


console.log(cutOffTree(
  [
  [2,3,4],
  [0,0,5],
  [8,7,6]
  ]
));