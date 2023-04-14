import json

class Account:
    def __init__(self,user_id, password, f_name,l_books_borrowed=[],l_books_reserved=[],
                 history_return=None,l_lost_Books = None, acc_fine=None):
        self.user_id=user_id
        self.password = password
        self.f_name = f_name
        self.l_books_borrowed=l_books_borrowed
        self.l_books_reserved=l_books_reserved
        self.history_return = history_return
        self.l_lost_Books = l_lost_Books
        self.acc_fine = acc_fine
    
    def add_borrowed_book(self,book):
        temp_list=None
        dic={"title":book.title,"author":book.author,"isbn":book.isbn}
        with open("accounts.json", "r") as fd:
            temp_list = json.load(fd)
            temp_list[self.user_id]["l_books_borrowed"].append(dic)

        with open("accounts.json", "w") as fd:
            fd.write(str(temp_list).replace("'", '"'))
            print("succsessful added to your account")
               
       
    
        
    def add_return_book(self,book):
        temp_list=None
        dic={"title":book.title,"author":book.author,"isbn":book.isbn}
        with open("accounts.json", "r") as fd:
            temp_list = json.load(fd)
            data= temp_list[self.user_id]["l_books_borrowed"]
          
          
            for index,bookItem in enumerate(temp_list[self.user_id]["l_books_borrowed"]):
                
                if bookItem['isbn']==book.isbn:
                   #print("mina",bookItem['isbn'],book.isbn)
                   data.pop(index)
            
            
            
                   with open('accounts.json', 'w') as f:
                      json_again = json.dump(temp_list,f)
                     # print(json_again) 
                      print("sucseeful deleted from your account")
                   
                with open("accounts.json", "r") as fd:
                          history_return = json.load(fd)
                          history_return[self.user_id]["history_return"].append(dic)

                with open("accounts.json", "w") as fd:
                          fd.write(str(history_return).replace("'", '"'))
                           
           

      
    
    
    
    def add_decrease_avavilabe_book(self,book):
        pass
    
    
    
    
    
    def add_lost_book(self,book):
        temp_list=None
        dic={"title":book.title,"author":book.author,"isbn":book.isbn}
        with open("accounts.json", "r") as fd:
            temp_list = json.load(fd)
            data= temp_list[self.user_id]["l_books_borrowed"]
          
          
            for index,bookItem in enumerate(temp_list[self.user_id]["l_books_borrowed"]):
                
                if bookItem['isbn']==book.isbn:
                   #print("mina",bookItem['isbn'],book.isbn)
                   data.pop(index)
                   with open('accounts.json', 'w') as f:
                      json.dump(temp_list,f)
                   
                with open("accounts.json", "r") as fd:
                          lost_book = json.load(fd)
                          lost_book[self.user_id]["l_lost_Books"].append(dic)

                with open("accounts.json", "w") as fd:
                          fd.write(str(lost_book).replace("'", '"'))
    
    
                print("lostbook added to the list of lost book in your account ")
                
    
    
    def add_acc_fine_book(self):
            with open("accounts.json", "r") as fd:
                      lost_book = json.load(fd)
                      lost_book[self.user_id]["acc_fine"]= lost_book[self.user_id]["acc_fine"]+10

            with open("accounts.json", "w") as fd:
                      fd.write(str(lost_book).replace("'", '"'))
    
    def print_borrowed_books(self):
           self.report("l_books_borrowed")
           print ("These are all of books you borrowed ")  
            
        
    def printreturnBooks(self):
            
            self.report("history_return")
            print ("These are all of books you returned")  
        
    def printlostBooks(self):
            
           self.report("l_lost_Books")
           print ("These are all of books you lost")
                
                
                
                
    def report(self,select_string):
              with open("accounts.json", "r") as fd:
                  accounts_info = json.load(fd)
              
                  result=accounts_info[self.user_id][select_string]
                              
                  for i,book in enumerate(result,1):
                     
                      print (f"""Title(book{i}):{book['title']} 
                             Isbn:{book['isbn']}
                             Athour:{book['author']}
                             {'*'*30}
                              """)
