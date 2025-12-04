from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book


def reset_database():
    Book.drop_table()
    Author.drop_table()
    Author.create_table()
    Book.create_table()

    Author.create ("J.K. Rowling", "JKR@gmail.com")
    Author.create ("George R.R. Martin", "GoergeMrtin5@gmail.com")
    Author.create ("J.R.R. Tolkien", "Tolkien45@gmail.com")
    Book.create("Harry Potter and the Sorcerer's Stone", "Fantasy", 1997, 1)
    Book.create("A Game of Thrones", "Fantasy", 1996, 2)
    Book.create("The Hobbit", "Fantasy", 1937, 3)   