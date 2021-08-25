# Blog Capstone part 2-adding styling

Part 1 was done in [Day 57 Project.](https://github.com/priyanka-111-droid/100daysofcode/tree/main/Day057/Project/blog-templating/blog-templating-start)

## 1.Download the starting bootstrap template

* https://startbootstrap.com/previews/clean-blog/

* Unzip the downloaded file and rename the folder to "upgraded-blog"

* Create **static** and **templates** folders and move HTML files to templates folder and remaining files to static folder.

* In templates folder,also create a header.html and footer.html file 

* Finally create a main.py outside static and templates folders.

## 2.Get the home page to work

* Use what you have learnt about Flask, get the home page to render when you go to http://localhost:5000 in your browser.Don't worry about the styling just yet.

* HINT: https://stackoverflow.com/questions/46127005/why-does-localhost5000-not-work-in-flask

## 3.Fix the header and footer

Now the styling is missing because the static files (CSS/JS/images etc.) are served up by our server and they are no longer at the locations specified in the header.

* Fix the header in **index.html** so that the styling and bootstrap all appear. 

* It's usually a good idea to build a dynamic url for the static resources instead of just pointing to the static folder. See the documentation here:https://flask.palletsprojects.com/en/2.0.x/quickstart/#static-files and check this [video tutorial](https://www.youtube.com/watch?v=O5m6lNy3w-g).

* Fix the footer resources so that the Javascript works. You can verify this by checking that when you scroll the navigation bar becomes sticky at the top and changes background color.

## 4.Using Jinja to Render templates

The reason why Jinja Templates are called templates is because it makes it easier to create HTML pages by templating. Instead of re-writing the same header/navigation bar/footer you can just create a header and footer template which can then be applied to all web pages in your website.

e.g.

{% include "header.html" %}

Changeable part of your webpage. e.g. the body of the page.

{% include "footer.html" %}

Then when the website is rendered, the header.html and footer.html gets inserted where the {% include %} specifies.

Using https://jinja.palletsprojects.com/en/3.0.x/templates/#include

* Remove the <head> & navigation code from index.html and place it in the header.html file.

* Remove the <footer> from index.html and place it in the footer.html file.

* Using the above documentation, use include to make the website still function exactly the same as before.

## 5.Make the About and Contact Pages work

Now that you've seen how you can replace the repeatable parts of your website (header/footer), we're going to make the rest of the pages work.

* Delete the navigation bar item that points to the "Sample Post".

* Update main.py and the about.html and contact.html files so that when you click on the About link in the navigation bar it goes to the About page and likewise with the Contact page. 

* See if you can make the static images work on the About and Contact pages.

## 6.Fetch and render blogs from API

Just like our last blog website, we're going to save you the hassle of writing all your blog posts.We are going to get the posts from our API on npoint.

https://api.npoint.io/bd293e18554ba56ad1aa


* In main.py get hold of the json data at the above API endpoint.

* Use the data from the API to render the home page, replacing the title, subtitle, author and dates of each blog post with the data from the API.

HINT 1: Instead of using a custom class, you can simply use Jinja variables to use the dot notation instead of square brackets. See: https://jinja.palletsprojects.com/en/3.0.x/templates/#variables

HINT 2: You'll need to use a for loop in the Jinja template, which we've done before. See the documentation here: https://jinja.palletsprojects.com/en/3.0.x/templates/#for

* (Optional)We can change the background image using [unsplash](https://unsplash.com/)

## 7.Rendering individual posts

* Render each individual post in the post.html page. When a user clicks on a particular post title on the home page (index.html), we should take them to the post.html page where the title/subtitle/image/date/author/body of the post is shown.

* Backgrounds for all invidual posts are from unsplash.












