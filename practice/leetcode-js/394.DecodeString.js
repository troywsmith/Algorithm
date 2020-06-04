// decodeString = (s) => {
//   let stringStack = (s.match(/([a-z])+/g));
//   let kStack = (s.match(/[0-9]/gi))
//   let result = '';
//   console.log(stringStack);
//   console.log(kStack);
//   while (stringStack.length) {
//     // let lastK = kStack.pop();
//     // let lastString = stringStack.pop();
//     // result += lastString.repeat(parseInt(lastK));
//     // // repeat ^ next k times with next string in front
//     // result = (result).repeat(parseInt(lastK));
//     // console.log(stringStack);
//     // result += stringStack[i].repeat(parseInt(kStack[i]));
//     result = stringStack.pop() + result;
//   }
//   return result;
// };

var decodeString = function(s) {
  let re = /(\d+)\[([a-z]*)\]/
  let temp;
  while((temp = re.exec(s))) {
    s = s.replace(re, temp[2].repeat(parseInt(temp[1], 10)));
  }
  return s;
};

console.log(decodeString("3[a]2[bc]"));
console.log(decodeString("3[a2[c]]"));
console.log(decodeString("2[abc]3[cd]ef"));

