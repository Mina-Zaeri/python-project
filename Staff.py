from User import User
from LibDatabase import LibDatabase
from Book import Book
import json
class Staff(User):
    
    def __init__(self, name, userid, staffDept,account):#account agregation shode
        super().__init__(name, userid)
        self.staffDept = staffDept
        self.account=account

    def menu(self):
        print("""
              1.Borrow
              2.Return
              3.Calculate fine
              q.Quit
              
              """)         
        opt_staff=input ("Please input the number of option:")
        
        if opt_staff=="1" :
            self.handle_borrowed_book()
        elif opt_staff=="2" :
           self.handle_return_book()
            
    def handle_borrowed_book(self):
        #we can show teh all books
        
        search_arg=input("*************\nPlease inter part or compelte of author's name or isbn number or book's name:")
        show=LibDatabase()
        result=show.search(search_arg)
        if result ==[]  :
            print ("There is no any book with this info")

        else : 
            for book in result:
                
                print (f"""Title:{book[1]} 
                           Isbn:{book[0]}
                           Athour:{book[2]}
                           Availabe:{book[3]}""")
           
                
            isbn=input ("These are all of books available \nNow import the isbn number is selected:")  
            bookclass=None
            for book in result:
                if isbn==book[0] and book[3]:
                    bookclass=Book(book[1],book[2],book[0],book[3]) #instance az class book
                    
            if bookclass==None:
                print ("book not found or not avaliable")
                return 0
            result=show.issue_book(bookclass)
            self.account.add_borrowed_book(bookclass)
            
    def handle_return_book(self):
        with open("accounts.json", "r") as fd:
            accounts_info = json.load(fd)
            #print("self.userid",self.userid)
            #print("accounts_info[self.userid]",accounts_info[self.userid])
            result=accounts_info[self.userid]["l_books_borrowed"]
            #print("accounts_info[self.userid][l_books_borrowed]",result)
            for book in result:
                
                print (f"""Title:{book['title']} 
                           Isbn:{book['isbn']}
                           Athour:{book['author']}
                           """)
                           
            isbn=input ("These are all of books you borrowed \nNow import the isbn number to return:")  
            bookclass=None
            # print(result)
            for book in result:
                # if isbn==book['isbn'] and book['availabe']>1:
       
                # elif isbn==book['isbn']and book['availabe']==1:
                if isbn==book['isbn']:
                    bookclass=Book(book['title'],book['author'],book['isbn'],1)
                    # print("bookclass",bookclass)
                    
                    self.account.add_return_book(bookclass)
                    

                
           