# Binary Search

![Morty Searching](https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif)

### What is it?

Binary search is an algorithm that we can use to find the value of an element within an array. However, it is only effective if the elements in the array are sorted. If the value you are searching for is in the array, binary search returns the **position** (or index) of the element. Otherwise, binary search returns `null`.  

+ The binary search algorithm begins by comparing the target value to the value of the middle element of the sorted array.

+ If the target value is equal to the middle element's value, then the position is returned and the search is finished.

+ If the target value is less than the middle element's value, then the search continues on the lower half of the array (excluding middle element)

+ If the target value is greater than the middle element's value, then the search continues on the upper half of the array.

+ Continue until the target value is found (and its element position is returned), or until the entire array has been searched (and `null` is returned)

+ _Note:_ You are eliminating half the elements every time with binary search.

### Exercise

1. Write a binary search algorithm that will take an array and a single number as parameters and return a boolean true if that number exists in that array and a boolean false if that number does not exist. _Note: Each problem has two parts_

   ```js
   array = [6, 7, 8, 9, 10, 14, 15, 17, 19, 22, 23, 25, 30]
   binary_search(array, 22) => true
   binary_search(array, 13) => false
   ```

2. Write a binary search algorithm that takes an array of names and a single name as parameters and returns the name of the student if found else returns null if not found.  _Note: Each problem has two parts_

   ```js
   students = ["Jesica", "Yaakov", "Darrell", "Dan", "Ryan", "Raul", "Rachel", "Ehsanul", "Eryl", "Sean", "Andrey", "Akram", "Supreet", "Jae", "Joel", "Simon", "John", "Alvin", "Troy", "Elyas"];
   binarySearch(students, "Your Name")
   binarySearch(students, "Paris")
   ```
