# square_list(l) <-- square each element of a list so [1,2,3] would return [1,4,9]
# cap_words(l) <-- capitalize each word in a list of words
# find_min(l) <-- return the smallest value in a list of numbers

def square_list(l):
    newList = []
    for i in l:
        newList.append(i ** 2)
    return newList
# do a loop -> filter -> subset of list
# do a loop -> map -> a new list w/ each element modified
# do a loop -> reduce -> a single value
# map() creates a new list with the new conditions
# learning about pure and unpure programming functions

def cap_words(l):
    newList = []
    for i in l:
        newList.append(i.upper())
    return newList

def find_min(l):
    l.sort()
    return l[:1]

# 


def tests():
    # add tests here
    print(square_list([1,2,3]))
    print(cap_words(["words", "apple", "straw", "computer"]))
    print(find_min([6,3,5,2,8,9,10]))


if __name__== "__main__":
    tests()