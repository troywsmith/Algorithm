// --- Directions
// Given a string, return a new string with the reversed
// order of characters
// --- Examples
//   reverse('apple') === 'leppa'
//   reverse('hello') === 'olleh'
//   reverse('Greetings!') === '!sgniteerG'

function reverse(str) {

  // debugger;

  //// solution 1:
  // return str
  //   .split('')
  //   .reverse()
  //   .join('');

  // // solution 2:
  // let reverse = '';
  // for (let char of str) {
  //   reverse = char + reverse;
  // }
  // return reverse;

  // solution 3:
  return str.split('').reduce((reverse, char) => {
    return char + reverse;
  }, '')
}

// console.log(reverse('apple'));
module.exports = reverse;