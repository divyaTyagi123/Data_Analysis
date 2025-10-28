"""
Types of Attributes --
1. Class attribute - a normal variable created inside a class is a class attribute 
2. Instance attribute - A attribute created using an instance like self.naem , self.age etc. it is known as instance attribute

Types of methods --
1. instance method
2. class method
3. static method
"""

class Animal :
    name = "lion"  # class variable

    def __init__(self , age):
        self.age = age   # instance variable


    def show(self):      # instance method , self is necessary , can't give 0 argument
        print("how are you")
    
    @classmethod         # class method
    def hello(cls):      # cls target class location
        print(f"how are you {cls.age}")   #cls can't print age here as it is not targeting object

    @staticmethod
    def static():
        print("how are you ")


obj = Animal(12)

obj.show()
obj.hello()