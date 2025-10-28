
class Factory :
    a = 12  # attribute

    def hello(self):       #
        print("How are you")

    print("Hello i am getting initialized")   # run only once


print(Factory().a)
Factory().hello()
Factory.a

"""
Constructor => special method that is called automatically when an object is created from a class. its main role is to initialize the object by setting up its attributes or state.
* the method __new__ is the constructor that creates a new instance of the class while __init__ is the initializer that sets up the instance's attributes after creation  

* __new__ method : responsible for creating a new instance of a class. it allocates memory and returns the new object. it is called before __init__.
class ClassName : 
    def __new__(cls, parameters):
        instance = super(ClassName, cls).__new__(cls) return instance

* __init__ method: this method initializes the newly created instance and is commonly used as a constructor in python. it is called immediately after the object is created by __new__ method and is responsible for initializing attributes of the instance.
class ClassName:
    def __init__(self,parameters):
        self.attribute = valu
"""

class Factory :
    def __init__(self,material,zips,pockets):  # self contains the location of object 
        print(self)
        self.material = material
        self.zips = zips
        self.pockets = pockets
    
    def show(self):
        print(f"your object details are {self.material}, {self.pockets},{self.zips}")


reebok = Factory("leather", 3 , 2)

campus = Factory("nylon", 3 , 3)

print(reebok.pockets)
print(campus.pockets)

reebok.show()

