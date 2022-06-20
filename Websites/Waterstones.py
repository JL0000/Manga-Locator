from Websites.Website import Website
import cloudscraper
from bs4 import BeautifulSoup

class Waterstones(Website):
    def __init__(self):
        self.base_html = "https://www.waterstones.com"

    def get_soup(self, search, page):
        scraper = cloudscraper.create_scraper(delay=10,   browser={'custom': 'ScraperBot/1.0',})
        req = scraper.get(search + page)
        return BeautifulSoup(req.content, 'html.parser')

    def get_search(self, html, book_name):
        html += "/books/search/term/"
        first_word = True
        words = book_name.split()
        for word in words:
            if first_word:
                html += word
                first_word = False
            else:
                html  += ("+" + word)
        return html + "/category/394/facet/347/page/"

    def one_match(self, soup):
        return True if soup.select("section.book-detail") else False
    
    def get_match(self, soup):
        match = soup.select("section.book-detail")[0]
        name = match.find("span", {"id": "scope_book_title"}).text.strip()
        availability = match.select("#scope_offer_availability")[0].text.strip()
        if availability == "Not available":
            price = "Not available"
        else:
            price = match.select("div.price > b")[0].get("itemprop")

        link = soup.find("meta",{"name":"og:url"})['content']
        return [self.create_entry(name, price, link)]

    def search_matches(self, soup):
        return soup.select("div.info-wrap")

    def search_name(self, match):
        return match.select("div.title-wrap > a")[0].text.strip()
    
    def search_price(self, match):
        in_stock = match.select("div.book-price > span.format")
        if not in_stock[0].text:
            return "Sold out"
        else:
            return match.select("div.book-price > span.price")[0].text.strip()
    
    def search_link(self, match):
        return self.base_html + match.select("div.title-wrap > a")[0].get("href")
        


