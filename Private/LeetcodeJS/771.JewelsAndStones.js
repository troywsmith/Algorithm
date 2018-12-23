// numJewelsInStones = (J, S) => {
//   let hash = {};
//   let count = 0;
//   for (let each of S) {
//     hash[each] = (hash[each]) ? hash[each]+= 1 : 1;
//   }
//   for (let letter of J) {
//     hash[letter] ? count += hash[letter] : null;
//   }
//   return count;
// };

numJewelsInStones = (J, S) => {
  // replaces any stones that are not jewels with '' then returns length
  return S.replace(new RegExp(`[^${J}]`, 'g'), '').length;
}

console.log(numJewelsInStones("aA", "aAAbbbb"));
console.log(numJewelsInStones("z", "ZZ"));