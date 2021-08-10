# Internet Speed Twitter Complain bot

## Steps:

## 1.Create a Twitter account 

Store your Twitter account email and password and you'll also need to get your Internet Service Provider (ISP)'s guaranteed internet speeds. This should be in your contract somewhere. Alternatively, you could just use an example speed, e.g. 150Mbps download, 10Mbps upload.

## 2. Create a class

* Create a class called InternetSpeedTwitterBot

* In the init() method, create the Selenium driver and 2 other properties down and up .

* Create two methods - get_internet_speed() and tweet_at_provider() .

* Outside of the class, initialise the object and call the two methods in order. Where you first get the internet speed and then tweet at the provider.

## 3.Get Internet speeds

Use https://www.speedtest.net/ to get your live upload and download speeds.Use Selenium and Python to get the same result printed out in your console.Depending on your internet speeds, you might need to add a 60-180s delay to wait for the results.

## 4.Building a twitter bot

* Go through the process of logging-in and tweeting on Twitter as a human to study which selectors/id/classes/XPATHs you could target.

* Use Python and Selenium to complete the same process, login to Twitter, compose the tweet to include your up/down speeds and your promised speeds then send the tweet.

* If speed matches (ISP)'s guaranteed speeds,you don't need to tweet.

