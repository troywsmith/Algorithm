
## DOM Manipulation

Go to [generalassemb.ly](https://generalassemb.ly) and try the following exercises.

-----

*  Grab the `body` from the page using `document.querySelector`. and change the `opacity` to `.5`.

-----
* Grab all the `img` tags from the page. Iterate through each image and change the source to 

    ```
http://www.maine-coon-cat-nation.com/image-files/girl-kitten-names.jpg
    ```

* Create a `kittenPaint` function for your code above. Save it as a snippet in your developer console. Go to Google and run it there.

----

* Using 
    
    ```
document.querySelectorAll("*")
    ```
to grab **all elements** on the page, iterate through each `element` in the list using a `for` loop. Use 

    ```
element.style.backgroundImage = "url(http://www.maine-coon-cat-nation.com/image-files/girl-kitten-names.jpg)"
    ``` 

    to change every element to have a kitten background image.
* Turn the above exercise into a `kittenBomb` function and save it in `sources` under your snippets. Then run it on your favorite site.


-----

* Select the `body` from the page. When it is clicked change its style using the following, 
    
    ```
body.style.transform = "rotateZ(60deg)";
    ```

* Create a `click` event on the `body`.  When the body is `clicked` grab all the images on the page and use the `style.transform` above to rotate each image. In other words, when the page is clicked rotate all images on the pages.

