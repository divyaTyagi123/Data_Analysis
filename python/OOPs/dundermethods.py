"""
dunder methods are special methods in python that start and end with '__' 
they automatically get called when you perform certain actions on an object 
they can help :
* customize behaviour of your class
* make your class objects behave like built-in data types (like strings , lists, etc)
"""

class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"hello how are you and your name is {self.name}"

    def __add__(self,other):
        return f"{self.age + other.age}"
    
    
    
obj = Animal("lion", 12)
obj2 = Animal("Dolphin" , 14)

print(obj + obj2)