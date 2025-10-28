# the thing you accept is parameters
# the thimg you provide to parameter is argument 


#positional argument 
def sum(a,b):
    print(f"Sum of {a} and {b} is {a+b}")

sum(34,23)

#keyword argument
def hello(name,age):
    print(f"your name is {name} and age is {age}")
hello(age = 22, name = "Divya")

#default argument
def sum(a,b=40):
    print(f"the sum is {a+b}")
sum(12)


def square(num):
    return num**2

print(square(36))