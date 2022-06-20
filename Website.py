from bs4 import BeautifulSoup
import requests

class Website():
    def __init__(self):
        self.base_html = "anysite.com"
        
    def get_search(self, html, book_name):
        html += "/search?q="
        first_word = True
        words = book_name.split()
        for word in words:
            if first_word:
                html += word
                first_word = False
            else:
                html  += ("+" + word)
        return html + "&page="

    def get_matches(self, book_name):
        search = self.get_search(self.base_html, book_name)
        all_matches = []
        result = True
        page = 1
        while(result):  
            result = False
            soup = self.get_soup(search, str(page))
            matches = self.search_matches(soup)
            for match in matches:
                name = self.search_name(match)
                price = self.search_price(match)
                link = self.search_link(match)
                if name:
                    result = True
                all_matches.append({
                    "name": name,
                    "price": price,
                    "link": link,
                })
            page += 1
        return all_matches
    
    def get_soup(self, search, page):
        page = requests.get(search + str(page))
        return BeautifulSoup(page.content, 'html.parser')

    def search_matches(self, soup):
        pass
    
    def search_name(self, match):
        pass
    
    def search_price(self, match):
        pass

    def search_link(self, match):
        pass