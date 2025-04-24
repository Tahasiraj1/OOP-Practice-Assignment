class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return cls.total_books
    
book1 = Book("Atomic Habits")
book2 = Book("Rich Dad Poor Dad")
book3 = Book("Clean Code")

print(Book.total_books)

