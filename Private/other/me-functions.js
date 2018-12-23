// CHALLENGE SET A

// Challenge 1

/*
Save this file to your WDI/ folder, run in your terminal using node me-functions.js >> Each of the following tasks can be accomplished using a single Array method in 1 line of code.

Create an array: var cacti = ['barrel', 'columnar', 'hedgehog', 'cluster', 'prickly pear'];
Print out the 3rd element (hedgehog) to the console.
Print out the length of the array to the console.
Print out the last element (prickly pear) - can you find two different ways to do this?
Put epiphytic on the end of the array.
Use indexOf to find the index of 'columnar' and print it out.
Remove 'barrel' (the first element) from the list.
Add 'barrel' back to the front of the list
Remove the 4th element of the list (hint: use splice).
*/
var cacti = ['barrel', 'columnar', 'hedgehog', 'cluster', 'prickly pear'];
console.log(cacti[2]);
console.log(cacti.length);
console.log(cacti[cacti.length-1] );
cacti.push('epiphytic');
console.log(cacti);
console.log(cacti.indexOf('columnar'));
cacti.shift('barrel');
console.log(cacti);
cacti.unshift('barrel');
console.log(cacti);
cacti.splice(4);
console.log(cacti);

// Challenge 2

/*
Use for to print out each fruit from the list.

var fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry",
"Fig", "Guava", "Huckleberry", "Ice plant", "Jackfruit"];
*/
var fruits = ["Apple", "Banana", "Cherry", "Durian", "Elderberry",
"Fig", "Guava", "Huckleberry", "Ice plant", "Jackfruit"];

fruits.forEach(function(element) {
    console.log(element);
});


// Challenge 3

/*
Print the same list items as above, in reverse order.
*/

// CHALLENGE SET B

// Challenge 1A

/*
var dogs = ['Snoopy', 'Scooby', 'Pluto', 'Goofy', 'Astro', 'Mr. Peabody', 'Odie', "Santa's Little Helper", 'Brian'];
Use forEach to print each character in the list of famous cartoon dogs.
*/

// CHALLENGE 1B

/*
Use forEach and String.toUpperCase method to convert the list of characters into all capitals. That is, you should replace each character in the array with an all UPPERCASE version of that character's name.

Use console.log( dogs ) to verify your solution has changed the dogs array.
*/



