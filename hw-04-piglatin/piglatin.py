# make a file named piglatin.py and copy over the piglatinify function.
# add a function piglatinSentence which will take a string representing a sentence and convert it to piglatin. Remember that you can use split() to split the sentence into words for the for loop - "hello world".split() will result in ["hello","world"] which you can put in a for loop.

def piglatinify(word):
    first = word[0]
    rest = word[1:]
    VOWELS = 'aeiou'
    if first in VOWELS:
        encoded = word + "ay"
    else:
        encoded = rest + first + "ay"
    return encoded 

def piglatinSentence(sentence):
    arrSentence = sentence.split()
    length = len(arrSentence)
    for i in range(length):
      print(piglatinify(arrSentence[i]))

piglatinSentence("I love working at The Coding Space")
         