// const mergeSort = (nums1, nums2) => {
//   // let result = [];
//   while (nums2.length) {
//     nums1[0] < nums2[0] ? null : nums1.push(nums2.shift());
//   }
//   return nums1
// }

// console.log(mergeSort([1,2,3,0,0,0], [2,5,6]));

const mergeSort = (nums1, nums2) => {
  let i = 0;
  while (nums2.length) {
    let next = nums2.shift();
    console.log(next);
    nums1[nums1.length - 1 - i] = next;
    console.log(nums1, nums2);
    i++;
  }
  nums1.sort();
};

console.log(mergeSort([1, 2, 3, 0, 0, 0], [2, 5, 6]));
