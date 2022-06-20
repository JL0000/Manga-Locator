from Websites.Website import Website

class BookDepository(Website):
    def __init__(self):
        self.base_html = "https://www.bookdepository.com"

    def get_search(self, html, book_name):
        html += "/search?searchTitle="
        first_word = True
        words = book_name.split()
        for word in words:
            if first_word:
                html += word
                first_word = False
            else:
                html  += ("+" + word)
        return html + "&searchLang=123&category=2634&advanced=true&page="
    
    def one_match(self, soup):
        return True if soup.select("div.item-block") else False
    
    def get_match(self, soup):
        match = soup.select("div.item-block")[0]
        name = match.select("div.item-info > h1")[0].text.strip()
        price = self.search_price(match)
        link = soup.find("link",{"rel":"canonical"})['href']
        return [self.create_entry(name, price, link)]

    def search_matches(self, soup):
        return soup.select("div.book-item")

    def search_name(self, match):
        return match.select("div.item-info > h3.title > a")[0].text.strip()
    
    def search_price(self, match):
        price = match.select("div.item-info > span.sale-price")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def search_link(self, match):
        return self.base_html + match.select("div.item-info > h3.title > a")[0].get("href")
        
