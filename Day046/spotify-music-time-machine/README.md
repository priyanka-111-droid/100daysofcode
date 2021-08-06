# Spotify Musical time machine

# Steps:

## 1.Scraping the Billboard Hot 100

Input a historical date from user,convert it to YYYY-MM-DD format.Using what you've learnt about BeautifulSoup, scrape the top 100 song titles from Billboard Hot 100 on that date into a Python List.

Hints:

1.[strptime and strftime](https://www.programiz.com/python-programming/datetime)

2.[Beautiful Soup is returning empty list](https://stackoverflow.com/questions/65545425/why-beautiful-soup-select-by-class-return-empty-list-by-find-all-works/65546278)

3.Take a look at the URL of the chart on a historical date: https://www.billboard.com/charts/hot-100/2000-08-12

## 2.Authentication of Spotify

1.In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App:
https://developer.spotify.com/dashboard/

3.Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project.Use http://example.com as your Redirect URI.

4.We're going to use one of the most popular Python Spotify modules - [Spotipy](https://spotipy.readthedocs.io/en/2.16.1/?highlight=create%20new%20playlist#) to authenticate.

Hints:

* This is the method you'll need: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.oauth2.SpotifyOAuth and see this [article](https://jman4190.medium.com/build-your-own-spotify-wrapped-with-python-spotify-and-glide-apps-493dc7da20b) for reference and this [post](https://stackoverflow.com/questions/63712286/why-cant-i-grant-authorization-to-my-spotify-app).

* You need the "playlist-modify-private" scope in order to create a private playlist on Spotify.

* Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar.

* Get the user id of the authenticated user (your Spotify username).You'll need this method: https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user.The output of the above method is a dictionary, look for the value of the "id" key.

## 3.Search Spotify for songs from step 1.

Using the [Spotipy documentation](https://spotipy.readthedocs.io/en/2.18.0/), create a list of Spotify [song URIs](https://spotipy.readthedocs.io/en/2.13.0/#ids-uris-and-urls) for the list of song names you found from step 1 (scraping billboard 100).

Hints:

* You can use the query format "track: {name} year: {YYYY}" to narrow down on a track name from a particular year.

* Sometimes a song is not available in Spotify, you'll want to use exception handling to skip over those songs.

* Try [slicing](https://stackoverflow.com/questions/10897339/python-fetch-first-10-results-from-a-list) the list of 100 songs from step 1 into just 2 or 3 songs and use [json viewer](http://jsonviewer.stack.hu/) to visualise data better.

* pprint() might also help you visualise the result better. https://docs.python.org/3/library/pprint.html


## 4.Creating new playlist on Spotify and adding songs to it

1.Using the Spotipy documentation, create a new private playlist with the name "YYYY-MM-DD Billboard 100", where the date is the date you inputted in step 1.

HINT: You'll need the user id you got from Step 2.

2.Add each of the songs found in Step 3 to the new playlist.

HINT: You'll need the playlist id which is returned as an output once you've successfully created a new playlist.

## 5.Viewing your playlist

In order to view your playlist,login to Spotify,Scroll to the bottom and under USEFUL LINKS,click 'Web Player'.

