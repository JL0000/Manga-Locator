from Website import Website

class TravellingMan(Website):
    def __init__(self):
        self.base_html = "https://travellingman.com"

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

    def search_matches(self, soup):
        return soup.select("div.product-card--list")

    def search_name(self, match):
        return match.select("a > span")[0].text.strip()
    
    def search_price(self, match):
        price = match.select("div.list-view-item__link > div.list-view-item__price-column > dl > div.price__regular > dd > span ")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def search_link(self, match):
        return self.base_html + match.select("a")[0].get("href")
        


