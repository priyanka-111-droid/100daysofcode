# Web scraping Capstone:Data entry job automation

We will be tackling a research data entry job.

We will go to Zillow to get address,price and links of real estate properties that match a certain criteria.We will transfer the data to google forms and use it to create a spreadsheet in google sheets.

Steps:

## 1.Create a google form

Go to https://docs.google.com/forms/ and create your own form.Add 3 questions to the form(What is the address of property,price per month and link to the property), make all questions "short-answer".
Click send and copy the link address of the form. You will need to use this in your program.

## 2. Web scraping from Zillow using Beautiful soup

Go to [this web address on Zillow](https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D) and see how the website is structured, this is where you'll be scraping the data from.

Create a list of addresses for all the listings you scraped.

Create a list of prices for all the listings you scraped. 

Create a list of links for all the listings you scraped.

HINT 1: In order to access Zillow using requests, you'll need to provide your user agent and accepted languages via a header. We've discussed this in the Amazon Price Scraping project in day 47.

HINT 2: Some of the links you get back from Zillow may be incomplete.All you need to do is just add https://www.zillow.com in front e.g.

https://www.zillow.com/b/argenta-san-francisco-ca-5Xj7m7/


## 3.Using Selenium to fill the google form

Use Selenium to fill in the form you created. Each listing should have its price/address/link added to the form. You will need to fill in a new form for each new listing.

Hint:https://www.geeksforgeeks.org/automatically-filling-multiple-responses-into-a-google-form-with-selenium-and-python/

Once all the data has been filled in, click on the "Sheet" icon to create a Google Sheet from the responses to the Google Form. You should end up with a spreadsheet with all the details from the properties. Eg.

![Screenshot (700)](https://user-images.githubusercontent.com/77121296/129002583-e289c519-6eb9-4f10-a6fc-fd859d65b375.png)



