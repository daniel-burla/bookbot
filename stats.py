def get_num_words(book_text):
    count = len(book_text.split())
    return count

def char_counter(book_text):
    char_low = list(book_text.lower())
    counter = {}
    for char in char_low:
        if char in counter:
            counter[char] = counter[char] + 1
        else:
            counter[char] = 1
    return counter  # Just return the counter dictionary

def sort_char_count(char_dict):
    # Create a list to hold our dictionaries
    chars_list = []
    
    # Loop through the character dictionary
    for char, count in char_dict.items():
        # Create a dictionary for each character and its count
        char_info = {"char": char, "count": count}
        # Add this dictionary to our list
        chars_list.append(char_info)
    
    # Define a function to extract the count from a dictionary
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list using our function as the key
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
