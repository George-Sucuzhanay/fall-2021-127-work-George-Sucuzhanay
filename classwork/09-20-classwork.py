# # Sept 20, 2021 (Mon)

# def isEven(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# def isEvenTerse(number):
#     return number % 2 == 0

# def isOdd(number):
#     return not isEven(number)

# longString ="""
# Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.
# Email readers can see the video 
# """
# def countLetters(s,letter):
#     """ 
#     count the number of times letter occurs in string s
#     """
#     count = 0
#     for l in s:
#         print(l)


# longString ="""
# Street bands have been picking up the slack for the last year in NYC, performing for outside diners and more throughout the city. This festival celebrates them and puts them front and center.
# Email readers can see the video 
# """
# def countLetters(s,letter):
#     """ 
#     count the number of times letter occurs in string s
#     """
#     count = 0
#     print(s)
#     for l in s:
#         if l==letter.lower() or l==letter.upper():
#             count = count + 1
#     return count 


# def tests():
#     print("IsEven tests")
#     print("isEven(23)",isEven(23))
#     print("isEven(24)",isEven(24))
#     print()
#     print("IsEvenTerse tests")
#     print("isEvenTerse(23)",isEvenTerse(23))
#     print("isEvenTerse(24)",isEvenTerse(24))
#     print()
#     print("IsOdd tests")
#     print("isOdd(23)",isOdd(23))
#     print("isOdd(24)",isOdd(24))
#     print()
#     print("Count letters a in longString")
#     print(countLetters(longString,'A'))

# if __name__=="__main__":
#     # put the stuff here to be run automatically if you
#     # run this file as a program 
#     tests()
    
# Resources
# docs.python.org
# w3schools Python string methods
# String Methods help with string manipulation
# codingbat.com for extra programming exercises for python

# Resources
# docs.python.org
# w3schools Python string methods
# String Methods help with string manipulation
# codingbat.com for extra programming exercises for python

def initialize(name):
    """
    takes a name in the form "First Last" and returns "F. Last"
    ex: initialize("Mike Zamansky") would return "M. Zamansky"
    pass
    """
    last = name.split()
    lastname = last[1]
    newname = name[0] + ". " + lastname
    return newname
    
def capBoth(name):
    """
    takes a name in the form "first last" and returns the  name
    capitalized.
    ex: capBoth("mike zamansky") --> "Mike Zamansky"
    """
    last = name.split()
    lastname = last[1].title()
    firstname = last[0].title()
    newname = firstname + " " + lastname
    return newname

def bondify(name):
    """
    takes a name in the form "first last" and returns 
    "last, first last"
    ex: bondify("James Bond") --> "Bond, James Bond"
    """
    last = name.split()
    lastname = last[1].title()
    firstname = last[0].title()
    newname = lastname + ", " + firstname + " " + lastname
    return newname

def tests():
    # add tests here
    print(initialize("Mike Zamansky"))
    print(capBoth("mike zamansky"))
    print(bondify("James Bond"))

if __name__== "__main__":
    tests()
