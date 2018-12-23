const peakIndexInMountainArray = (A) => {
  return A.indexOf(Math.max(...A));
};

console.log(peakIndexInMountainArray([0, 1, 0]));
console.log(peakIndexInMountainArray([0, 2, 1, 0]));