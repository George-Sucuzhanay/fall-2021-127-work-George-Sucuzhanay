# Solution to CS 127 exam
import math

def mathProblem(n,k):
    numerator = (1 + n) ** k
    denominator = math.sqrt(k + 1)
    finalSolution = numerator / denominator
    return finalSolution

print(mathProblem(3,5))

def remove_e(sentence):
    result = ""
    for letter in sentence:
        if letter != 'e':
            result = result + letter
    return result

s = "The letter E will be removed"
print("Sentence  = ",s, "New Sentence: ", remove_e(s))


def box(length,height):
    result = ""
    if height % 2 != 0:
        height = height - 1;
    xs = "X"*length
    os = "O"*length
    for row in range(height // 2):
        result = result + os+'\n'
        result = result + xs+'\n'
    return result 

print(box(5,4))

def makeacronym(w):
    acronym = ""
    w = w.lower()
    for word in w.split():
        acronym = acronym + word[0]
    return acronym
