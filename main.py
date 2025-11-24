#get_book_text focuses on reading a file and returning text.

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents
#main focuses on program flow: which file to read, and what to do with the result.

def main():
    path_to_file = "books/frankenstein.txt"
    run_book_from_path = get_book_text(path_to_file)
    print(run_book_from_path)

#function call expression at the top level of the module
main()
    

