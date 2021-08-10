#####<<<<STEP 1:SET TWITTER ACCOUNT>>>>####
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time 
from dotenv import load_dotenv
import os

# Additionally, you'll need to get your Internet Service Provider (ISP)'s guaranteed internet speeds. This should be in your contract somewhere. Alternatively, you could just use an example speed, e.g. 150Mbps download, 10Mbps upload.

PROMISED_UP=10       #ISP promised upload speed
PROMISED_DOWN=150    # ISP promised download speed
CHROME_DRIVER_PATH="C:\Python_development\chromedriver.exe" 
MY_EMAIL=os.getenv('MY_EMAIL') #Twitter Email
PASSWORD=os.getenv('PASSWORD') #Twitter password


#####<<<<STEP 2:CREATING A CLASS AND GETTING INTERNET SPEEDS AND TWEETING AT PROVIDER>>>>#####

# Create a class called InternetSpeedTwitterBot
class InternetSpeedTwitterBot:
# In the init() method, create the Selenium driver and 2 other properties down and up .
    def __init__(self,driver):
        self.up=0
        self.down=0
        self.driver=driver

# Create two methods - get_internet_speed() and tweet_at_provider() .
    def get_internet_speed(self):
        # pass
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()

        time.sleep(3)
        go_button=self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(60)
        self.up=self.driver.find_element_by_css_selector('.result-data-large.number.result-data-value.download-speed').text
        self.down=self.driver.find_element_by_css_selector('.result-data-large.number.result-data-value.upload-speed').text
     

    def tweet_at_provider(self):

        if(float(self.down)<PROMISED_DOWN or float(self.up)<PROMISED_UP):
            self.driver.get("https://twitter.com/login")

            time.sleep(2)
            # email = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
            email=self.driver.find_element_by_name('session[username_or_email]')
            # password = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')
            password=self.driver.find_element_by_name('session[password]')

            email.send_keys(MY_EMAIL)
            password.send_keys(PASSWORD)
            time.sleep(2)
            password.send_keys(Keys.ENTER)

            time.sleep(5)
            tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(3)

            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
            tweet_button.click()

            time.sleep(2)
        else:
            print("Speed is alright!")

        self.driver.quit()

# Outside of the class, initialise the object and call the two methods in order. Where you first get the internet speed and then tweet at the provider.
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
obj=InternetSpeedTwitterBot(driver)

# print(obj.up)
# print(obj.down)
try:
    obj.get_internet_speed()
except NoSuchElementException:
    print("Could not get current download and upload speed.Please try again later")
else:
    #If no errors i.e we have managed to get current upload and download speed successfully,go to twitter.
    obj.tweet_at_provider()

