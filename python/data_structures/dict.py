# dictionary
# mutable - you can change , add , or remove key-value pairs after creation 
# duplicates - keys must be unique , but values can be duplicate
# order - dictionary follows insertion order
# heterogenous - can store different types of keys and values
""""
d = {1 : "hello" , 2: "div"}

print(d[1])       # hello

d[1] = "tyagiji"   # change

d.update({5:"hello ji"})   

d[4] = "bonjour"

del d[4]

d.keys()
d.values()

myDict = {10 : "A" , 20: "B" , 30: "C" , 40: "D"}

for i in myDict:
    print(i)   # print keys
    print(myDict[i])   # print values

#  help(dict)

d.clear()

d2 = d.copy()

d.get(40)  # give values for given key
d.items()  # give key value pairs
d.pop(2)
d.popitem()

# merge two dictionaries

a = {10 : 100 , 20 : 200 , 30: 300}
b = {40 : 400 , 50 : 500 , 60 : 600}

for i in a :
    a[i] = b[i]
print(a)
"""


# /*Ques/* - count the frequencies of integers in a list

a = [1,12,3,2,1,12,3,2,1,1,1,1,2,12,3]

dict = {}
for i in a :
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

print(dict)