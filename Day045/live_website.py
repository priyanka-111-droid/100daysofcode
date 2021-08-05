from bs4 import BeautifulSoup
import requests #to get hold of data from particular url

response=requests.get(url="https://news.ycombinator.com")
# print(response.text) prints entire html code

yc_web_page=response.text
soup=BeautifulSoup(yc_web_page,"html.parser")
# print(soup.title)

#use inspect in chrome developer tools to find out the classes and ids
#TODO 1:Store title of first article under article_text using BeautifulSoup and print it.
first_article=soup.select_one(selector=".athing .title .storylink")
article_text=first_article.getText()
# print(article_text)
#TODO 2:print link to same article
article_link=first_article.get("href")
# print(article_link)


#TODO 3:print number of upvotes to that article
article_upvotes=soup.select_one(selector=".subtext .score").getText()
# print(article_upvotes)



#TODO 4:get all article titles,links,upvotes
all_articles=soup.select(selector=".athing .title .storylink")
#we can't use getText() directly on list(all_articles) so we can use for loops or list comprehensions to access each individual article and then use getText()
all_article_texts=[]
all_article_links=[]
for article in all_articles:
    #get all text and append it to list
    all_article_texts.append(article.getText())
    #get all links and append it to another list
    all_article_links.append(article.get("href"))

all_article_upvotes=[x.getText() for x in soup.select(selector=".subtext .score")]

# print(all_article_texts)
# print(all_article_links)
# print(all_article_upvotes)


#TODO 5:In all_article_upvotes list,we want to convert it to a number format so remove the word 'points' that comes after it
all_article_upvotes=[int(each_upvote.split(" ")[0]) for each_upvote in all_article_upvotes]
# print(all_article_upvotes)

#TODO 6:Print title and link for Hackernews story with highest number of upvotes
index_of_max=all_article_upvotes.index(max(all_article_upvotes))
print(all_article_texts[index_of_max])
print(all_article_links[index_of_max])


