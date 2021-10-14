# Possibles Ideas:
# - creating a huge string and then concatenate
# -  must use for loops
# - possible look how to capitalize the first word of a sentence


# - extra of user choice 

# <-------------------------------------------------------------------------------------->
# MAKE SURE TO MAKE MORE THAN ONE COMMITS SHOWING YOU PROGRESSIVELY WORKED ON THE PROJECT
# POINTS DEDUCTED!
# <-------------------------------------------------------------------------------------->

from random import randrange

def randomVerb():
    verbs = ['ate','walked','slept','behave', 'belong', 'hold']
    i = randrange(len(verbs))
    item = verbs[i]
    return verbs[i]

# print(randomVerb())

def randomNoun():
    nouns=['dog','hammer','cat','car','frog', 'horse', "John", 'dragon', 'home']
    i = randrange(len(nouns))
    item = nouns[i]
    return nouns[i]
    
# print(randomNoun())

def madlib(randomNoun, randomVerb):
    myStoryLine1 = "One day, Gerald and Piggie decided to go on a " + randomNoun + ". Gerald and Piggie began to " + randomVerb + ". Gerald asks if they need to pack " + randomNoun + "."
    myStoryLine2 = "Piggie tells Gerald that when she returns to make sure to get"
    return myStoryLine1 + myStoryLine2

print(madlib(randomNoun(), randomVerb()))


# from random import randrange

# movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']


# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.
