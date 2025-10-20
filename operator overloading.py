class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages + other.pages
b1=Book(142)
b2=Book(126)
print("Total Pages in two Books",b1+b2)
print(type(b1))
print(type(b2))

#Output:
#       Total Pages in two Books 268
#       <class '__main__.Book'>
#       <class '__main__.Book'>
