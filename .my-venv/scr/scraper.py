import requests
import json
from bs4 import BeautifulSoup

class WikipediaScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.country_endpoint = "/countries"
        self.leaders_endpoint = "/leaders"
        self.cookies_endpoint = "/cookie"
        self.leaders_data = {}
        self.session = requests.Session()

    def refresh_cookie(self):
       """
       Refreshes the user cookie and returns it.

       This function sends a GET request to the cookies endpoint and returns the user cookie.
       """
       cookie_req = self.session.get(self.base_url + self.cookies_endpoint)
       cookie_req.raise_for_status()
       return cookie_req.cookies.get('user_cookie')
        

    def get_countries(self):
        """
        Refreshes the cookie and returns a JSON object containing the list of countries.
        """
        self.refresh_cookie()
        countries_url = self.base_url + self.country_endpoint
        countries_req = self.session.get(countries_url)
        countries_req.raise_for_status()
        return countries_req.json()

    def get_leaders(self, country):
        """
        Fetches the leaders of a given country from the API and stores the data in a JSON file.
        """
        self.refresh_cookie()
        leaders_url = f"{self.base_url}{self.leaders_endpoint}?country={country}"
        leaders_req = self.session.get(leaders_url)
        leaders_req.raise_for_status()
        country_leaders = []
        for leader in leaders_req.json():
            if leader:
                leader_info = {
                    "first_name": leader.get("first_name"),
                    "last_name": leader.get("last_name"),
                    "wikipedia_url": leader.get("wikipedia_url"),
                    "first_paragraph": self.get_first_paragraph(leader.get("wikipedia_url"))
                }
                print(f"Full Name: {leader_info['first_name']} {leader_info['last_name']}")
                print(f"Wikipedia URL: {leader_info['wikipedia_url']}")
                print(f"First Paragraph: {leader_info['first_paragraph']}\n")
                country_leaders.append(leader_info)
        self.leaders_data[country] = country_leaders
        self.to_json_file("leaders_data.json")



    def get_first_paragraph(self, wikipedia_url):
        """this will fetch the first paragraph """
        response = self.session.get(wikipedia_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        for tag in soup.find_all("p"):
            if "<p><b>" in str(tag):
                extract_first_paragraph = tag
                return extract_first_paragraph.get_text()

    def to_json_file(self, filepath):
        """
        This method writes the contents of the 'leaders_data' dictionary to a JSON file.
    
        :param filepath: The path of the file to write to.
        """
        with open(filepath, 'w') as json_file:
            json.dump(self.leaders_data, json_file, indent=4)

