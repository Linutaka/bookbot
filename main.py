def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def num_words(words):
    words_list = words.split()
    return len(words_list)

def main():
    book = get_book_text("/home/robert/projects/bookbot/books/frankenstein.txt")
    print(book)

    words = num_words(book)
    print(f"{words} words found in the document")


main()