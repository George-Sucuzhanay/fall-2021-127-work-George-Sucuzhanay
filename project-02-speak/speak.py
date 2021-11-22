# -*- coding: utf-8 -*-
# George Sucuzhanay

# Task:
# Create a program name speak.py. This program will read it’s input from a file named input.txt and will convert it to piratespeak and print out the result.

# Your program will take an text file named input.txt and read it in and use the dictionary (described below) to translate the contents of input.txt to pirate-speak. Your program should print out the results.

# Notes:
# make more than 1 commit 

# use a dictionary of pirate traslations
# the story line must be in a input.txt textfile

# Extra:
# use a data text file and import it

def build_substitution_dictionary(filename):
    d = {}
    f = open(filename)
    for line in f.readlines():
        line = line.strip('\n')
        (part,word) = line.split(':')
        d.setdefault(part,[])
        d[part].append(word)
    return d   
# work on substuitiing the pirate.dat with input.txt
def madlibify(story,substitutions):
    result_list = []
    # a = substitutions["hi"] == "hi" # false!
  
    # print(substitutions["hi"])
    # print(type(substitutions["hi"][0]))

    for word in story.split():
        lastchar = word[-1]
        if lastchar in ".!?,":
            word = word.rstrip(lastchar)
            suffix=lastchar
        else:
            suffix=''
        for key in substitutions.keys():
            if word == key:
                print(key, "  => this key matches if a word in the textfile")
                # finalizing accessing subsitutions keys
                # by the looking of things substitutions["hi"] == "hi" are NOT the SAME!!
                newword = substitutions[word][0]
                # trouble accessing the list inside of the dict values
            else:
                newword = word
                print(newword)
        newword = newword + suffix

        result_list.append(newword)
        print(result_list)
    return " ".join(result_list)

def main():
    story = open("project-02-speak/input.txt").read()
    substitution = build_substitution_dictionary("project-02-speak/pirate.dat")
    print(substitution)
    result = madlibify(story,substitution)
    print(result)

if __name__=="__main__":
    main()