"""
Args and Kwargs -->

they're special keywords in python used in function definitions to accept a flexible number of arguments.
args are used for multiple positional arguments, and 
kwargs are used for multiple keyword arguments

args becomes a tuple and kwargs becomes a dictionary 

helps in building flexible functions , decorators, APIs and more


"""
def adder(func):    
    def wrapper(*args , **kwargs):
        print("the addition to your numbers are")
        func(*args, **kwargs)
        print("thankyou i hope your experience with us is amazing")
    return wrapper

@adder
def addition(a,b):
    print(f"{a} + {b} = {a+b}")

addition(34,68)



def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    
    print(sum)

addition(2,3,66,784,76,2,98)


def information(**kwargs):
    print("Your information is\n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")


information(name = "Divya" , age = 23 , designation = "AI/ML")