## Challenge 1

1. Create an array: `var cacti = ['barrel', 'columnar', 'hedgehog', 'cluster', 'prickly pear'];`
2. Print out the 3rd element (hedgehog) to the console.
  ```js
  cacti[2]
  ```
3. Print out the length of the array to the console.
  ```js
  cacti.length
  ```
4. Print out the last element (prickly pear) - can you find two different ways to do this?
  ```js
  cacti[cacti.length-1]
  ```
5. Put epiphytic on the end of the array.
  ```js
  cacti.push("epiphytic")
  ```
6. Use indexOf to find the index of 'columnar' and print it out.
  ```js
  cacti.indexOf("columnar")
  ```
7. Remove 'barrel' (the first element) from the list.
  ```js
  cacti.shift("barrel")
  ```
8. Add 'barrel' back to the front of the list
  ```js
  cacti.unshift("barrel")
  ```
9. Remove the 4th element of the list (hint: use splice).
  ```js
  cacti.splice(3, 1)
  ```

## Challenge 2

1. Use for to print out each fruit from the list.
   ```js
   let fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Guava", "Huckleberry", "Ice plant", "Jackfruit"];

   fruits.forEach(function(element) {
     console.log(element);
   });
   ```

2. Print the same list items as above, in reverse order.
   ```js
   fruits.reverse();

   for (let i = 0; i < fruits.length; i++) {
       let item = fruits[i];
       console.log(item);
   }
   ```

## Challenge 3

1. Use `forEach` to print each character in the list of famous cartoon dogs.
   ```js
   let dogs = ['Snoopy', 'Scooby', 'Pluto', 'Goofy', 'Astro', 'Mr. Peabody', 'Odie', "Santa's Little Helper", 'Brian'];

   dogs.forEach(function(element) {
     console.log(element);
   });
   ```

## Challenge 4

1. Use `forEach` and `string.toUpperCase` method to convert the list of characters into all capitals. That is, you should replace each character in the array with an all UPPERCASE version of that character's name.
   ```js
   dogs.map(function(dog){ return dog.toUpperCase() })
   ```

   _Use console.log(dogs) to verify your solution has changed the dogs array._
