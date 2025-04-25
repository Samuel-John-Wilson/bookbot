# Bookbot Project, 23-4-25 - Samuel Wilson



import sys
from stats import get_book_text
from stats import word_count
from stats import character_count
from stats import get_only_alpha
from stats import sort_on
from stats import dictionary_to_list

def main(path_to_file):
    
    # Print dynamic heading and introduction
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------") 
    print(f"Found {word_count(path_to_file)} total words")
    print("--------- Character Count -------")
    
    # Get the sorted list of character counts
    sorted_chars = dictionary_to_list(character_count(path_to_file))
    # Print each character and its count
    for char_dict in sorted_chars:
        char = char_dict["char"]
        #Skip non-alphabetical characters
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")

    print("============= END ===============")
        
# if input does not contain the correct number of arguments, print useage message
 

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)        

main(sys.argv[1])
            

#Franken_Count = character_count('books/frankenstein.txt')

# def print_counts(path_to_file):
#    print(f"{word_count(path_to_file)} Words found in the document")
#    print(f"Characters found: {character_count(path_to_file)}")

#print_counts('books/frankenstein.txt')




