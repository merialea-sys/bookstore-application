from helpers import (
    exit_program,
    display_books,
    lookup_book_by_title,
    add_book,
    remove_book,
    display_authors,
    lookup_author_by_name,
    add_author,
    remove_author,
    display_genres,
    display_books_by_author_id,
)

def main():
    while True:
        menu()
        choice = input(">")
        if choice == "0":
            exit_program()
        elif choice == "1":
            display_books()
        elif choice == "2":
            lookup_book_by_title()
        elif choice == "3":
            add_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            display_authors()
        elif choice == "6":
            lookup_author_by_name()
        elif choice == "7":
            add_author()
        elif choice == "8":
            remove_author()
        elif choice == "9":
            display_genres()
        elif choice == "10":
            display_books_by_author_id()
        else:
            print("Invalid choice. Please try again.")
        
def menu():
    print("Please select an option:")
    print("0: Exit")
    print("1: Display all books")
    print("2: Lookup book by title")
    print("3: Add a new book")
    print("4: Remove a book")
    print("5: Display all authors")
    print("6: Lookup author by name")
    print("7: Add a new author")
    print("8: Remove an author")
    print("9: Display all genres")
    print("10: Display books of the given author_id")
            

if __name__ == "__main__":
    main()
