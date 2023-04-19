from User import User
from Staff import Staff
from Account import Account
import json

class Libarian(User):
    def __init__(self, name, userid):
        super().__init__(name, userid)
    
    def menu(self):
        print("""
              1.List user
              2.All the Return Books
              3.All the Lost Books
              4.All the Borrowed Books
              q.Quit
              
              """)
        select_option=input("Input the option:")
        if select_option=="1":
           self.user_report()
            
        elif select_option=="2": 
           self.printreturnBooks()
        elif select_option=="3": 
            self.printlostBooks()
        elif select_option=="4": 
            self.printBorrowedBooks()
    
    def user_report(self):
          with open("accounts.json", "r") as fd:
              accounts_info = json.load(fd)
              for account in accounts_info:
                  
                  result=accounts_info[account]["id"]
                  f_name=accounts_info[account]["f_name"]
                  print(f"These are list of user {result}**{f_name}")
              select_user=input("Input id  user: ")
              self.handel_user_acction(select_user) 
                  
                  
                  
    def handel_user_action(self,select_user):
            with open("accounts.json", "r") as fd:
                accounts_info = json.load(fd)
                for account in accounts_info:
                    if account==select_user:
                        if accounts_info[account]["user_type"] == "Staff":
                            #usr ye instans staff hast
                            usr = Staff(accounts_info[account]["f_name"],accounts_info[account]["id"],accounts_info[account]["dept"],
                                    Account(accounts_info[account]["id"],accounts_info[account]["password"], accounts_info[account]["f_name"],accounts_info[account]["l_books_borrowed"],accounts_info[account]["l_books_reserved"],accounts_info[account]["history_return"],accounts_info[account]["l_lost_Books"]))
                            usr.menu()
                        if accounts_info[account]["user_type"] == "Sudent":
                            pass
                  
                 
                  
    
    def printreturnBooks(self):
        
        self.report("history_return")
        print ("These are all of books users returned") 
        
        
    def printlostBooks(self):
         
        self.report("l_lost_Books")
        print ("These are all of books users lost")
        
    def printBorrowedBooks(self):
        self.report("l_books_borrowed")
        print ("These are all of books users borrowed ")     
        
    def report(self,select_string):
          with open("accounts.json", "r") as fd:
              accounts_info = json.load(fd)
              for accountId in accounts_info:
                 
                  result=accounts_info[accountId][select_string]
               
                  
                  f_name=accounts_info[accountId]["f_name"]
                  print(f"these are all the books for {f_name}")
                  for i,book in enumerate(result,0):
                      print("resultttt",book)
                      print (f"""Title(book{i}):{book['title']} 
                         Isbn:{book['isbn']}
                         Athour:{book['author']}
                         {'*'*30}
                          """)
         
              
          
          
          
         