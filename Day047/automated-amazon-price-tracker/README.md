# Automated Amazon price tracker

## 1.Use Beautiful Soup to get price of item from Amazon

*  Find a product on Amazon that you want to track and get the product URL.

*  Use the requests library to request the HTML page of the Amazon product using the URL.

* You'll need to pass along some headers in order for the request to return the actual website HTML. You can see your browser headers by going to this website:http://myhttpheader.com/
At minimum you'll need to give your "User-Agent" and "Accept-Language" values in the request header.

*  Use BeautifulSoup to make soup with the web page HTML you get back. You'll need to use the "lxml" parser instead of the "html.parser" for this to work.

* Use BeautifulSoup to get hold of the price of the item as a floating point number and print it out.

## 2.Send an email to yourself when price falls below a target value,say $100 in this case

* So when the price is below 100 then use the smtp module to send an email to yourself. In the email, include the title of the product, the current price and a link to buy the product.


