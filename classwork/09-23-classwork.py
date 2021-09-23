import random
def piglatinify(word):
    """
    input: a single word
    returns: the word transformed into piglatin
    
    Notes: if the first letter is a vowel, add "ay" to the end
        otherwise move first to end and add "ay" to end
        
    """
    # separate word into first and rest
    first = word[0]
    rest = word[1:]
    # ABCD      A is the first and BCD is the rest
    # if first is a vowel add ay
    VOWELS = "aeiou"
    if first in VOWELS:
        encoded = word + "ay"
    # otherwise move first to last and add ay
    else:
        encoded = rest + first + "ay"
    
    return encoded

    # debugging is 10 times harder than write your code
    # if working on a program : what is the minimal amount of people that work on a programming project
    # you and you two weeks from now   wowowowowowowowo!!!!!!
    # mohamand and henry
    
    
def test():
    s = "hello"
    print(s,piglatinify(s));
    s = "able"
    print(s,piglatinify(s));
    s = "bob"
    print(s,piglatinify(s));


if __name__=="__main__":
    test()