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
    verbs = ['ate','walked','slept']
    i = randrange(len(verbs))
    item = verbs[i]
    return verbs[i]

print(randomVerb())

def randomNoun():
    nouns=['dog','hammer','cat','car','frog']
    i = randrange(len(nouns))
    item = nouns[i]
    return nouns[i]
    
print(randomNoun())

def madlib(randomNoun, randomVerb):
    pass

# from random import randrange

# movie_list = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 'The Shawshank Redemption', 'Pulp Fiction']

# # get random index number
# i = randrange(len(movie_list))
# item = movie_list[i]
# # Select item using index number
# print("Randomly selected item", movie_list[i], "is present at index:", i)

# # Output Randomly selected item Citizen Kane is present at index: 2

# When run, it should print out at least two original sentences each followed by two different madlab outputs for each.
# These sentences can be declared as multiline (triple quote) strings in your program.
