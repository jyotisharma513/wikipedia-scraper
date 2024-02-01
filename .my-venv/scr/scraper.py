
import requests
import json

root_url='https://country-leaders.onrender.com'
r=requests.get(root_url)

# assign the /status endpoint to another variable called status_u
status_url = "/status"

# query the /status endpoint using the get() method and store it in the req variable
req = requests.get(f'{root_url}/{status_url}')

# check the status_code using a condition and print appropriate messages
if req.status_code == 200:
    print("Everything okay !")
else:
    print(f"Error: {req.status_code}")
leaders = req.text
#print(leaders)

#cookies
cookie_url = '/cookie'
req1=requests.get(f'{root_url}/cookie')
cookies=req1.cookies
#print(cookies)


country_url='/countries'
req2 = requests.get(f'{root_url}{country_url}',cookies=cookies).json()
#print(req2)

leaders_url='/leaders'
req3 = str(requests.get(f'{root_url}{leaders_url}',cookies=cookies,params={"country":'be'}).json())
#print(req3)

from bs4 import BeautifulSoup
soup=BeautifulSoup(req3,'html.parser')
pretty_soup=soup.prettify()
#print(pretty_soup)

leader_url='/leader'
req4 = requests.get(f'{root_url}{leader_url}',cookies=cookies,params={'leader_id': 'Q721772'}).json()
#print(req4)


jules_url='https://nl.wikipedia.org/wiki/Jules_Vandenpeereboom'
req4=requests.get(jules_url)
soup=BeautifulSoup(req4.content,'html.parser')
#print(soup)
first_paragraph = soup.find('p').get_text()
#print(first_paragraph)

first_paragraph = ""
for p in soup.find_all("p"):
    first_paragraph = p.get_text()
    break


def get_first_paragraph(wikipedia_url):
    print(wikipedia_url)
    req4=requests.get(wikipedia_url)
    soup=BeautifulSoup(req4.content,'html.parser')
    #print(soup)
    first_paragraph = soup.find('p').get_text()
    print(first_paragraph)


get_first_paragraph(wikipedia_url='https://fr.wikipedia.org/wiki/Agnes_Nixon')


#   print(wikipedia_url) # keep this for the rest of the notebook
#   [insert your code]
#   return first_paragraph

