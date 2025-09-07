import sys

from stats import  count_words
from stats import  count_characters
from stats import  get_book_text
from stats import  sort_dictionary



def main():

    if len(sys.argv) < 2:
        print("Wrong input! Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    message = f"{num_words} words found in the document"
    

    chr_dict = count_characters(text)
    dict_list = sort_dictionary(chr_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dict in dict_list:
        char = dict["char"]
        if not char.isalpha():
            continue
        num = dict["num"]
        print(f"{char}: {num}")
    print("============= END ===============")


main()