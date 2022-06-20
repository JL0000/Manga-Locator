from bs4 import BeautifulSoup
import requests

class Website():
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
        p = 1
        while(result):  
            result = False
            page = requests.get(search + str(p))
            soup = BeautifulSoup(page.content, 'html.parser')
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
            p += 1
        return all_matches

    def search_matches(self, soup):
        pass
    
    def search_name(self, match):
        pass
    
    def search_price(self, match):
        pass

    def search_link(self, match):
        pass