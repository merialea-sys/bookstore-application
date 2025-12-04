from models.__init__ import CONN, CURSOR

class Author:

    all = {}

    def __init__(self, name, email, id=None):
        self.name = name
        self.email = email
        self.id = id

    def __repr__(self):
        return f"<Author {self.name}, email={self.email}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name,str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        if isinstance(email, str) and len(email) > 0:
            self._email = email
        else:
            raise ValueError("Email must be a non-empty string")
        
    @classmethod
    def create_table(cls):
        """CREATES THE AUTHORS TABLE IF IT DOESN'T EXIST"""
        sql = """
            CREATE TABLE IF NOT EXISTS authors(
            author_id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT
            )"""
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """DROPS THE AUTHORS TABLE IF IT EXISTS"""
        sql = """
            DROP TABLE IF EXISTS authors
            """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert new row in the authors table"""
        sql = """
            INSERT INTO authors (name, email)
            VALUES (?, ?)
            """
        CURSOR.execute(sql, (self.name, self.email))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, email):
        """INITIALIZE AND SAVES A NEW AUTHOR INSTANCE TO THE DATABASE"""
        author = cls(name, email)
        author.save()
        return author
    
    def delete(self):
        """DELETES THE AUTHOR FROM THE DATABASE"""
        sql = """
            DELETE FROM authors
            WHERE author_id = ?
            """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Returns a list containing an Author object per row from the database"""
        author = cls.all.get(row[0])

        if author:
            author.name = row[1]
            author.email = row[2]
        else:
            author = cls(row[1], row[2])
            author.id = row[0]
            cls.all[author.id] = author

        return author
    
    @classmethod
    def get_all(cls):
        """Returns a list of all Author instances from the database"""
        sql = """
            SELECT * FROM authors
            """
        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_name(cls, name):
        """Finds an author by their name """
        sql = """
            SELECT * FROM authors
            WHERE name = ?
            """
        row = CURSOR.execute(sql, (name,)).fetchone()
        
        return cls.instance_from_db(row) if row else None 
    
    @classmethod
    def find_by_id(cls, author_id):
        """Finds an author by their ID"""
        sql = """
            SELECT * FROM authors
            WHERE author_id = ?
            """
        row = CURSOR.execute(sql, (author_id,)).fetchone()
        
        return cls.instance_from_db(row) if row else None 
    
    
    def books(self):
        """Returns a list of books written by the current author"""
        from models.book import Book

        sql = """
            SELECT * FROM books
            WHERE author_id = ?
            """
        CURSOR.execute(sql, (self.id,))
        rows = CURSOR.fetchall()

        return [Book.instance_from_db(row) for row in rows]

    
