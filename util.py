import csv

def get_manga_name():
    manga_name = input("Enter book name: ")
    return manga_name.strip()

def append_to_csv(all_matches, manga_name):
    keys = all_matches[0].keys()

    with open(manga_name + ".csv", 'a', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(all_matches)