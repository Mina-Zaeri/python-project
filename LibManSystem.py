import json
from LibDatabase import LibDatabase
from Book import Book
from Account import Account
from Staff import Staff
#from Student import Student
class LibManSystem:
 
    def __init__(self):
        self.db=LibDatabase()
        LibManSystem.loadBooks(self.db)
       
        LibManSystem.login()
        
    
    @staticmethod
    def loadBooks(db):
        with open("book2.json", "r") as fd:
            books = json.load(fd)
            
        for book in books:
            # print(b['isbn'], b['title'])#man ye instance az class BOOK sakhtam
            bookclass=Book(book["title"],book["authors"],book["isbn"],100)
            db.insertBook(bookclass) #pasesh dadam be in insertbook
        
    @classmethod                                            
    def authenticate(cls,userid,password):
        with open("accounts.json", "r") as fd:
            accounts = json.load(fd)
            # print(acc)  
        if userid in accounts:
            if accounts[userid]['password'] == password:
                return True, accounts[userid]
        return False, None
    
    @classmethod       
    def login(cls):
        print("Welcome to BCU Library System")
        userid = input("Enter userid: ")
        password = input("Enter your password: ")
        verify, userinfo = LibManSystem.authenticate(userid, password)
        if verify:
            print("Welcome....")
            if userinfo["user_type"] == "Staff":
                
               #,userinfo["history_return"],userinfo["l_lost_Books"],userinfo["acc_fine"]
                usr = Staff(userinfo["f_name"],userinfo["id"],userinfo["dept"],
                            Account(userinfo["id"], userinfo["password"], userinfo["f_name"],userinfo["l_books_borrowed"],userinfo["l_books_reserved"]))
                usr.menu()
            elif userinfo["user_type"] == "Student":pass
               # usr = Student(userinfo["name"],userid,userinfo["class"])
               # usr.menu()
            elif userinfo["user_type"] == "Libarian":
                pass
            else:
                print("Data error")
            

        else:
            print("Login failure")
            
            
    def reg():
        pass
    def logout():
        pass
    

test=LibManSystem()



