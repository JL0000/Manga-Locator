import csv

def get_book_name():
    book_name = input("Enter book name: ")
    return book_name.strip()

def append_to_csv(all_matches):
    keys = all_matches[0].keys()

    with open('matches.csv', 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_matches)