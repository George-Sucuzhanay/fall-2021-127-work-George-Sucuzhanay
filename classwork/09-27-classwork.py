# def fb1():
#     for i in range(1,100):
#         if i % 3 == 0 and i % 5 == 0:
#             print(i,"fizzbuzz")
#         elif i % 3 == 0:
#             print(i,"fizz")
#         elif i % 5 == 0:
#             print(i,"buzz")
#         else:
#             print(i)

# def fb2():
#     for i in range(1,100):
#         output = ""
#         if i % 3 == 0:
#             output = output + "fizz"
#         if i % 5 == 0:
#             output = output + "buzz"
#         if output == "":
#             output = i
#         print(i,output)
# fb2()      


# Don't do this -> from random import *
# this is a bit better --> from random import randrange
# these two options are the way to go
import random
# now we use random to use it ex. random.randrange(5,50)

# this is an alternative if the name is really long
# import random as rnd
# the above let us use rmd as a shorthand for random
# so we can write rnd.randrage(5,50) etc.

def piglatinify(word):
    first = word[0]
    rest = word[1:]
    VOWELS = 'aeiou'
    if first in VOWELS:
        encoded = word + "ay"
    else:
        encoded = rest + first + "ay"
    return encoded 

def piglatinSentence(sentence):
    arrSentence = sentence.split()
    length = len(arrSentence)
    for i in range(length):
      print(piglatinify(arrSentence[i]))

def listExample():
    l = [5,2,3,10,15,20]
    z = 0 
    for item in l:
        if item == 3:
            z = z + 1
    print(z)
    # adds 1 to each of the items in the list
    for i in range(len(l)):
        l[i] = l[i] + 1
    print(l)


def tests():
    # add tests here
    piglatinSentence("I love working at The Coding Space")
    listExample()


if __name__== "__main__":
    tests()