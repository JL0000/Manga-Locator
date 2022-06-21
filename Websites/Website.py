from bs4 import BeautifulSoup
import requests

class Website():
    def __init__(self):
        self.base_html = "anysite.com"
        self.search_prefix = "/search?q="
        self.search_suffix = "&page="

    def get_matches(self, book_name):
        search = self.get_search(self.base_html, book_name)
        all_matches = []
        result = True
        page = 1
        while(result):  
            result = False
            soup = self.get_soup(search, str(page))
            if self.one_match(soup):
                return self.get_one_match(soup)
            matches = self.find_matches(soup)
            if matches:
                result = True
            for match in matches:
                all_matches.append(self.get_match(match))
            page += 1
        return all_matches

    def get_search(self, html, book_name):
        html += self.search_prefix
        first_word = True
        words = book_name.split()
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
    
    def one_match(self, soup):
        return False
    
    def get_one_match(self, soup):
        pass
    
    def get_match(self, match):
        name = self.get_name(match)
        price = self.get_price(match)
        link = self.get_link(match)
        return self.create_entry(name, price, link)

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