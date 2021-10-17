"""
George Sucuzhanay
Madlibs Project
"""
# Possibles Ideas:
# - creating a huge string and then concatenate
# -  must use for loops
# - possible look how to capitalize the first word of a sentence

# <-------------------------------------------------------------------------------------->
# MAKE SURE TO MAKE MORE THAN ONE COMMITS SHOWING YOU PROGRESSIVELY WORKED ON THE PROJECT
# POINTS DEDUCTED!
# <-------------------------------------------------------------------------------------->

from random import randrange

def randomVerb():
    verbs = ['ate','walked','slept','behave', 'belong', 'hold']
    i = randrange(0,len(verbs))
    item = verbs[i]
    return item

# print(randomVerb())

def randomNoun():
    nouns = ['dog','hammer','cat','car','frog', 'horse', "John", 'dragon', 'home']
    i = randrange(0,len(nouns))
    item = nouns[i]
    return item
 
# print(randomNoun())

def madlib(randomNoun, randomVerb):
    myStoryLine1 = "One day, Gerald and Piggie decided to go on a " + randomNoun + ". Gerald and Piggie began to " + randomVerb + ". Gerald asks if they need to pack " + randomNoun + "."
    myStoryLine2 = "Piggie tells Gerald that when she returns to make sure to get"
    return myStoryLine1 + myStoryLine2

# print(madlib(randomNoun(), randomVerb()))

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.

# Practice Function:
def working(myStoryLineEx):
    testing = myStoryLineEx.split()
    # print(testing)
    newList = []
    for items in testing:
        if (items == '<noun>' or items == '<noun>,' or items == '<noun>.'):
            print("this conditional is true and its a noun")
            i = randomNoun()
            newList.append(i)
            # print(items)
        elif(items == '<verb>' or items == '<verb>,' or items == '<verbs>.'):
            print("this conditonal is working and its a verb")
            i = randomVerb()
            newList.append(i)
        else:
            newList.append(items)
    return newList

myStoryLineEx = "One day, Gerald and Piggie decided to go on a <noun>. Gerald and Piggie began to <verb>. Gerald asks if they need to pack <noun>."
print(working(myStoryLineEx))