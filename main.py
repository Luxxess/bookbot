def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words = get_count_words(text)
    #print(f"{count_words} words found in the document")
    charachters = get_count_characters(text)
    #print(f"The book has {charachters} of each character")
    sort_dict(charachters)


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
    
def sort_dict(characters):
    for c in characters:
        print(characters[c])
        
main()