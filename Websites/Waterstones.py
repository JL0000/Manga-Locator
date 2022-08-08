from Websites.Website import Website
import cloudscraper
from bs4 import BeautifulSoup

class Waterstones(Website):
    def __init__(self):
        self.base_html = "https://www.waterstones.com"
        self.search_prefix = "/books/search/term/"
        self.search_suffix = "/category/394/facet/347/page/"
        self.scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})

    def get_soup(self, search, page):
        req = self.scraper.get(search + str(page))
        return BeautifulSoup(req.content, 'html.parser')

    def is_one_match(self, soup):
        return True if soup.select("section.book-detail") else False
    
    def get_one_match(self, soup):
        match = soup.select("section.book-detail")[0]
        name = match.find("span", {"id": "scope_book_title"}).text.strip()
        unavailability = match.select("#scope_offer_availability")[0].text.strip()
        if "available" in unavailability:
            price = "Sold out"
        else:
            price = match.select("div.price b")[0].text.strip()

        link = soup.find("meta",{"name":"og:url"})['content']
        return [self.create_entry(name, price, link)]

    def find_matches(self, soup):
        return soup.select("div.info-wrap")

    def get_name(self, match):
        return match.select("div.title-wrap > a")[0].text.strip()
    
    def get_price(self, match):
        in_stock = match.select("div.book-price > span.format")
        if not in_stock[0].text:
            return "Sold out"
        else:
            return match.select("div.book-price > span.price")[0].text.strip()
    
    def get_link(self, match):
        return self.base_html + match.select("div.title-wrap > a")[0].get("href")
        


