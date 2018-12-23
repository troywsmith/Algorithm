1. Read and console log the following:

  * the array that contains all the student club data
  
  ```js
  clubs
  ```
  * the number of clubs
    ```js
   clubs.length
   ```

  * the object that contains all of the information for the second club
  ```js
   clubs[1]
   ```

  * the teacher of the first club
   ```js
   clubs[0].teacher
   ```
  * the array of students in the second team
  ```js
  clubs[1].students
   ```

  * the last name of the second student on the third team
  ```js
  clubsclubs[2].students[1].last
  ```

2. Create an object literal representing a student with your name, and assign it to a variable.

   ```js
   var my_name = {first: 'Benjamin', last: 'Stiller'}
   ```

3. Create an object literal representing a new club, and assign it to a variable. Make sure it has values for name, students, and teacher.

   ```js
   let new_club = {
   name: 'Volleyball Team',
   students: [
     {first: 'Anna', last: 'Bancroft'},
     {first: 'Jane', last: 'Eyre'}
   ],
   teacher: 'James Madison'
   }
   ```

4. Add your new club to the array of clubs.

   ```js
   clubs.push(new_club)
   ```

5. Add yourself as a student in the new club.

   ```js
   clubs[3].students.push(my_name)
   ```

6. Update Samuel Black's first name to Sam everywhere it occurs.
   ```js
   clubs[2].students[1].first = "Sam"
   ```

7. Oops, the school is losing extracurricular funding. Remove one of the clubs from the array. Add a comment to say which club has been defunded.

   ```js
   clubs.pop()
   ```
