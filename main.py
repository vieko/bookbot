from sys import argv
from stats import count_words, count_individual_characters, sort_list_of_dictionaries

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if len(argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        exit(1)
    
    book_text = get_book_text(argv[1])
    num_words = count_words(book_text)
    character_dict = count_individual_characters(book_text)
    list_of_dicts = sort_list_of_dictionaries(character_dict)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for dict in list_of_dicts:
        if dict["character"].isalpha():
            print(f'{dict["character"]}: {dict["count"]}')
    print('============= END ===============')


if __name__ == '__main__':
    main()

