from User import User
from LibDatabase import LibDatabase
from Book import Book
import json
class Staff(User):
    
    def __init__(self, name, userid, staffDept,account):#account aggregation shode
        super().__init__(name, userid)
        self.staffDept = staffDept
        self.account=account
    
    def menu(self):
        while True:
            print("""
                  1.Borrow Books
                  2.Return Books
                  3.Lost Books
                  4.Report
                  5.Show fine
                  6.Quit
                  
                  """)         
            opt_staff=input ("Please input the number of option:")
            
            if opt_staff=="1" :
                self.handle_borrowed_book()
            elif opt_staff=="2" :
               self.handle_return_book()
            elif opt_staff=="3" :
               self.handle_lost_book()
            elif opt_staff=="4" :
               self.show_report()
            elif opt_staff=="5" :
               self.show_fine()
            elif opt_staff=="6" :
               print("Exiting program...")
               break
            
            
    def exit_program():
      print("Exiting program...")
      quit()
        
    def show_fine(self):
       with open("accounts.json", "r") as fd:
           accounts_info = json.load(fd)
       
           result=accounts_info[self.userid]["acc_fine"]
           print("these your fine:",result)
           
    def handle_borrowed_book(self):##1
        
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
                             Availabe:{book[3]}
                        """)
           
                
            isbn=input ("These are all of books available \n\nNow import the isbn number is selected:")  
            bookclass=None
            for book in result:
                if isbn==book[0] and book[3]:
                    bookclass=Book(book[1],book[2],book[0],book[3]) #instance az class book
                    
            if bookclass==None:
                print ("book not found or not avaliable")
                return 0
            result=show.issue_book(bookclass)
            self.account.add_borrowed_book(bookclass)
            
            
            
    def handle_return_book(self):##2
        with open("accounts.json", "r") as fd:
            accounts_info = json.load(fd)
        
            result=accounts_info[self.userid]["l_books_borrowed"]
            #print("accounts_info[self.userid][l_books_borrowed]",result)
            
            for i,book in enumerate(result,1):
               
                print (f"""Title(book{i}):{book['title']} 
                       Isbn:{book['isbn']}
                       Athour:{book['author']}
                       {'*'*30}
                        """)
  
                    
            isbn=input ("These are all of books you borrowed \n\nNow import the isbn number to return:\n")  
            bookclass=None
           
            for book in result:
                
                if isbn==book['isbn']:
                    bookclass=Book(book['title'],book['author'],book['isbn'],1)
                    self.account.add_return_book(bookclass)
                    

                
    def handle_lost_book(self):##2
          with open("accounts.json", "r") as fd:
              accounts_info = json.load(fd)
          
              result=accounts_info[self.userid]["l_books_borrowed"]
              
              
              for i,book in enumerate(result,1):
                 
                  print (f"""Title(book{i}):{book['title']} 
                         Isbn:{book['isbn']}
                         Athour:{book['author']}
                         {'*'*30}
                          """)
    
                      
              isbn=input ("These are all of books you borrowed \n\nNow import the isbn number that you lost:\n")  
              bookclass=None
             
              for book in result:
                 
                  if isbn==book['isbn']:
                      bookclass=Book(book['title'],book['author'],book['isbn'],1)
                      self.account.add_lost_book(bookclass)
                      self.account.add_acc_fine_book()
                      
                      
    def show_report(self):
            print("""
                   1-Report Borroew Book
                   2-Report Return Book
                   3-Report Lost Book
                                  
                  """)
            select_option=input("Select your option :")
            if select_option =="1":
                
                self.account.print_borrowed_books()
            elif select_option =="2":
                self.account.printreturnBooks()
            elif select_option =="3":
                 self.account.printlostBooks()  
            else:
                print("Enter is not valid")