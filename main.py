import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book = get_book_text(sys.argv[1])
    #print(book)

    num_words = get_num_words(book)
    #print(f"{num_words} words found in the document")

    num_character = get_counting_characters(book)
    #print(num_character)

    sorted = chars_sort(num_character)
    #print(sorted)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha() == True:
            ch = i["char"]
            num = i["num"]
            print(f"{ch}: {num}")
    print("============= END ===============")


    

from stats import get_book_text, get_num_words ,get_counting_characters, chars_sort

main()