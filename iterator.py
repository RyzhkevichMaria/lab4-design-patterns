from typing import List


class Book:
    """Книга."""
    
    def __init__(self, title: str):
        self.title = title

    def __str__(self):
        return self.title


class LibraryIterator:
    """Итератор по библиотеке."""
    
    def __init__(self, books: List[Book]):
        self._books = books
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration


class Library:
    """Коллекция книг с поддержкой итератора."""
    
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def __iter__(self):
        return LibraryIterator(self._books)


# Демонстрация
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Война и мир"))
    library.add_book(Book("Преступление и наказание"))
    library.add_book(Book("1984"))

    print("Книги в библиотеке:")
    for book in library:
        print(book)
