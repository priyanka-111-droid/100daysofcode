#We will be following all the followers of any account with large number of followers.(eg.chefsteps) in this project.
####<<<<STEP 1:SET UP INSTAGRAM CREDENTIALS>>>>####
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
from dotenv import load_dotenv
import os

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

INSTA_EMAIL=os.getenv('INSTA_EMAIL') #Instagram Email
INSTA_PASSWORD=os.getenv('INSTA_PASSWORD') #Instagram password

CHROME_DRIVER_PATH="C:\Python_development\chromedriver.exe" 
INSTAGRAM_LOGIN="https://www.instagram.com"
SIMILAR_ACCOUNT='chefsteps'
####<<<<STEP 2:CREATE A CLASS>>>>####
class InstaFollower:
    def __init__(self,driver):
        self.driver=driver
    def login(self):
        ###<<<<STEP 3:LOGIN TO INSTAGRAM>>>>###
        self.driver.get(f"{INSTAGRAM_LOGIN}/accounts/login/")
        self.driver.maximize_window()
        time.sleep(2)
        email=self.driver.find_element_by_name('username')
        password=self.driver.find_element_by_name('password')
        time.sleep(1)
        email.send_keys(INSTA_EMAIL)
        password.send_keys(INSTA_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
    
    def find_followers(self):
        ###<<<STEP 4:FIND FOLLOWERS OF TARGET ACCOUNT>>>###
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element_by_css_selector(".isgrP ul div li")
        for i in range(10):
            #In this case we're executing some Javascript, that's what the execute_script() method does. 
            #The method can accept the script as well as a HTML element. 
            #The modal in this case, becomes the arguments[0] in the script.
            #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        ###<<<STEP 5:FOLLOW ALL FOLLOWERS OF TARGET ACCOUNT>>>###
        all_buttons = self.driver.find_elements_by_css_selector(".isgrP ul div li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()


driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
obj=InstaFollower(driver)
obj.login()
obj.find_followers()
obj.follow()


