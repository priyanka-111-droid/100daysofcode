from bs4 import BeautifulSoup
import requests
import lxml 

ZILLOW_URL="https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
INCOMPLETE_LINK="https://www.zillow.com"
class Zillow:
    def __init__(self):
        self.response=requests.get(url=ZILLOW_URL,headers=headers)
        self.soup = BeautifulSoup(self.response.text, "lxml")
        self.address_list=[]
        self.prices_list=[]
        self.links_list=[]

    def getting_address(self):
        all_address=self.soup.select(".list-card-addr")
        for value in all_address:
            value_address=value.text
            if '|' in value_address:
                value_address=value_address.split("|")[-1]

            self.address_list.append(value_address)


    def getting_prices(self):
        all_prices=self.soup.select(".list-card-price")
        for value in all_prices:
            value_price=value.text
            if '+' in value_price:
                value_price=value_price.split("+")[0]
            else:
                value_price=value_price.split("/")[0]

            self.prices_list.append(value_price)

    def getting_links(self):
        all_links=self.soup.select(".list-card-top a")
        for value in all_links:
            value_link=value.get('href')

            #some links scraped might be incomplete 
            if INCOMPLETE_LINK not in value_link:
                value_link=f"{INCOMPLETE_LINK}{value_link}"
            self.links_list.append(value_link)
            

    def return_all_data(self):
        all_data=[[self.address_list[x],self.prices_list[x],self.links_list[x]] for x in range(len(self.address_list))]
        return all_data

    


