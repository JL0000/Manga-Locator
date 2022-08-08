from bs4 import BeautifulSoup
import requests
import re

class Website():
    def __init__(self):
        self.base_html = "anysite.com"
        self.search_prefix = "/search?q="
        self.search_suffix = "&page="

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
                good_match = self.get_match(match, manga_name)
                if good_match:
                    all_matches.append(good_match)
            page += 1
        return all_matches

    def get_search(self, html, manga_name):
        html += self.search_prefix
        first_word = True
        words = manga_name.split()
        for word in words:
            if first_word:
                html += word
                first_word = False
            else:
                html  += ("+" + word)
        return html + self.search_suffix

    def get_soup(self, search, page):
        page = requests.get(search + str(page))
        return BeautifulSoup(page.content, 'html.parser')
    
    def is_one_match(self, soup):
        return False
    
    def get_one_match(self, soup):
        pass
    
    def get_match(self, match, manga_name):
        name = self.get_name(match)
        if self.name_is_correct(name, manga_name):
            price = self.get_price(match)
            link = self.get_link(match)
            return self.create_entry(name, price, link)
        else:
            return []
        
    def name_is_correct(self, name, manga_name):
        words1 = re.split("\W+", manga_name.lower())
        words2 = re.split("\W+", name.lower())
        if set(words1).issubset(words2):
            return True
        else:
            return False

    def find_matches(self, soup):
        pass

    def get_name(self, match):
        pass

    def get_price(self, match):
        pass

    def get_link(self, match):
        pass

    def create_entry(self, name, price, link):
        return {"name": name, "price": price, "link": link,}