// ARRAY MANIPULATION

/*
getPairs(names)

Write a function called getPairs that takes in an array of names and outputs random pairs of names. How could you use this to generate pairs of students for pair programming?
*/
const tesseract_students = ["Yaakov", "Darrell", "Dan", "Ryan", "Raul", "Rachel", "Ehsanul", "Eryl", "Sean", "Andrey", "Akram", "Supreet", "Jae", "Joel", "Simon", "John", "Alvin", "Troy", "Elyas"];

function getPairs(arr,n) {
    let pairsArray = [];

    function shuffleArray(sourceArray) {
        for (let i = 0; i < sourceArray.length - 1; i++) {
            let randIndex = i + Math.floor(Math.random() * (sourceArray.length - i));
            let temp = sourceArray[randIndex];
            sourceArray[randIndex] = sourceArray[i];
            sourceArray[i] = temp;
        }
        return sourceArray;
    }
    let shufStuds = shuffleArray(arr);
    while (shufStuds.length > 0) {
        let xxx = shufStuds.splice(0, n);
        pairsArray.push(xxx);
    }
    return pairsArray;
}

console.table(getPairs(tesseract_students,10));






// // ITERATION METHODS

// /*
// Write a function called each that takes in an array argument (called arr) and a function argument (called callback). This will be our version of JavaScript's forEach. The function argument (callback) should take two arguments: one element from the array, and the index of that element. The each function should loop through the array and call callback once for each element. After the loop, each should return arr, the original array that was passed in.
// */

// // starter structure for OUR each
// var each = function (arr, callback) {
//     // YOUR CODE IN HERE!



// }

// // set up variables for arguments
// var lottoNumbers = [18, 14, 15];             // our arr
// var logMessage = function (element, index) {   // our cb
//     console.log("The next number is..... " + element + "!");
// }

// each(lottoNumbers, logMessage);
// // logs to the console:
// //   "The next number is..... 18!"
// //   "The next number is..... 14!"
// //   "The next number is..... 15!"
// // returns [18, 14, 15]

// /*
// Write a function called partition that takes in an array and another function (a callback). The callback should take in an element and an index and return true or false. partition should split the array into two groups: one whose elements all resulted in true and one whose elements all resulted in false. It should return a new array with the two groups nested inside.
// */

// // starter structure for our partition
// var partition = function (arr, callback) {
//     // YOUR CODE IN HERE!



// }

// // set up variables for arguments
// var nums = [0, 1, 2, 3, 4, 5];  // our arr
// var isOdd = function (num) {    // our truth test
//     return num % 2 !== 0;
// };

// partition(nums, isOdd);
// // returns [[1, 3, 5], [0, 2, 4]]

// /*
// Write a function called pluck that takes in an array of objects and a string that is one of their keys. pluck should iterate through the array, pick out the value each object has associated with the given key, and return a new array containing those values. This iteration method won't use a callback.
// */

// // starter structure for our pluck
// var pluck = function (arr, key) {
//     // YOUR CODE IN HERE!



// }

// // set up variable for arguments
// var grandparents = [
//     { first: "June", last: "Crane", age: 74 },
//     { first: "Jim", last: "Crane", age: 76 },
//     { first: "Linda", last: "Fuentes", age: 62 },
//     { first: "Panfilo", last: "Fuentes", age: 76 }
// ];

// // call the pluck function, asking for the key 'first'
// pluck(grandparents, 'first');
// // returns ["June", "Jim", "Linda", "Panfilo"]