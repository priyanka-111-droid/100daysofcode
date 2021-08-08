from selenium import webdriver
import time

CHROME_DRIVER_PATH="C:\Python_development\chromedriver.exe" #only for windows machine
driver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

COOKIE_URL="http://orteil.dashnet.org/experiments/cookie/"

driver.get(COOKIE_URL)
get_cookie=driver.find_element_by_id("cookie")

#Making this upgrades dictionary
# upgrades={
#     "Cursor":15,
#     "Grandma":100,
#     "Factory":500,
#     "Mine":2000,
#     "Shipment":7000,
#     "Alchemy Lab":50000,
#     "Portal":1000000,
#     "Time machine":123456789
# }
items=driver.find_elements_by_css_selector("#store b")
ids=[]
cost=[]
for value in items:
    val=(value.text.strip().split(" - "))
    if(len(val)!=1):
        ids.append(val[0])
        cost.append(int(val[len(val)-1].replace(",","")))

upgrades={ids[i]:cost[i] for i in range(len(ids))}
#can also try reversing dictionary
# upgrades=dict(reversed(list(upgrades.items())))



#main loop
five_sec = time.time()+5
five_min=time.time()+60*5

while True:
    get_cookie.click()
    if time.time()>five_sec:
        money=driver.find_element_by_id("money").text.replace(",","")
        possible_upgrades=[]
        possible_ids=[]
        for x in upgrades:
            if int(money)>upgrades[x]:
                possible_upgrades.append(upgrades[x])
                possible_ids.append(f"buy{x}")
        
        highest_affordable_upgrade=max(possible_upgrades)
        temp_index=possible_upgrades.index(highest_affordable_upgrade)
        purchase_upgrade=driver.find_element_by_id(possible_ids[temp_index])
        purchase_upgrade.click()

        #Add another 5 seconds until the next check
        five_sec=time.time()+5
    
    #After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

                
driver.quit()