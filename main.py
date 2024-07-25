def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    chars_dict = get_count_characters(text)
    sort_dict(chars_dict)
    list_dict = sort_list(chars_dict)
    output(count_words, list_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_count_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    l_text = text.lower()
    characters = {
    'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0,
    'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
    'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0,
    'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0,
    'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0,
    'z': 0
    }
    
    for char in characters:
        test = l_text.count(char)
        characters[char] = test

    return characters
    
def sort_dict(chars_dict):

    new_dict = {}
    for c in chars_dict:
        new_dict[c] = new_dict["num"] = chars_dict[c]
    return new_dict["num"]

def sort_list(chars_dict):
    list_dict = []
    for c in chars_dict:
        temp = {}
        temp[c] = chars_dict[c]
        list_dict.append(temp)
    list_dict.sort(reverse=True, key=sort_dict)
    return (list_dict)

def output(count_words, list_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count_words} words found in the document\n")
    for letter in list_dict:
        for char in letter:
            print(f"The '{char}' character was found {letter[char]} times")
    print("--- End report ---")
    return 0


main()