from util import *
from TravellingMan import TravellingMan
from Waterstones import Waterstones

def main():
    book_name = get_book_name()
    matches = []
    # tm = TravellingMan()
    ws = Waterstones()
    matches.extend(ws.get_matches(book_name))
    append_to_csv(matches)

if __name__ == "__main__":
    main()

