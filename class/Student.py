import User

class Student(User):
    def __init__(self,name,uid,uclass):
        super().__init__(name,uid,account)
        self.uclass=uclass
        
    @staticmethod
    def foo(self):
         print ("foo")  
    def menu(self):
      while True:
             print ("""
                 -menu-
                 1:Draw book Student
                 2:Retuern
                 3:Search 
                 4-reserevd
                 5-finance
                   """)
                   
             choice= input("please select your option:")  
             f={"1".self.foo,
                "2":self.foo,
                "3":self. foo,
                "q"::None}.get(choice,None)
           if choice =="q" or choice=="Q"
              break
          elif f==None:
              print ("Try again..")
          else :
              f()

      ip=input ("select option:")
      c={
          "1":'opt1',
          "2":'opt2',
          "3":'opt3',
          "q":'optq'
          }.get(ip,None)
      if c==None:
          print ("try again..")
      else:
          Student.foo()
