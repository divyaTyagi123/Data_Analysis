"""
Used to create List, Dictionary and set.
but you don't have to use multiple lines of code for loops and if-else statements.
"""

# list comprehension
l = [i for i in range(1,21) if i % 2 == 0]

print(l)


# dictionary comprehension

d = {i : i**2 for i in range(1,10)}

print(d)

# set comprehension

even_no = {num for num in range(1,10) if num % 2 == 0}
print(even_no)


"""
Lambda Function -->
an anonymous , inline function defined using the lambda keyword.
it's often used for short , simple functions that are used only once or temporarily.
you can have multiple arguments but there will be only one expression.
"""


addition = lambda a,b : a + b     # provide an object stored in a variable

print(addition(12 , 13))

isEven = lambda a : "even" if a%2 == 0 else "odd"
print(isEven(57))