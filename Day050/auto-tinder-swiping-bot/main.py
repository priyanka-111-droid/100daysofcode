#We will login in to Tinder using our Facebook account

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from dotenv import load_dotenv
import os

MY_EMAIL=os.getenv('MY_EMAIL') #Facebook Email
PASSWORD=os.getenv('PASSWORD') #Facebook password

CHROME_DRIVER_PATH="C:\Python_development\chromedriver.exe" 
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get("https://tinder.com/")
driver.maximize_window()

#Login button
time.sleep(2)
login_button = driver.find_element_by_xpath('//*[@id="s722988905"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
login_button.click()

try:
    # Facebook login option
    time.sleep(2)
    fb_login = driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()
                                           
except NoSuchElementException:
    # more options
    time.sleep(2)
    more_options=driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    # Facebook login option
    time.sleep(1)
    fb_login = driver.find_element_by_xpath('//*[@id="s-1005392171"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    fb_login.click()
    

#switch window from base window(tinder) to facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title) 

# #typing email and password
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')

email.send_keys(MY_EMAIL)
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title) 

#disabling popups 
time.sleep(5)
allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#for free version of Tinder,per day only 100 swipes allowed.
for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()