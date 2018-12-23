// 1. What is the outcome of the following expressions?
/*
true || false
// true
false && false
//true
true && false
//false
(false || true) && true
//true
false && ((true || false) && (false || true))
//false
*/

// 2. What is the outcome of each of the following expressions?
/*
true && 6
//6
0 || "hi"
//hi
["a","b","c"] || "123"
//["a","b","c"]
{"key":"value"} || false
//{"key":"value"}
*/

// 4. When a user tries to login to our website we want to check that they actually input a value for username and a value for password. If they typed both in, give them an "All Good". But if either the username or the password are missing, give them an error: "Missing Username" / "Missing Password".
/*
username // string
//
password // string
*/

// 5. We need a quick way to determine if that blip on the radar is superman or not. Sometimes it's just a bird. Sometimes it's just a plane. But we definitely want to know if its superman. Write some code which will alert: "It's superman!" when the following are true (it's up to you to decide what makes the most sense):

/*
isBirdlike // boolean
//
isPlanelike // boolean
//
hasFeathers // boolean
//
isMadeOfMetal // boolean
// 
*/

// 6. Jimmy loves roller coasters, but there are a bunch of rules (ugh!) for riding. For starters, it costs 5 tokens. Here's how we might code that:

// var tokens = 2; // Jimmy's tokens
// var height = 2;
// var age = 10;
// var parent = "no";
// var parkPass = "no";
// var bossLook = "no";

// // Can he ride?
// if ((tokens >= 5 || parkPass === "yes") && height >= 4 && (age >= 12 || parent === "yes") || bossLook === "no") {
//     console.log("Step right up!");
// } else {
//     console.log("Sorry, you can't ride")
// }

/*
Edit the code above to check the following additional Requirements:

Must be at least 4ft tall.
Must be at least 12 years old.
Replace the previous rule: now riders under 12 must be accompanied by an adult.
If the boss isn't looking, you can sneak in!
Riders with a park pass get in free.
*/

// 7. Create a loop which prints out:

// var x;
// for (x = 0; x <= 5; x++) {
//     console.log(x);
// }

/*
0
1
2
3
4
5
*/

// 8. Create the "Bottles of beer on the wall" song (watch out for infinite loops!):

/*
    5 bottles of beer on the wall,
    5 bottles of beer!
    Take one down and pass it around,
    4 bottles of beer on the wall...

    4 bottles of beer on the wall,
    4 bottles of beer!
    Take one down and pass it around,
    3 bottles of beer on the wall...
    etc.
  */

// How would you change "0" to "No more"?
// How would you fix "1 bottles of beer"?

