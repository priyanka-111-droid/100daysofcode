# Remember:

1.If we are using the data privately, for example to create a service for ourselves then it does not matter.

2.But if you are using someone else's data for business,only data publicly available can be scraped.**You CANNOT commercialise copyrighted content.**

Eg.you can't scrape someone else's  youtube video data and use it on your website.

3.**You CANNOT scrape data behind authentication.**
Eg.if you need to login to facebook to use the data,its illegal.

4.A lot of websites use captchas or recaptchas to prevent bots like our python code from accessing the data.

5.**If a website has a public API,then always go for the API.**

6.You can find out what can be scraped and what cannot be scraped from a website by **adding '/robots.txt'** after root of website url. It tells you what endpoints you cannot use.

Eg. https://news.ycombinator.com/robots.txt

7.Don't scrape more than once a minute as it puts a lot of demand on website server.




