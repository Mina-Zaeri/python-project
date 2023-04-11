import sqlite3
class LibDatabase:
    def __init__(self):
        
        self.connection = sqlite3.connect('dbtest2.db')#:memory:
        self.cursor = self.connection.cursor()

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS  books(
            isbn text PRIMARY KEY,
            title text,
            author text,
            available integer
    
            )""")

    

    def insertBook(self,book):  
        try:
            with self.connection:
               
                   self.cursor.execute("INSERT INTO books VALUES(:isbn,:title,:author,:available)",{'isbn':book.isbn,'title':book.title,'author':book.author,'available':book.available})
               
        except:
             pass
    def search(self,search_arg):
        with self.connection:
            search_arg = '%'+search_arg+'%'
            self.cursor.execute('SELECT * FROM books WHERE isbn LIKE ? OR author LIKE ? OR title LIKE ?',(search_arg,search_arg,search_arg))
            return self.cursor.fetchall()   
           
          
    def getBooks(self):
            with self.conn:
                self.c.execute('SELECT * FROM books')
            return self.c.fetchall()
    def issue_book(self,book):
       with self.connection:
           self.cursor.execute(''' UPDATE books
              SET available = ?
              WHERE isbn = ?''',(book.available-1,book.isbn))
           # self.cursor.execute("""UPDATE books 
           #                WHERE title=:title AND 'author':author""",
           #                {'title':book.title, 'author':book.author, 'available':book.available-1})
                          
    def return_book(self,b):
            with self.conn:
                self.c.execute("""UPDATE books SET issued=:issued)",
                          WHERE title=:title AND 'author':author""",
                          {'title':b.title, 'author':b.author, 'available':b.available})
                          
    def remove_book(self,b):
            with self.conn:
                self.c.execute("""DELETE from books WHERE title=:title AND author=:author""",
                          {'title':b.title, 'author':b.author})
                
