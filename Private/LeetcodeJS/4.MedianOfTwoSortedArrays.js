function findMedianSortedArrays(nums1, nums2) {
  function merge(left, right) {
    let result = [];
    let i = 0;
    let j = 0;
    while(i < left.length && j < right.length) {
      let pushed = (left[i] < right[j]) ? left[i++] : right[j++];
      result.push(pushed);
    }
    return result.concat(left.slice(i)).concat(right.slice(j))
  }
  let merged = merge(nums1, nums2);
  let mid = Math.floor(merged.length/2);
  return (merged.length % 2 === 0) ? (merged[mid] + merged[mid - 1]) / 2 : merged[mid];
};

console.log(findMedianSortedArrays([1, 2], [3, 4]));