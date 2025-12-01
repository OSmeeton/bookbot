#getting word count
def get_num_words(text):
    words_in_book = text.split()
    count = len(words_in_book)
    return count

#Counting Characters
def character_counter(letters):
    letter_dict = {}
    for letter in letters:
        lower_letter = letter.lower()
        if lower_letter in letter_dict: 
            letter_dict[lower_letter] += 1
        else:
            letter_dict[lower_letter] = 1
    return letter_dict
