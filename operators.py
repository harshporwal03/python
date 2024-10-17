class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return Book(self.pages + other.pages)

    def __str__(self):
        return f'Book with {self.pages} pages'

b1 = Book(100)
b2 = Book(200)
b3 = b1 + b2
print(b3)

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def __gt__(self,other):
        return self.marks>other.marks
     def __le__(self,other):
        return self.marks<other.marks

  print("10>20=",10>20)
s1=Student("Dayal",100)
s2=Student("Ramesh",200)
print("s1>s2=",s1>s2)   