#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:36:30 2023

@author: Stish
"""


#%%
import sqlite3


# conn = sqlite3.connect(':memory:')
class Dbase:
    def __init__(self):
        
        self.conn = sqlite3.connect('data.db')
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS  books(
            isbn text PRIMARY KEY,
            title text,
            author text,
            available integer
    
            )""")

    

    def insertBook(self,b):  
        try:
            with self.conn:
               
                   self.c.execute("INSERT INTO books VALUES(:isbn,:title,:author,:available)",{'isbn':b.isbn,'title':b.title,'author':b.author,'available':b.available})
               
        except:
             pass
    def search(self,opt,s):
            s = '%'+s+'%'
            cmd = f'SELECT * FROM books WHERE {opt} LIKE :s'
            if opt in ['title','author']:
               # c.execute('SELECT * FROM books WHERE title LIKE :s', {'s':s})
                self.c.execute(cmd, {'s':s})
                # c.execute('SELECT * FROM books WHERE title =:s', {'s':s})
            else: 
                self.c.execute('SELECT * FROM books WHERE author LIKE :s', {'s':s})
                # c.execute('SELECT * FROM books WHERE author =:s', {'s':s})
            return self.c.fetchall()    
          
    def getBooks(self):
            with self.conn:
                self.c.execute('SELECT * FROM books')
            return self.c.fetchall()
    def issue_book(self,b):
            with self.conn:
                self.c.execute("""UPDATE books SET issued=:issued)",
                          WHERE title=:title AND 'author':author""",
                          {'title':b.title, 'author':b.author, 'available':b.available})
                          
    def return_book(self,b):
            with self.conn:
                self.c.execute("""UPDATE books SET issued=:issued)",
                          WHERE title=:title AND 'author':author""",
                          {'title':b.title, 'author':b.author, 'available':b.available})
                          
    def remove_book(self,b):
            with self.conn:
                self.c.execute("""DELETE from books WHERE title=:title AND author=:author""",
                          {'title':b.title, 'author':b.author})
                


#%%
db=Dbase()
#%%
class Book:
    def __init__(self,isbn,title,author,available=3):
        self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.available = available

    def __repr__(self): 
        return f"{self.title}, {self.author}"
#%%
import json

def loadBooks():
    with open('book2.json') as fd:
        books= json.load(fd)
        for b in books:
            nb= Book(b['isbn'],b["title"],b["authors"])
            db.insertBook(nb)

loadBooks()
#%%
print (db.getBooks())
#%%                  
b1 = Book(1,"Harry Potter and the Half-Blood Prince (Harry Potter  #6)",
        "Douglas Adams")

b2= Book(2,"The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)",
           "J.K. Rowling/Mary GrandPré")
b3 = Book(3,"Life at BCU", "Stish Sarna")
b4 = Book(321,"Python Programming", "Stish Sarna")
b5 = Book(123,"Data Structures", "Stish Sarna")
# #%%
db.insertBook(b1)
db.insertBook(b3)
db.insertBook(b4)
db.insertBook(b5)
#%%
print('>>', db.search('author',"Stish"))
print('remove')
db.remove_book(b4)
print('>>',db.search('author',"Stish"))
 #%%



# #%%
# conn = sqlite3.connect('test.db')
# c=conn.cursor()
# c.execute("INSERT INTO student VALUES('Stish','sarna',21,'programming21')")
# c.execute("INSERT INTO student VALUES('rita','sarna',22,'programming22')")
# c.execute("INSERT INTO student VALUES('kieran','sarna',23,'programming23')")
# c.execute("INSERT INTO student VALUES('veni','sarna',24,'programming24')")
# c.execute("INSERT INTO student VALUES('shiv','sarna',25,'programming25')")
# conn.commit()
# conn.close()

# #%%
# conn = sqlite3.connect('test.db')
# c=conn.cursor()
# c.execute("SELECT * FROM student WHERE second ='sarna'")
# # print(c.fetchone())
# # print(c.fetchmany(5))
# print(c.fetchall()) # returns in a list
# conn.commit()
# conn.close()

# #%%
# s = Student('STISH',"SARNA",888,'PYTHON')
# s2 = Student('RITA',"SARNA",786,'c#')
# conn = sqlite3.connect('test.db')
# c=conn.cursor()

# #option-1
# c.execute("INSERT INTO student VALUES(?,?,?,?)",(s.f,s.s,s.age,s.course))
# conn.commit()

# #option-2 better
# c.execute("INSERT INTO student VALUES(:f,:s,:age,:course)",
#           {'f':s2.f,'s':s2.s,'age':s2.age,'course':s2.course})
# conn.commit()
# c.execute("SELECT * FROM student WHERE second ='SARNA'")
# print(c.fetchall()) # returns in a list

# conn.close()

#%%
# conn = sqlite3.connect('test.db')
# c=conn.cursor()
# # c.execute("SELECT * FROM student WHERE second =?",('sarna',))
# c.execute("SELECT * FROM student WHERE second =:last",{'last':'SARNA'})
# # print(c.fetchone())
# # print(c.fetchmany(5))
# print(c.fetchall()) # returns in a list
# conn.commit()
# conn.close()

#%%
# import sqlite3

# conn = sqlite3.connect('mysqlite.db')
# c = conn.cursor()
# 			
# #get the count of tables with the name
# c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students1' ''')

# #if the count is 1, then table exists
# if c.fetchone()[0]==1 : 
# 	print('Table exists.')
# else :
# 	print('Table does not exist.')
# 			
# #commit the changes to db			
# conn.commit()
# #close the connection
# conn.close()
