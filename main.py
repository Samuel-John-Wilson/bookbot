# Bookbot Project, 23-4-25 - Samuel Wilson



from stats import get_book_text
from stats import word_count
from stats import character_count
from stats import get_only_alpha

#def main(path_to_file):
#    text = get_book_text(path_to_file)
#    print(text)

            

#Franken_Count = character_count('books/frankenstein.txt')

def print_counts(path_to_file):
    print(f"{word_count(path_to_file)} Words found in the document")
    print(f"Characters found: {character_count(path_to_file)}")

#print_counts('books/frankenstein.txt')




