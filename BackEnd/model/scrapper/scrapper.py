from bs4 import BeautifulSoup 
import requests

class Scrapper:
    def __init__(self):
        self.url = None 
        self.header = { 
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
            'Accept-Language' : 'en-US,en;q=0.5',
            'Accept-Encoding' : 'gzip', 
            "Upgrade-Insecure-Requests": "1",
            'DNT' : '1', 
            'Referer' : 'https://www.google.com/search?q=grocery&sxsrf=ALiCzsahLJ4V2ShzqcW0GaXYLjUfbVWqYQ%3A1663610066401&source=hp&ei=0qwoY8P4FfHN9AP2qYKoDg&iflsig=AJiK0e8AAAAAYyi64rj_5ulY-UP5h9Fm-jl6gnXxqOku&ved=0ahUKEwjDqbO4tqH6AhXxJn0KHfaUAOUQ4dUDCAk&uact=5&oq=grocery&gs_lcp=Cgdnd3Mtd2l6EAMyCAgAEMkDEMsBMgUIABCSAzIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBOgQIIxAnOhEILhCABBCxAxCDARDHARDRAzoLCAAQgAQQsQMQgwE6CAguELEDEIMBOgoIABCxAxCDARBDOgQIABBDOgoILhDHARDRAxBDOhMILhCxAxCDARDHARDRAxDUAhBDOgQILhBDOgUIABCABDoICAAQgAQQsQM6BwgAELEDEEM6CwguEMcBEK8BEMsBOgcIIxDqAhAnOgYIIxAnEBM6CgguEMcBENEDECc6EAguELEDEIMBEMcBENEDEEM6BAgAEAM6CAguEIAEELEDOgsILhCABBDHARCvAToUCC4QgAQQsQMQgwEQxwEQrwEQ1AI6CwguELEDEIMBENQCOhEILhCABBCxAxDHARDRAxDUAjoOCC4QgAQQsQMQxwEQrwE6DgguEIAEELEDEMcBENEDOggIABCABBDJAzoHCAAQChDLAToKCAAQyQMQChDLAVAAWI5BYP1DaAhwAHgAgAGAAYgB9wmSAQQxMy4ymAEAoAEBsAEK&sclient=gws-wiz',
            'Connection' : 'close'
            }
    def get_url(self, page):
        self.url = page

    def scrapping(self):
        # try:
        page = requests.get(self.url, self.header)    
        soup = BeautifulSoup(page.content, 'html.parser')
        boxes = soup.find_all('div', class_='clearfix')        
        for i in boxes:
            try:
                name = (i.find('div', class_='title'))    
                print((name.text).strip())
            except:
                pass    
        # except:
        #     print('fail page requests')



def main():

    page = 'https://www.kijiji.ca/b-grand-montreal/iphone-11/k0l80002?rb=true&dc=true'
    s = Scrapper()
    s.get_url(page)
    s.scrapping()



if __name__== '__main__':
    main()  