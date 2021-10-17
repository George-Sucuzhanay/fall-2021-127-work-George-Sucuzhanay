"""
George Sucuzhanay
Madlibs Project
"""

from random import randrange

def randomVerb():
    verbs = ['eat','walk','sleep','fight', 'scream', 'jump', 'sing', 'laugh']
    i = randrange(0,len(verbs))
    item = verbs[i]
    return item

def randomNoun():
    nouns = ['dog','hammer','cat','car','frog', 'horse', "rabbit", 'dragon', 'home', 'park', 'zoo', 'computer']
    i = randrange(0,len(nouns))
    item = nouns[i]
    return item
 
def firstsentence():
    testing = myStoryLineEx.split()
    newList = []
    for items in testing:
        if (items == '<noun>'):
            items = randomNoun()
            newList.append(items)
        elif (items == '<noun>,'):
            items = randomNoun()
            newList.append(items + ",")
        elif(items == '<noun>.'):
            items = randomNoun()
            newList.append(items + ".")
        elif(items == '<verb>'):
            items = randomVerb()
            newList.append(items)
        elif(items == '<verb>,'):
            items = randomVerb()
            newList.append(items + ",")
        elif(items == '<verb>.'):
            items = randomVerb()
            newList.append(items + ".")
        else:
            newList.append(items)
    return ' '.join(newList)

def secondsentence():
    testing2 = myStoryLineEx2.split()
    newList2 = []
    for words in testing2:
        if (words == '<noun>'):
            words = randomNoun()
            newList2.append(words)
        elif (words == '<noun>,'):
            words = randomNoun()
            newList2.append(words + ",")
        elif (words == '<noun>.'):
            words = randomNoun()
            newList2.append(words + ".")
        elif(words == '<verb>'):
            words = randomVerb()
            newList2.append(words)
        elif (words == '<verb>,'):
            words = randomVerb()
            newList2.append(words + ",")
        elif (words == '<verb>.'):
            words = randomVerb()
            newList2.append(words + ".")
        else:
            newList2.append(words)
    return ' '.join(newList2)

myStoryLineEx = "One day, Gerald and Piggie decided to go on a <noun>. Gerald and Piggie began to <verb>. Gerald asks if they need to pack a <noun>. to go to the <noun>. It was sad to hear that Gerald is wanting to <verb> Piggie." 
myStoryLineEx2 = "Piggie tells Gerald that she has to bring her <noun> since Piggie is wanting to <verb> him. Gerald notices that Piggie forgot her <noun>, and he <verb>. The next day Piggie and Gerald went to the <noun> and saw a <noun> on a chair. Both Piggie and Gerald made sure to bring a <noun>."

print(firstsentence())
print(secondsentence())
