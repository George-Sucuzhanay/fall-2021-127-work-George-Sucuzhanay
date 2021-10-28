# Dictionaries
# main data strcutire in Python

# We use lists in Python to 
    # 1) have many items of the same type 
    # 2) access by index(number)
    # 3) has order

# In dictionaries aka key/value pairs or key/value store
# They store multiples of different types

# hash, hash table and hash map => refer to this similar concept

# this is an empty dictionary
d = {}

# we put things in with the  [] notation

d['one'] = "hello"
d['two'] = 45
d[3] = ["a", "list", "of", "items"]
# print(d)

# to access
# print(d['two'])

# reassigning
d['two'] = "New stuff"
d['hello'] = 'world'

print(d)

d[3][1] = "replaced list with this"
print(d[3])
print(d)

# we can initialize it inline

d2 ={
    'first' : 'Bugs', 
    'last' : 'bunny',
    3 : 1945,
    "subdict" : {1:2, "a":"b"},
    'sublist': [1,2,3,4,5],

}

k = d2.keys()
print(k)

v = d2.values()
print(v)

for key in d2.keys():
    print(key)
for val in d2.values():
    print(val)

# in dictionaires ORDER DOES NOT MATTER!!!! only list do

# deleting keys
del(d['hello'])


