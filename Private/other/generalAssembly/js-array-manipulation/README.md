# Array Manipulation

## Challenge Set A ##

### Challenge 1 ###

Use your chrome console (`ctrl+opt+j`) to perform the following activities.
Each of the following tasks can be accomplished using a single Array method in 1 line of code.

1. Create an array: `var cacti = ['barrel', 'columnar', 'hedgehog', 'cluster', 'prickly pear'];`
1. Print out the 3rd element (hedgehog) to the console.
1. Print out the length of the array to the console.
1. Print out the last element (prickly pear) - can you find two different ways to do this?
1. Put `epiphytic` on the end of the array.
1. Use `indexOf` to find the index of 'columnar' and print it out.
1. Remove 'barrel' (the first element) from the list.
1. Add 'barrel' back to the **front** of the list
1. Remove the 4th element of the list (hint: use `splice`).

### Challenge 2 ###

1. Use `for` to print out each fruit from the list.

    ```js
    var fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry",
    "Fig", "Guava", "Huckleberry", "Ice plant", "Jackfruit"];
    ```
### Challenge 3 ###

1. Print the same list items as above, in reverse order. 

### Challenge 4 ###

1. Use a `for` loop to print out every *third* fruit. The output should be `"Cherry"`, `"Fig"`, `"Ice plant"`.


## Challenge Set B: `forEach` ##

### Challenge 1a ###

```js
var dogs = ['Snoopy', 'Scooby', 'Pluto', 'Goofy', 'Astro', 'Mr. Peabody', 'Odie', "Santa's Little Helper", 'Brian'];
```

Use `forEach` to print each character in the list of famous cartoon dogs.


###Challenge 1b ###

Use `forEach` and `String.toUpperCase` method to convert the list of characters into all capitals.  That is, you should replace each character in the array with an all UPPERCASE version of that character's name.

Use `console.log( dogs )` to verify your solution has changed the `dogs` array.


###Challenge 2 ###

1. *Dig Inn* has a line wrapped around the block! It takes about two minutes per delicious Charred Chicken Marketbowl. Output the customer's name & their expected wait time.
    
    ```javascript
    // warning -- below is pseudo-code!
    var customers:   Ada, Paris, Mike, Cameron, Lizzie, Eric, Ryan, Celeste, Drake, Jason
    customers.forEach(fn);
    
    
    /* sample output:
       Ada: 2 minutes
       Paris: 4 minutes
       Mike: 6 minutes
       Cameron: 8 minutes
       Lizzie: 10 minutes
       ...
       Jason: 20 minutes
    */
    ```

1. If you originally solved this challenge with a `for` loop, rewrite it using `forEach`. You may want to check out <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach">documentation about `forEach`</a>'s callback method arguments.  If you originally solved this challenge with `forEach`, rewrite your solution with a `for` loop. 


