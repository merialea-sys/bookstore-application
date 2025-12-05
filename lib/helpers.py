from models.author import Author
from models.book import Book

def exit_program():
    print("Exiting the program. Goodbye!")
    exit()

def display_books():
    books = Book.get_all()
    for book in books:
        print(book)

def lookup_book_by_title():
    title = input("Enter the book title: ")
    book = Book.find_by_title(title)
    print(book) if book else print(f"Book {title} not available.")

def add_book():
    title = input("Enter book title:")
    genre = input("Enter book genre:")
    year = int(input("Enter year of publication:"))
    author_id = int(input("Enter author ID:"))
    try:
        book = Book.create(
            title,
            genre,
            year,
            author_id
        )
        print(f"Book {book.title} added successfully.")
    except ValueError as e:
        print(f"Error adding book: {e}")

def remove_book():
    remove_book_name = input("Enter the name of the book to remove: ")
    if book := Book.find_by_title(remove_book_name):
        book.delete()
        print(f"Author {remove_book_name} removed successfully.")
    else:
        print(f"Author {remove_book_name} not found.")


def display_authors():
    authors = Author.get_all()
    for author in authors:
        print(author)

def lookup_author_by_name():
    name = input("Enter the author's name: ")
    author = Author.find_by_name(name)
    print(author) if author else print(f"Author {name} not found.")

def add_author():
    name = input("Enter author name:")
    email = input("Enter author email:")
    try:
        author = Author.create(
            name,
            email
        )
        print(f"Author {author.name} added successfully.")
    except ValueError as e:
        print(f"Error adding author: {e}")

def remove_author():
    remove_author_name = input("Enter the name of the author to remove: ")
    if author := Author.find_by_name(remove_author_name):
        author.delete()
        print(f"Author {remove_author_name} removed successfully.")
    else:
        print(f"Author {remove_author_name} not found.")

def display_genres():
    genre = input("Enter specific genre: ")
    book = Book.get_by_genre(genre)
    if book:
        print(book)
    else:
        print(f"Genre {genre} is unavailable")


def display_books_by_author_id():
    author_id = input("Enter the author's id: ")
    try:
        author_id_int = int(author_id)
        author = Author.find_by_id(author_id_int)

        if author:
            list_of_books = author.books()

            if list_of_books:
                print(f"Books by {author.name}:")
                for book in list_of_books:
                    print(book)
            else:
                print(f"Author {author.name} (ID: {author_id_int}) has no books available.")

        else:
            print(f"Error: Author ID {author_id_int} not found in the database")

    except ValueError:
        print("invalid input.Please enter a valid integer ID.")

