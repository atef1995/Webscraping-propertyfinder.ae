import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time


url = "https://www.propertyfinder.ae/"

class propertyFinder:

    def click_on_search(self):
        self.driver = webdriver.Chrome()

        # Navigate to the Property Finder website
        self.driver.get(url)
        self.driver.maximize_window()
        self.action_chains = ActionChains(self.driver)
        # Wait until the search button is visible on the page
        buy_button = self.driver.find_element(By.XPATH,"//a[normalize-space()='Buy']")
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Buy']"))
        )

        # Click the search button
        buy_button.click()
        for i in range(4):
            print('page',i+1)
            current_url = self.driver.current_url
            self.scrape_info(current_url)
            self.scroll_then_next()

    def scroll_then_next(self):
        next = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Next']")))
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});", next)
        next.click()
        print("clicked on next")
        self.scrape_info(self.driver.current_url)

    def scrape_info(self,url):

        WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='card-list card-list--property ']")))
        # send a GET request to the website and store the response
        response = requests.get(url,allow_redirects=True,headers={'User-Agent': 'Custom'})

        # parse the HTML content of the response using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # find all the property cards on the page
        # property_cards = soup.find_all("div",{"data-qs":"cardlist"})

        cards = soup.find_all("div",{"class":"card-list__item"})

        # loop through each property card and extract the relevant information
        for property_card in cards:

            price = property_card.find("div",{"class":"card__content"}).find("p",{"class":"card-intro__price"}).text.replace("\n"," ").replace(" ","")
            address = property_card.find("div",{"class":"card__content"}).find("p",{"class":"card-specifications__location"}).text
            link = property_card.find("article",{"class":"card"}).find("a")["href"]
            full_link = "".join(("https://www.propertyfinder.ae",link))
            print(price,address,full_link)
            
            # extract the property title
            # property_title = property_card.find("div", {"class": "card__title"}).text.strip()
            # print("Property Title:", property_title,"\n-"*10)
            
            # extract the property price
            # property_price = property_card.find("div", {"class": "card-intro__price-area"}).text.strip()
            # print("Property Price:", property_price,"-"*10)
            
            # # extract the property location
            # property_location = property_card.find("span", {"class": "card__location-text"}).text.strip()
            # print("Property Location:", property_location,"\n-"*10)
            
            # extract the number of bedrooms
            # property_bedrooms = property_card.find("div", {"class": "card-specifications__location"}).text.strip()
            # print("Property Bedrooms:", property_bedrooms,"\n-"*10)
            
            # # extract the number of bathrooms
            # property_bathrooms = property_card.find("div", {"class": "card__property-amenity card__property-amenity--bathrooms"}).find("span", {"class": "card__property-amenity-value"}).text.strip()
            # print("Property Bathrooms:", property_bathrooms,"\n-"*10)
            
            # # extract the size of the property
            # property_size = property_card.find("div", {"class": "card__property-amenity card__property-amenity--area"}).find("span", {"class": "card__property-amenity-value"}).text.strip()
            # print("Property Size:", property_size,"\n-"*10)
            
            print("-" * 50)
            

pr = propertyFinder()
pr.click_on_search()