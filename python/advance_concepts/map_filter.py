"""
Map  -->
Map is used for applying a function to multiple times.
takes a list (or any sequence)
applies the same funciton to every item in that list 
gives you back a new list(in python 3, it gives a map object which you can convert to a list)

Use map() when you want to transform every iyem in a list
it doesn't remove or skip items (that's what filter() does)
you can use it with lambda or normal functions 

"""

a = [1,2,3,4,5]
result = map(lambda x : x**2 , a)

print(result)    # print object


res = map(lambda x : x%2==0 , a)
print(list(res))          #[False,True,False,True,Fasle]

"""
filter()  -->
takes a list (or other sequence )
checks each item using a function (a test)
kepps only the items that pass the test (i.e. return True)

"""

# def even(x):
#     return x%2==0

a = [1,2,3,4,5,6,7,8,9,10]

result = filter(lambda x : True if x%2 == 0 else False , a)
print(list(result))         # provide items having value True accoring to given function

"""
Module  --> 
    Module is just a single file containing codde and we can use this file ocde in other file 
    a single pyhton file(.py)
    contains functions, variables, or classes
    used to organize and resuse code
    python comes with lots of ready-to-use modules like:
        math , random, datetime

Package -->
    a folder that contains one or more modules, it may also contain sub-packages.
    and you just have to use from and import keywords to use these things.
"""

from math import sqrt

#print(math.sqrt(35))
print(sqrt(34))

from OOPs import intro
