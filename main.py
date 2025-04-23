from stats import get_num_words, char_counter, sort_char_count
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    aux = (len(sys.argv))
    if aux != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        book = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words") 
    print("--------- Character Count -------")
    
    # Get the character count dictionary
    char_dict = char_counter(text)
    
    # Get the sorted list of character dictionaries
    sorted_chars = sort_char_count(char_dict)
    
    # Print each character and its count
    for char_info in sorted_chars:
        char = char_info["char"]
        count = char_info["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

main()