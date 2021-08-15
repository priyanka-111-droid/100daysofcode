import requests
BLOG_URL="https://api.npoint.io/09b8316e15e0e21878a0"

class Post:
    def __init__(self):
        self.response=requests.get(url=BLOG_URL)
        self.all_posts=self.response.json()


    def return_blog(self):
        modified_blog=self.all_posts
        return modified_blog 




            

