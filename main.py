def main():
    book = "books/frankenstein.txt"
    text = get_book_text(book)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
   
main()