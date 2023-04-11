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
    
    @classmethod
    def load_account(cls, a_id):
        with open("accounts.json") as fd:
            acc = json.load(fd)
            return Account(acc[user_id]["id"],
                           acc[user_id]["password"], 
                           acc[user_id]["f_name"], 
                           acc[user_id]["l_books_borrowed"], 
                           acc[user_id]["l_books_reserved"],
                           acc[user_id]["l_return_books"],
                           acc[user_id]['l_lost_books'],
                           acc[user_id]["acc_fine"]
                            )
    def add_borrowed_book(self,book):
        with open("accounts.json", "w") as fd:
            accounts = json.load(fd)
            #templist=[book.title,book.author,book.isbn,1]
            accounts[self.user_id]["l_books_borrowed"].append(book)
        
    def printBorrowedBooks(self):
        for i , b in enumerate(self.l_books_borrowed, start=1):
            if i == 1: 
                print('\nBorrowed Books:\n','-'*20)
            print(f"{i}:  {LibaryData.d_books.get(b,'Unkown')}")
            print('-'*20)
        
    def cal_fine(self):
        pass
    def __repr__(self):
        
            
        return f"""{'*'*20}
id: {self.a_id}
books_borrowed: {self.l_books_borrowed}
    """
#         return None
