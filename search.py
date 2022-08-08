from util import *
from Websites.TravellingMan import TravellingMan
from Websites.Waterstones import Waterstones
from Websites.BookDepository import BookDepository
from Websites.Blackwells import Blackwells

def main():
    manga_name = get_manga_name()
    matches = []
    tm = TravellingMan()
    ws = Waterstones()
    bd = BookDepository()
    bw = Blackwells()
    matches.extend(tm.get_matches(manga_name))
    matches.extend(ws.get_matches(manga_name))
    matches.extend(bd.get_matches(manga_name))
    matches.extend(bw.get_matches(manga_name))
    if matches:
        append_to_csv(matches, manga_name)
    else:
        print("No matches")

if __name__ == "__main__":
    main()

