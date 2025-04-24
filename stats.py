

# dictionary containing the alphabet and symbols as keys


# takes the file path and returns the file contents as a string
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents





# counts the number of words in a string
def word_count(path_to_file):
    file_contents = get_book_text(path_to_file)
    text = file_contents.split()
    count = len(text)
    return count
    
    #print(f"{count} words found in the document")



# Turns characters into lower case, then counts each one in a file    
def character_count(path_to_file):
    characters = {}
    text = get_book_text(path_to_file).lower()
    for char in text:
        if char in characters:
            characters[char] +=1
        else:
            characters[char] = 1
    # Sort the dictionary by its keys and return as a new dictionary
    sorted_characters = dict(sorted(characters.items()))
    return sorted_characters        
        
def get_only_alpha(dic):
    alpha_dic = {key: value for key, value in dic.items() if key.isalpha()}

    return alpha_dic




      