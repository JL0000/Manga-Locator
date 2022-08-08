from bs4 import BeautifulSoup
import requests
from Websites.Website import Website

class Blackwells(Website):
    def __init__(self):
        self.base_html = "https://blackwells.co.uk"
        self.search_prefix = "/bookshop/search/?productTitle="
        self.search_suffix = "&offset="
        self.languages = ["German", "French", "Spanish", "Japanese"]

    def get_matches(self, manga_name):
        search = self.get_search(self.base_html, manga_name)
        all_matches = []
        result = True
        page = 1
        while(result):  
            result = False
            soup = self.get_soup(search, page)
            if self.is_one_match(soup):
                return self.get_one_match(soup)
            matches = self.find_matches(soup)
            if matches:
                result = True
            for match in matches:
                language = match.select("p.product-format span")
                if len(language) > 1 and language[1].text.strip() not in self.languages:
                    all_matches.append(self.get_match(match, manga_name))
            page += 1
        return all_matches
        
    def get_soup(self, search, page):
        offset = (page - 1) * 48
        page = requests.get(search + str(offset))
        return BeautifulSoup(page.content, 'html.parser')

    def find_matches(self, soup):
        return soup.select("li.search-result__item div.product-info")

    def get_name(self, match):
        return match.select("h4 a.product-name")[0].text.strip()
    
    def get_price(self, match):
        price = match.select("div.product-price li.product-price--current")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def get_link(self, match):
        return self.base_html + match.select("h4 a.product-name")[0].get("href")
        
        