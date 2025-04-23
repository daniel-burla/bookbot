from stats import get_num_words, char_counter, sort_char_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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