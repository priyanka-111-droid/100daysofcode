from bs4 import BeautifulSoup
import requests
from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv 
import os

load_dotenv()

CLIENT_ID=os.getenv("CLIENT_ID")
CLIENT_SECRET=os.getenv("CLIENT_SECRET")
SPOTIPY_REDIRECT_URI="http://example.com"
scope="playlist-modify-private"


####<<<<STEP 1:Billboard 100 songs of any date from the past>>>>>####
BILLBOARD="https://www.billboard.com/charts/hot-100"

date_string = input("Enter date you wish to travel back to?Enter date in DD-MM-YYYY format :")
datetime_object = datetime.strptime(date_string, "%d-%m-%Y")
# print("datetime_object =", datetime_object)
date=(datetime_object.strftime("%Y-%m-%d")) #we only need date in YYYY-MM-DD format for web scraping

response=requests.get(url=f"{BILLBOARD}/{date}")
billboard_page=response.text
soup=BeautifulSoup(billboard_page,"html.parser")
# print(soup)

#See stack overflow link if getting empty list here!
# print(soup.select(".chart-element__information__song text--truncate color--primary")) # returns an empty list
# print(soup.select(".chart-element__information__song.text--truncate.color--primary")) #this returns full list
# print(soup.find_all(name="span",class_="chart-element__information__song text--truncate color--primary")) # also returns the full list

song_info=soup.select(".chart-element__information__song.text--truncate.color--primary")
song_titles=[]
for song in song_info:
    song_titles.append(song.getText())

####<<<<STEP 2:SPOTIFY AUTHENTICATION>>>>####

oauth = SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope)

user_token=oauth.get_access_token(code=None, as_dict=False, check_cache=True)
#create spotify client object in order to get user id
sp = spotipy.Spotify(auth=user_token)

user_results = sp.current_user() #gives a dictionary containing entire user profile
user_id=(user_results.get('id')) #we need user id from this dictionary

####<<<<<<STEP3:SEARCH SPOTIFY FOR SONGS FROM STEP 1>>>>>####

# The problem in this case is not with appending the song URI to the list, 
# the problem is with the json that you receive from Spotipy not having anything for the song URI 
# if there is no song to be found. 
# Therefore, this would be an index error instead of a type error.

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# print(song_uris)

###<<<<STEP 4:CREATING AND ADDING TO SPOTIFY PLAYLIST>>>>####
new_playlist=sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100", 
    public=False,
    collaborative=False, 
    description='new playlist for a particular date'
)
playlist_id=new_playlist['id']
songs_to_new_playlist=sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)

# print(songs_to_new_playlist)


#In order to view your playlist,login to Spotify,Scroll to the bottom and under USEFUL LINKS,click 'Web Player'

