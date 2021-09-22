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
    
# 5. Add a function pigLatinify(word) to that file which converts a word to piglatin based on the rules below.
# Rules:
# 1. If the word starts with a consonant. move the first letter to the end of the word and add "ay" - for example "word" would become "ordway"
# 2. If the word starts with a vowel, just add "ay" to the end - "order" would become "orderay"
# Make sensible decisions for any special cases that arise.

def pigLatinify(word):
    consonant = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    vowel = ["A", "E", "I", "O", "U"]
    lowerC = [x.lower() for x in consonant]
    lowerV = [x.lower() for x in vowel]

    for i in range(len(consonant)):
        if word[0] == consonant[i] or word[0] ==  lowerC[i]:
            return word[1:] + word[0] + "ay"
        else:
            for i in range(len(vowel)):
                if word[0] == vowel[i] or word[0] == lowerV[i]:
                    return word + "ay"


def tests():
    # add tests here
    print(initialize("Mike Zamansky"))
    print(capBoth("mike zamansky"))
    print(bondify("James Bond"))
    print(pigLatinify("word"))
    print(pigLatinify("order"))

if __name__== "__main__":
    tests()
