# sets are unordered , mutable , duplicate 

# stores values in form of hash values


a = {6,8,55,98}

a.add(3)
a.remove(8)
a.pop()
a.clear()

b = {7,99,98,78}

print(a.union(b))              # a|b
print(a.intersection(b))       # a&b
print(a.difference(b))         # b-a

print(a.symmetric_difference(b)) # a^b

b -= a

