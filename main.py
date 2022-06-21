from util import *
from Websites.TravellingMan import TravellingMan
from Websites.Waterstones import Waterstones
from Websites.BookDepository import BookDepository

def main():
    book_name = get_book_name()
    matches = []
    tm = TravellingMan()
    ws = Waterstones()
    bd = BookDepository()
    matches.extend(tm.get_matches(book_name))
    matches.extend(ws.get_matches(book_name))
    matches.extend(bd.get_matches(book_name))
    append_to_csv(matches, book_name)

if __name__ == "__main__":
    main()

