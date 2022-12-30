from bs4 import BeautifulSoup 
import requests
from model.object.header import Headers



class Scrapper:
    def __init__(self):
        self.url = None 
        self.header = Headers().HEADER_1
    def get_url(self, page):
        self.url = page

    def scrapping(self) -> dict:
        data_dict = {}
        # try:
        page = requests.get(self.url, self.header)    
        soup = BeautifulSoup(page.content, 'html.parser')
        boxes = soup.find_all('div', class_='clearfix')        
        for i in boxes:
            try:
                name_section = (i.find('div', class_='title'))    
                name = (name.text).strip()
            except:
                name = None
            # try:
            #     price =     
        # except:
        #     print('fail page requests')

            print(name)
        return data_dict


def main():

    page = 'https://www.kijiji.ca/b-grand-montreal/iphone-11/k0l80002?rb=true&dc=true'
    s = Scrapper()
    s.get_url(page)
    s.scrapping()



if __name__== '__main__':
    main()  