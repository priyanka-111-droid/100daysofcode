# Import Module
import time

from dotenv import load_dotenv
import os
# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Connect the path with your '.env' file name
load_dotenv(os.path.join(BASEDIR, '.env'))

GOOGLE_FORM_URL=os.getenv('GOOGLE_FORM_URL')

#start of class
class Form:
    def __init__(self,driver,datas):
    
        self.driver=driver 
        self.datas=datas

    def filling_info(self):

        #Get URL
        self.driver.get(GOOGLE_FORM_URL)

        #loading time
        time.sleep(1)

        # Iterate through each data
        for data in self.datas:
            # Initialize count is zero
            count = 0

            # contain input boxes
            textboxes = self.driver.find_elements_by_class_name(
                "quantumWizTextinputPaperinputInput")

            # Iterate through all input boxes
            for value in textboxes:
                # enter value
                value.send_keys(data[count])
                # increment count value
                count += 1

            # click on submit button
            submit = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
            submit.click()

            # fill another response
            another_response = self.driver.find_element_by_xpath(
                '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()


        # close the window
        self.driver.close()


