"""
Decorator  -- >  just a function that modifies another function without changing its actual code.
                 for creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.

"""


def decorate(func):     # func is a parameter that will take our function as argument 
    def wrapper():
        print("I will print myself before function hello")
        func()
        print("I will print after the  function ")
    return wrapper


@decorate
def hello():
    print("Hello i am divya")

hello()

#  decorator function captures our original function 
#  wrapper captures all parameters
def adder(func):    
    def wrapper(a,b):
        print("the addition to your numbers are")
        func(a,b)
        print("thankyou i hope your experience with us is amazing")
    return wrapper

@adder
def addition(a,b):
    print(f"{a} + {b} = {a+b}")

addition(34,68)


#  in addition if user give more than 2 arguments 

# for that we use args and kargs