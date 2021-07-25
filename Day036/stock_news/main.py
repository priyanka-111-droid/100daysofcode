import requests
import smtplib,os

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3:Send a mail to yourself with format given below:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

STOCK_API_KEY=os.environ.get('STOCK_API_KEY')
NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
STOCK_ENDPOINT="https://www.alphavantage.co/query"
NEWS_ENDPOINT="https://newsapi.org/v2/everything"
my_email=os.environ.get('MY_EMAIL')
password=os.environ.get('PASSWORD')


stock_parameters={
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":STOCK_API_KEY,
}
response=requests.get(url=STOCK_ENDPOINT,params=stock_parameters)
stock_data=response.json()
# print(stock_data)


all_dates=stock_data["Time Series (Daily)"]
data_list=[value for (key,value) in all_dates.items()]
yesterday_data=data_list[0]
yesterday_closing_price=yesterday_data["4. close"]
day_before_yesterday_data=data_list[1]
day_before_yesterday_closing_price=day_before_yesterday_data["4. close"]

diff=((float(yesterday_closing_price))-(float(day_before_yesterday_closing_price)))
up_down=None
if diff>0:
    up_down="🔺"
else:
    up_down="🔻"

diff_perc=round(diff/float(yesterday_closing_price)*100)


def mail(formatted_text):
    for text in formatted_text:
        connection=smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()#encrypts message so other ppl can't read
        connection.login(user=my_email,password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:{STOCK_NAME}:{up_down}{diff_perc}%\n\n{text}".encode("utf-8")
        )
        

def get_news():
    news_parameters={
        "q":f"+{COMPANY_NAME}",
        "language":"en",
        "apiKey":NEWS_API_KEY,
    }
    news_response=requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_data=news_response.json()
    three_articles=(news_data['articles'][:3])
    title_and_desc=[f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_articles]
    mail(title_and_desc)


#to test if the code works,comment the if statement.
if abs(diff_perc)>5:
    get_news()






