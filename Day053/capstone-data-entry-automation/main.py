from selenium import webdriver
from zillow import Zillow
from form import Form

#getting details from zillow into separate lists
obj=Zillow()
obj.getting_address()
obj.getting_prices()
obj.getting_links()

#combining above three into one list
all_data=obj.return_all_data()

#filling up the forms
CHROME_DRIVER_PATH="C:\Python_development\chromedriver.exe" 
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

form=Form(driver,all_data)
form.filling_info()

