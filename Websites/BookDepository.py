from Websites.Website import Website

class BookDepository(Website):
    def __init__(self):
        self.base_html = "https://www.bookdepository.com"

    def get_search(self, html, book_name):
        return html + "/search?searchTerm=" + book_name + "&page="

    def search_matches(self, soup):
        return soup.select("div.book-item")

    def search_name(self, match):
        return match.select("div.item-info > h3.title > a")[0].text.strip()
    
    def search_price(self, match):
        price = match.select("div.item-info > div.price-wrap > p.price > span.sale-price")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def search_link(self, match):
        return self.base_html + match.select("div.item-info > h3.title > a")[0].get("href")
        


