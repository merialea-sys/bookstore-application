from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book

def seed_database():
    Book.drop_table()
    Author.drop_table()
    Author.create_table()
    Book.create_table()

    rowling= Author.create("J.K. Rowling", "JKR@gmail.com")
    goerge = Author.create("George R.R. Martin", "GoergeMrtin5@gmail.com")
    tolkien = Author.create("J.R.R. Tolkien", "Tolkien45@gmail.com")
    smith = Author.create("John Smith", "JSmith05@gmail.com")
    maxwell = Author.create("Maxwell Payne", "payneMax@gmail.com")
    gloria = Author.create("Gloria Steinem", "gloriaSteinem@gmail.com")
    Book.create("Harry Potter and the Sorcerer's Stone", "Fantasy", 1997, rowling.id)
    Book.create("A Game of Thrones", "Fantasy", 1996, gloria.id)
    Book.create("The Hobbit", "Thriller", 1937, tolkien.id) 
    Book.create("The Lord of the Rings", "Fantasy", 1954, tolkien.id)
    Book.create("A Clash of Kings", "Horror", 1998, goerge.id)
    Book.create("A Storm of Swords", "Fantasy", 2000, gloria.id)
    Book.create("The Casual Vacancy", "Drama", 2012, rowling.id)
    Book.create("Fire & Blood", "History", 2018, smith.id)
    Book.create("The Silmarillion", "Fantasy", 1977, maxwell.id)


seed_database()