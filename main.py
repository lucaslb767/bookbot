BOOK_PATH = "books/frankenstein.txt"

def word_counter(s: str):
    return len(s.split())
def char_counter(s:str):
    char_dict = {}

    for char in s.lower():
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    
    return char_dict

def aggregator(s, d):
    print(f"--- Begin report of {BOOK_PATH} ---")
    print(f"{word_counter(s)} words found in the document\n")

    sorted_dict = {k: v for k,v in sorted(d.items(), reverse=True, key = lambda item: item[1])}

    for k, v in sorted_dict.items():
        if k.isalpha():
            print(f"The '{k}' character was found {v} times")

    print("--- End report ---")

def main():

    with open(BOOK_PATH, 'r') as f:
        file_contents = f.read()

    char_dict = char_counter(file_contents)

    aggregator(file_contents, char_dict)

main()