from Websites.Website import Website

class BookDepository(Website):
    def __init__(self):
        self.base_html = "https://www.bookdepository.com"
        self.search_prefix = "/search?searchTitle="
        self.search_suffix = "&searchLang=123&category=2634&advanced=true&page="
        
    def find_matches(self, soup):
        return soup.select("div.book-item")
    
    def one_match(self, soup):
        return True if soup.select("div.item-block") else False
    
    def get_one_match(self, soup):
        match = soup.select("div.item-block")[0]
        name = match.select("div.item-info > h1")[0].text.strip()
        price = match.select("div.price-info-wrap span.sale-price")
        if price:
            price = price[0].text.strip()
        else:
            price = "Sold out"
        link = soup.find("link",{"rel":"canonical"})['href']
        return [self.create_entry(name, price, link)]


    def get_name(self, match):
        return match.select("div.item-info > h3.title > a")[0].text.strip()
    
    def get_price(self, match):
        price = match.select("div.item-info > span.sale-price")
        if price:
            return price[0].text.strip()
        else:
            return "Sold out"
    
    def get_link(self, match):
        return self.base_html + match.select("div.item-info > h3.title > a")[0].get("href")
        
