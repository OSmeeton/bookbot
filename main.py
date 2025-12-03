import sys

#get_book_text focuses on reading a file and returning text.

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#importing get_num_words which uses len on the string to get number of words
from stats import get_num_words
from stats import character_counter
from stats import build_and_sort
#main focuses on program flow: which file to read, and what to do with the result.

def main():
    num_args = len(sys.argv)
    if num_args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    char_counts = character_counter(text)
    sorted_chars = build_and_sort(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

    print("============= END ===============")

main()