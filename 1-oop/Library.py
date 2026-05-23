

class Library:

    def __init__(self,name: str, books: list[str]):
        self.name = name
        self.books = books
    
    def add_book(self, book: str):
        self.books.append(book)

library = Library("City Library", ["Book A", "Book B"])
print(f"Library books: {library.books}")
library.add_book("Book C")
print(f"Books in Library: {library.books}")