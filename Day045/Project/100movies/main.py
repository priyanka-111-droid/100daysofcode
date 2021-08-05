from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://stacker.com/stories/1587/100-best-movies-all-time")
web_page=response.text
soup=BeautifulSoup(web_page,"html.parser")

movies=soup.select(selector=".ct-slideshow__slide__text-container__caption div")
movies_list=[]
for m in movies:
    movies_list.append(m.getText())

#Our movies_list contains a heading,'100 best movies of all time' and then the 100 movies from 100 to 1.
# We pop and store first item in the list,the heading,'100 best movies of all time' in a separate variable
# called heading as we need to flip the movies_list to display from 1 to 100.

heading=movies_list.pop(0)
flipped_movies_list=movies_list[::-1]
# print(flipped_movies_list)

with open("Day045/Project/100movies/movies.txt",mode="w",encoding="utf-8") as file:
    #writing the heading,'100 best movies of all time'
    file.write(f"{heading}\n\n")
    #displaying movies from 1 to 100
    for movie_names in flipped_movies_list:
        movie_names=movie_names.replace("#","")
        file.write(f"{movie_names}\n")



