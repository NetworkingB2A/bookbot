import sys
from stats import (
   get_number_of_words, 
   get_char_dict, 
   get_sorted_dict_list
   )

def get_book_text(file_path: str) -> str:
    with open(file_path, mode="r", encoding='utf-8-sig') as file:
        return file.read()

def print_report(list_char):
    list_text = ""
    for item in list_char:
      if item['char'].isalpha(): 
        list_text = list_text + item["char"] + ": " + str(item["num"]) + "\n"
    return list_text.rstrip()

def main():
    if len(sys.argv) != 2:
      print("Usage: python3 main.py <path_to_book>")
      sys.exit(1) 
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_number_of_words(book_text)
    letter_count = get_char_dict(book_text)
    sorted_letter_count = get_sorted_dict_list(letter_count)
    

#     #TODO: Move this var up to a function
#     #EXTRA: I could convert this over to a jinja2 template not needed but would be cooler
    report_var = f"""
============ BOOKBOT ============
Analyzing book found at { book_path}...
----------- Word Count ----------
Found { num_words } total words
--------- Character Count -------
{ print_report(sorted_letter_count) }
============= END ==============="""
    print(report_var)


if __name__ == "__main__":
  main()