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
