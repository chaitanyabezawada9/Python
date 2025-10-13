class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def get__name(self):
        return self.__name
    def set__name(self, name):
        self.__name = name
    def get__age(self):
        return self.__age
    def set__age(self,age):
        if age >0:
            self.__age = age
        else:
            print("Invalid age. Age must be positive.")
person = Person("Chaitanya",21)
print("Updated Name:",person.get__name())
print("Updated Age:",person.get__age())
person.set__age(-5)
    

#Output:
#Updated Name: Chaitanya
#Updated Age: 21
#Invalid age. Age must be positive.
