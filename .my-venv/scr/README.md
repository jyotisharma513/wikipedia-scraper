Name of the Project:
Web Scraper

Description:

We Created a scraper that builds a JSON file with the political leaders of each country we get from an API.
Also included in this file the first paragraph of the Wikipedia page of these leaders (we retrieved the Wikipedia page URL from the API, which we had to scrape ourself).
To do that we made a scraper.py file in which we made a class Wikipedia Scraper with various attributes like base_url,country_endpoint,leaders_endpoint,cookies_endpoint,leaders_data.And also created various methods like
refresh_cookie,get_countries,get_leaders,get_first_paragraph, to_json_file.Then we bundled everything together in a main.py file that calls the WikipediaScraper object and saves the data into a JSON file.

Installation:
->we use venv to isolate our virtual Python environment
->Install requests 
->Install BeautifulSoup to extract text from HTML


Usage:
One can try this project by going to the public repository whose link is given below
https://github.com/jyotisharma513/wikipedia-scraper

Visuals:
Here are some of the visuals:
![image](https://github.com/jyotisharma513/wikipedia-scraper/assets/156506456/91a8b35e-b8e2-4069-b4ab-b3d4034467fd)
![image](https://github.com/jyotisharma513/wikipedia-scraper/assets/156506456/6609dca8-3e3d-434f-95d0-ca94b34ab0bb)




