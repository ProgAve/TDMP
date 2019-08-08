class Person:
    def __init__(self,name="",age=30):
        self.__name = name
        self.__age = age
    def name(self):
        return self.__name
    def age(self):
        return self.__age

man = Person("Oxana")
man.__setattr__("__age",48)
print("Hello, ",man.name()," ", man.age())