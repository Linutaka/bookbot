import sys

if len(sys.argv) < 2:   # if user forgot to type <path_to_book>   ['main.py', 'books/...txt']
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    book = get_book_text(sys.argv[1])   # nimmt sich aus sys.argv den 2 Listeneintrag ['main.py', 'books/...txt'] <----den hier

    num_words = get_num_words(book)     # holt sich die Menge der Woerter in der .txt Datei

    num_character = get_counting_characters(book)   # text wir in lower Case umgewandelt und jedes einzelne Zeichen in ein Dictionary gepackt und gezaehlt

    sorted = chars_sort(num_character)  # packt Dictioanry in ein List e und sortiert die Nach anzahl des Zeichens absteigend

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if i["char"].isalpha() == True:             # wenn der key "char" ein Letter ist (nach Unicode Database) -> printe ihn und seine haeufigkeit
            ch = i["char"]
            num = i["num"]
            print(f"{ch}: {num}")
    print("============= END ===============")


    

from stats import get_book_text, get_num_words ,get_counting_characters, chars_sort

main()  # starte das Projekt