# -*- coding: utf-8 -*-

# Task:
# Create a program name speak.py. This program will read it’s input from a file named input.txt and will convert it to piratespeak and print out the result.

# Your program will take an text file named input.txt and read it in and use the dictionary (described below) to translate the contents of input.txt to pirate-speak. Your program should print out the results.


# make more than 1 commit 

# use a dictionary of pirate traslations
# the story line must be in a input.txt textfile

# Extra:
# use a data text file and import it

def build_substitution_dictionary(filename):
    d = {}
    f = open(filename)
    for line in f.readlines():
        line = line.strip()
        (part,word) = line.split(':')
        d.setdefault(part,[])
        d[part].append(word)
    return d   

# work on substuitiing the pirate.dat with 
def main():
    # text = open("project-02-speak/input.txt").read()
    substitution = build_substitution_dictionary("project-02-speak/pirate.dat")
    print(substitution)
    # result = madlibify(text,substitution)
    # print(result)
if __name__=="__main__":
    main()