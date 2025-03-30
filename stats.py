def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    return len(book_text)

def count_sentences(book_text):
    return len(book_text.split('.'))

def count_paragraphs(book_text):
    return len(book_text.split('\n\n'))

def count_individual_characters(book_text):
    character_dict = {}
    for char in book_text:
        char = char.lower()
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def sort_list_of_dictionaries(dict):
    dicts = []
    for key, value in dict.items():
        dicts.append({'character': key, 'count': value})
    dicts.sort(key=sort_on, reverse=True)
    return dicts
