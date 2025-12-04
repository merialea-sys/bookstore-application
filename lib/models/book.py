from models.__init__ import CONN, CURSOR
from models.author import Author

class Book:

    all = {}

    def __init__(self, title, genre, year_of_publication, author_id, id=None):
        self.title = title
        self.genre = genre
        self.year_of_publication = year_of_publication
        self.author_id = author_id

    def __repr__(self):
        return f"<Book {self.title}, {self.genre},published: {self.year_of_publication}" + f",Author ID: {self.author_id}>"
                

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")
        
    @property
    def genre(self):
        return self._genre  
    
    @genre.setter
    def genre(self, genre):
        if isinstance(genre,str):
            self._genre = genre
        else:
            raise ValueError("Genre must be a string")
        
    @property
    def year_of_publication(self):
        return self._year_of_publication    
    
    @year_of_publication.setter
    def year_of_publication(self, year):
        if isinstance(year, int) and year > 0:
            self._year_of_publication = year
        else:
            raise ValueError("Year of publication must be a positive integer")
        

    @property
    def author_id(self):
        return self._author_id      
    
    @author_id.setter
    def author_id(self, author_id):
        if isinstance(author_id, int) and author_id > 0:
            self._author_id = author_id
        else:
            raise ValueError("Author ID must be a positive integer")
        
    @classmethod
    def create_table(cls):
        """CREATES THE BOOKS TABLE IF IT DOESN'T EXIST"""
        sql = """
            CREATE TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY,
            title TEXT,
            genre TEXT,
            year_of_publication INTEGER,
            author_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors(author_id)
            )"""
        CURSOR.execute(sql)
        CONN.commit()


    @classmethod
    def drop_table(cls):
        """DROPS THE BOOKS TABLE IF IT EXISTS"""
        sql = """
            DROP TABLE IF EXISTS books
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """SAVES THE BOOK INSTANCE TO THE DATABASE"""
        sql = """
            INSERT INTO books (title, genre, year_of_publication, author_id)
            VALUES (?, ?, ?, ?)
            """
        CURSOR.execute(sql, (self.title, self.genre, self.year_of_publication, self.author_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def delete(self):
        """DELETES THE BOOK INSTANCE FROM THE DATABASE"""
        sql = """
            DELETE FROM books
            WHERE book_id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def create(cls, title, genre,year_of_publication,author_id):
        """CREATES AND SAVES A NEW BOOK INSTANCE TO THE DATABASE"""
        book = cls(title, genre, year_of_publication, author_id)
        book.save()
        return book
    
    @classmethod
    def instance_from_db(cls, row):
        """Returns a list containing a Book object per row from the database"""
        book = cls.all.get(row[0])

        if book:
            book.title = row[1]
            book.genre = row[2]
            book.year_of_publication = row[3]
            book.author_id = row[4]
        else:
            book = cls(row[1], row[2], row[3], row[4])
            book.id = row[0]
            cls.all[book.id] = book
        return book
    
    @classmethod
    def get_all(cls):
        """Returns a list of all Book instances from the database"""
        sql = """
            SELECT * FROM books
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_title(cls, title):
        """Finds a book by its title """
        sql = """
            SELECT * FROM books
            WHERE title = ?
            """
        row = CURSOR.execute(sql, (title,)).fetchone()

        if row:
            return cls.instance_from_db(row)
        else:
            return None

    
    @classmethod
    def get_by_genre(cls, genre):
        """Returns a list of books of the specified genre"""
        sql = """
            SELECT * FROM books
            WHERE genre = ?
            """
        rows = CURSOR.execute(sql, (genre,)).fetchall()

        return [cls.instance_from_db(row) for row in rows]