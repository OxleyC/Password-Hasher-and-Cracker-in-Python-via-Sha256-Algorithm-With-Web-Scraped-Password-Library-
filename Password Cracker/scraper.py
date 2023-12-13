from bs4 import BeautifulSoup
import requests

class Scraper:
    def __init__(self):
        url = "https://en.wikipedia.org/wiki/Wikipedia:10,000_most_common_passwords"        
        self.response = requests.get(url)
        
    def scraper(self):
    
        #print("\nSCRAPER: Scraping Passwords")
        
        soup = BeautifulSoup(self.response.text, 'html.parser')
            
        div_col_elements = soup.find_all(class_='div-col')
        
        passwordList = []
            
        for element in div_col_elements:
            
            #print(element.prettify())
            
            list_items = element.find_all('li')
                
                
            for list_item in list_items:
                
                passwordList.append(list_item.text)
                    
            
        print("SCRAPER: Printing password list")
        
        passCounter = 0
        
        for passInList in passwordList:
            
            print(passCounter, ":", passInList)
            passCounter += 1
            
        return passwordList
            