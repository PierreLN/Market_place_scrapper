from model.scrapperAndUtilities.scrapper import Scrapper

def main():
    s = Scrapper()
    page = 'https://www.kijiji.ca/b-grand-montreal/iphone-11/k0l80002?rb=true&dc=true'
    s.get_url(page)
    s.scrapping()

if __name__=='__main__':
    main()