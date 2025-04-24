
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
    print(f"{count} words found in the document")