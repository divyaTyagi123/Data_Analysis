"""
1. Inheritance
    types of inheritance
    1. Single inheritance
    2. Multiple ineritance (two parent class , only one child class)
2. Polymorphism
3. Encapsulation
4. Abstraction  - doesn't exist in python, we can achieve it using a library, define common interface for diff subclasses
"""


# class A:           # super class
#     a = "I am an attribute in A"
#     def hello(self):
#         print("Hello i am a method in A")

# class B(A):   # inherit A (accepts a class as parameter)
#     pass


# obj = A()

# obj2 = B()

# print(obj.a)
# print(obj2.a)

# obj2.hello()

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def show(self):
#         print(f"hello your name is {self.name}")

# class Human(Animal):
#     def __init__(self, name , age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"hello your name is {self.name},{self.age}")

    
# animal1 = Animal("lion")
# person1 = Human("Div",21)
# person1.show()

# class Animal :
#     name = "lion"

# class Human:
#     name2 = "Div"

# class Robot(Animal , Human):
#     name3 = "Charlie"

# obj = Robot()

# print(obj.name)
# print(obj.name2)
# print(obj.name3)


# polymorphism overriding , python doesn't support over loading
# def show():
#     print("You are best")

# show()

# def show():
#     print("You are amazing")

# show()

# class Animal:
#     def show(self):
#         print("hello i am divya")

#     """def show(self , name):
#         print(f"i am {name}")"""  # not exist in python

# class Human(Animal):
#     def show(self):              # method overriding
#         print("how are you")

# obj = Human()
# obj.show()


"""
Duck Typing

class Animal:
    def show(self):
        print("i am duck")

class Human:
    def show(self):
        print("Hello i am also a duck")

obj = Animal()
obj2 = Human()

obj.show()         i am duck
obj2.show()        Hello i am also a duck
"""


# Encapsulation
"""
Access Modifiers
1. Public - inherited classes and objects can access them 
2. Protected - created using a single underscore '_' but it still can be accesssed from outside the class. Python doesn't enforce protected access like other languages but it uses a naming convention to tell developers.
3. Private - it cannot be accessed from outside the class , only inside the class , created using '__' 
"""

class Factory:
    __a = "pune"

    def _show(self):           # protected
        print("hello i am a pune factory")

class Bhopal(Factory):
    def show2(self):
        print(super().__a)       # AttributeError: 'super' object has no attribute '_Bhopal__a'

obj = Bhopal()
obj.show2()       

# Abstraction 
from abc import ABC, abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def are(self):
        pass


class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        print("i have created")
    
    def area(self):
        print("i have created this")
    
obj = Circle()
