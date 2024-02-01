import requests
from bs4 import BeautifulSoup
import json
class WikipediaScraper():
    def __init__(self,base_url):
        self.base_url=base_url
        self.country_endpoint='/countries'
        self.leaders_endpoint='/leaders'
        self.cookies_endpoint='/cookie'
        self.leaders_data=[]
        #self.cookie=cookie

    def check_status(self):
          r=requests.get(self.base_url)
          self.status_url = "/status"
          req = requests.get(f'{self.base_url}/{self.status_url}')
          if req.status_code == 200:
            print("Everything okay !")
          else:
           print(f"Error: {req.status_code}")
         
         

    def refresh_cookie(self):
        cookies_endpoint = '/cookie'
        req1=requests.get(f'{self.base_url}/cookie')
        cookies=req1.cookies
        print(cookies)

    def get_countries(self):
        cookie=self.refresh_cookie
        req2 = requests.get(f'{self.base_url}{self.country_endpoint}',cookies=self.cookies).json()
        return req2
"""
    def get_leaders(self):
        cookie=self.refresh_cookie
        leader_data=[]
        countries=self.get_countries()
        for country in countries:
           params={'country':countries}
           leader_response=requests.get(f'{self.base_url}{self.leader_details.append(leader_response.text)}')
           return(leader_data)
     

    first_paragraph = ""
    #for p in soup.find_all("p"):
    #first_paragraph = p.get_text()
       #break

    def get_first_paragraph(wikipedia_url):
      cookie=self.refresh_cookie
      print(wikipedia_url)
      req4=requests.get(wikipedia_url)
      soup=BeautifulSoup(req4.content,'html.parser')
      #print(soup)
      first_paragraph = soup.find('p').get_text()
      print(first_paragraph)

    def to_json_file(self):
        pass

"""