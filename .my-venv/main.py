
from time import perf_counter
start_time = perf_counter()
from scr.scraper import WikipediaScraper

if __name__ == "__main__":
    
    
    wiki = WikipediaScraper(base_url="https://country-leaders.onrender.com")

    countries = wiki.get_countries()

    if countries:
        for country in countries:
            wiki.get_leaders(country)

        # Save the leaders data into a JSON file
        wiki.to_json_file(filepath="leaders_data.json")
print(f"\nTime spent to finish the task: {perf_counter() - start_time} seconds.")    


    


