#get_book_text focuses on reading a file and returning text.

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

#importing get_num_words which uses len on the string to get number of words
from stats import get_num_words
from stats import character_counter
#main focuses on program flow: which file to read, and what to do with the result.

def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    char_counts = character_counter(text)
    print(char_counts)

main()