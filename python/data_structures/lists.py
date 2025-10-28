#List
"""
Mutable: list is utable and we can change it's value after creation
Duplicate: list allows duplicate values to store 
Ordered: list maintains ordered data structures 
Heterogenous: we can store multiple types of data in a single list
"""
a=[32,234,567,75,5,44,41]

#1st way using index

for i in range(len(a)):
    print(a[i])

#2nd way directly on values

for i in a:
    print(i)

# Methods (defined in class)

#help(list)

a.append(6)
a.insert(3,78)
a.extend((45555,8776,67656))
print(a)

a.remove(234)
value = a.pop(234)
idx = a.index(45555)

a[-1] = 98

x = [1,2,3,4,5]

y = x    # deep copy, changes reflect in original

y[0] = 100

print(x)   # [100 , 2 , 3 , 4 , 5]

z = a.copy()   # shallow copy,  returns a shallow copy of a 