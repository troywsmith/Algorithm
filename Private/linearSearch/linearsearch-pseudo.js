arr = [6, 7, 8, 9, 10, 14, 15, 17, 19, 22, 23, 25, 30]
// linear_search(array, 10) => true
// linear_search(array, 13) => false

function linsearch(array, target) {
  for (let i = 0; i < array.length; i++) {
    if (target === array[i]) {
      console.log(true);
      return true;
    }
  }
  console.log(false);
  return false;
}

linsearch(arr, 10);
