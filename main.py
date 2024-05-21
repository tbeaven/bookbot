def main():
    book_path = "/home/thomasmbeaven/workspace/github.com/tbeaven/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    letter_count = count_letters(text)
    sorted_list_of_tuples = sort_letters_by_frequency(letter_count)

    print(f"--- Begin report of {book_path} ---")
    print(f"This book has {count_words(text)} words.")
    
    for key,value in sorted_list_of_tuples:
        if not key.isalpha():
            continue
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

def get_book_text(path):
    #Read the text from specified book file
    with open(path) as f:
        return f.read()

def count_words(text):
    #Print the number of words in the text
    words = text.split()
    return len(words)

def count_letters(text):
    #Returns a dictionary with no. occurences in the text of each letter of the alphabet
    import string
    letters = {}
    for letter in string.ascii_lowercase:
        letters[letter] = 0
    
    lower_case_text = text.lower()
    for char in lower_case_text:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters

def sort_letters_by_frequency(letter_count):
    #Accepts dictionary and sorts by value size
    
    list_of_tuples = [(key, value) for key, value in letter_count.items()]

    sorted_list_of_tuples = sorted(list_of_tuples, key=lambda item: item[1], reverse=True)

    return sorted_list_of_tuples

main()