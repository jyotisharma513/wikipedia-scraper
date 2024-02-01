from scr.scraper1 import WikipediaScraper
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":


    wiki=WikipediaScraper("https://country-leaders.onrender.com")
    countries=wiki.get_countries()
    print(countries)
    

