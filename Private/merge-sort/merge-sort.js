arr = [3, 4, 8, 13, 1, 5, 6, 11];

const mergeSort = (arr) => {
  console.log('array: ' + arr);
  let n = arr.length;
  let mid = Math.floor(n / 2);
  let left = arr.slice(0, mid);
  let right = arr.slice(mid);
  //   console.log('mid: ' + mid);
  //   console.log('left: ' + left);
  //   console.log('right: ' + right);
  if (n <= 1) {
    return arr;
  }
  return merge(mergeSort(left), mergeSort(right));
}

//merge sorted areas
const merge = (left, right) => {
  let result = [];
  while (left.length > 0 && right.length > 0) {
    if (left[0] <= right[0]) {
      result.push(left.shift());
    } else {
      result.push(right.shift());
    }
  }
  while (left.length > 0) {
    result.push(left.shift());
  }
  while (right.length > 0) {
    result.push(right.shift());
  }
  return result;
}

console.log(mergeSort(arr));
