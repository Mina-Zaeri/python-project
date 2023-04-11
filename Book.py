class Book:
    def __init__(self, title, author,isbn,available):
      self.title = title
      self.author = author
      self.isbn = isbn
      self.available=available
    
    def __repr__(self):
        return f"""
      {self.title}
    ~ {self.author}
    
    """
    
