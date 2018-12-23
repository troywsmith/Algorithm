
// // problem 1
// // starter structure for OUR each
// var each = function(arr, callback){
//     // YOUR CODE IN HERE!
//     for (let i=0; i < arr.length; i++) {
//         callback(arr[i]);
//     }
//     }

//     // set up variables for arguments
//     var lottoNumbers = [18, 14, 15];             // our arr
//     var logMessage = function(element, index){   // our cb
//         console.log("The next number is..... " + element + "!");
//     }

//     each(lottoNumbers, logMessage);
//     // logs to the console:
//     //   "The next number is..... 18!"
//     //   "The next number is..... 14!"
//     //   "The next number is..... 15!"
//     // returns [18, 14, 15]



// // problem 2
// // starter structure for our partition
// var partition = function (arr, callback) {
//     // YOUR CODE IN HERE!



// }

// // set up variables for arguments
// var nums = [0, 1, 2, 3, 4, 5];  // our arr
// var isOdd = function (num) {      // our truth test
//     return num % 2 !== 0;
// };

// partition(nums, isOdd);
// // returns [[1, 3, 5], [0, 2, 4]]


// // problem 3
// // starter structure for our pluck
// let pluck = function (arr, key) {
//     // YOUR CODE IN HERE!
//     let firstNames = [];
//     for (let index=0; index<arr.length; index++) {
//         firstNames.push(arr[index][key]);
//     }
//     return firstNames;
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









// // Example of getPairs!

// // set up names argument
// var students = ["Johnny", "Emily A", "Ling", "Jason", "Franchesca"];
// // call getPairs function
// getPair(students);
// returns [["Emily A", "Ling"], ["Franchesca", "Jason"] , ["Johnny"]]

// var swap = function (arr, indexOne, indexTwo) {
//     // swap values 

//     return arr;
//   };

//   swap(["moe", "larry", "curly"], 0, 2);
//   // => ["curly", "larry", "moe"]


//   var getRand = function (low, high) {
//     // your work

//     return randNum;
//   };

//   getRand(5, 6)
//   // => 5 or 6
//   getRand(5, 10)
//   // => 6 or some other num between 5 and 10


//   var randArr = function (size) {
//     // your work;

//     return arr; 
//   }

//   randArr(3)
//   //=> [23, 11, 82];
//   randArr(2)
//   //=> [88, 42];


//   var getMax = function (arr) {
//     // your work

//     return max;
//   }

//   getMax([1,2,88, 34, 22])