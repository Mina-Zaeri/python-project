# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 11:05:50 2023

@author: id003941
"""
import json

class LibManSystem:
 
    def __init__(self):
        self.db=LibDatabase()
        LibManSystem.loadBooks(self.db)
       
        LibManSystem.login()
        
    
    @staticmethod
    def loadBooks(db):
        with open("data.json", "r") as fd:
            books = json.load(fd)
        for b in books:
            # print(b['isbn'], b['title'])
            LibDatabase.dBooks[b['isbn']] = Book(b["isbn"], 
                                                 b["title"],
                                                 b["authors"])
            db.insertBook()
    @classmethod                                            
    def authenticate(cls,uid,pswd):
        with open("login.json", "r") as fd:
            acc = json.load(fd)
            # print(acc)  
        if uid in acc:
            if acc[uid]['pswd'] == pswd:
                return True, acc[uid]
        return False, None
    
    @classmethod       
    def login(cls):
        print("Welcome to BCU Lib System")
        uid = input("Enter uid: ")
        pswd = input("Enter your password: ")
        v, u = LibManSystem.authenticate(uid, pswd)
        if v:
            print("Welcome....")
            if u["uType"] == "Staff":
                usr = Staff(u["name"],uid,u["dept"])
                usr.menu()
            elif u["uType"] == "Student":
                usr = Student(u["name"],uid,u["class"])
                usr.menu()
            elif u["uType"] == "Libarian":
                pass
            else:
                print("Data error")
            

        else:
            print("Login failure")
            
            
    def reg():
        pass
    def logout():
        pass
    
#%%
class Book:
    def __init__(self, title, author, isbn):
      self.title = title
      self.author = author
      self.isbn = isbn
    
    def __repr__(self):
        return f"""
{self.title}
    ~ {self.author}
    """
    


#%%
class LibDatabase:
    dBooks = {}
    def __init__(self):
        pass
    
#%%
class User:
    def __init__(self,name, uid):
        self.name = name
        self.uid = uid

        
    def __repr__(self):
        return f"{self.name}"
    


class Student(User): 
    b_limit = 3
    def __init__(self,f,s,dept,acc=None):
        super().__init__(f,s,acc)
        self.d = dept

    def menu(self):
        print(f"""menu for Student
1. Option 1  ~search
2. Option 2 ~List borrowed books
3. Option 3 ~Add book
4. Option 4 ~User record
q. Return

""")
        while True:
            c = input("\nSelect Option (1-4|q): ")
            choice = {"1" :self.f_opt1,
                  "2" :self.f_opt2,
                  "3" :self.f_opt3,
                  "4" :self.f_opt4,
                  "q" :"q"}.get(c,"invalid")        
            if choice == "q":
                print('Bye..')
                break
            elif choice != "invalid":
                choice()
            else:
                print("Try again...")

    def f_opt1(self):
        print("option-1")
        if 439785960 in self.account.l_books_borrowed:
           self.account.l_books_borrowed.remove(439785960)
           self.account.l_books_borrowed.append(439785960)
        else:
           print ("dfdfdfdf")
    def f_opt2(self):
        print("option-2")
        self.account.printBorrowedBooks()
    def f_opt3(self):
        print("option-3~")
        # check if the book is availble
        fbooks=bcu.db.search("title","harry")
        for i,v in enumerate((fbooks),strat=1) :
            print (i,v)
        lc=len(fbooks)
        choice =int (input("select:"))
        if choice <=lc:
            print (f"choice selected {fbooks [choice-1].isbn}")
        else:
            print ("go slow")
        self.account.l_books_borrowed.append(439785960)
        self.account.l_books_borrowed.append(fbooks[choice-1].isbn)
        # print(f">>Saving: {LibaryData.d_books.get(439785960,'Unkown')}")
        # update file
    def f_opt4(self):
        # print current status
        print(self)
    def f_ex(self):
        return
    def __repr__(self):
        return f"{self.f}\n {self.account}"
   
    def foo(self):
        print("You called foo")
        
    def menu(self):
        while True:
            print("""
                  1. option-1
                  2. option-2
                  3. option-3
                  q. Quit
                  
                  """) 
            choice = input("Please select your option: ")
            f = {"1": self.foo,
                 "2": self.foo,
                 "3": self.foo,
                 "q": None}.get(choice,None)
            if choice == "q" or choice =="Q":
                break
            elif f == None:
                print("Try again...")
            else:
                f()
                
        
class Staff(User):
    def __init__(self, name, uid, sDept):
        super().__init__(name, uid)
        self.sDept = sDept

    def menu(self):
        print("""
              1. option-1s
              2. option-2s
              3. option-3
              q. Quit
              
              """)         
class Libarian(User):
    pass
        
#%%
bcu = LibManSystem()