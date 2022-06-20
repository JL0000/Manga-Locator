from util import *
from TravellingMan import TravellingMan

def main():
    book_name = get_book_name()
    matches = []
    tm = TravellingMan()
    matches.extend(tm.get_matches(book_name))
    append_to_csv(matches)

if __name__ == "__main__":
    main()

