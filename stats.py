def sort_on(items):
    return items["num"]

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def count_words(text):
    word_list = text.split()
    return len(word_list)

def count_characters(text):
    chr_list = list(text)
    chr_dict = {}
    for character in chr_list:
        chr = character.lower()
        if chr in chr_dict:
            current_number = chr_dict[chr]
            current_number += 1
            chr_dict[chr] = current_number
        else:
            chr_dict[chr] = 1
    return chr_dict

def sort_dictionary(dict):
    dict_list = []
    for key in dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = dict[key]
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list